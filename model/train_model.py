"""
train_model.py
---------------
OptiCrop - Smart Agricultural Production Optimization Engine
End-to-end model training pipeline:
    1. Load dataset
    2. Univariate / Bivariate / Multivariate EDA (plots saved to /model/plots)
    3. Null value check
    4. Outlier handling (IQR method)
    5. Seasonal crop extraction
    6. Train/test split
    7. K-Means clustering (Elbow method)
    8. Logistic Regression model training
    9. Evaluation (classification report)
    10. Save trained model + label reference as model.pkl
"""

import os
import pickle
import warnings

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

warnings.filterwarnings("ignore")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "Crop_recommendation.csv")
PLOTS_DIR = os.path.join(BASE_DIR, "model", "plots")
MODEL_PATH = os.path.join(BASE_DIR, "model", "model.pkl")

os.makedirs(PLOTS_DIR, exist_ok=True)

pd.set_option("display.max_columns", None)
plt.rcParams["figure.figsize"] = (12, 8)

# ---------------------------------------------------------------------------
# 1. Read the dataset
# ---------------------------------------------------------------------------
data = pd.read_csv(DATA_PATH)
df = data.rename(columns={"N": "nitrogen", "P": "phosphorous", "K": "potassium"})
print("Dataset shape:", df.shape)
print(df.head())

# ---------------------------------------------------------------------------
# 2. Univariate analysis
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(2, 4, figsize=(16, 8))
fig.suptitle("Distribution of agricultural conditions")
cols = ["nitrogen", "phosphorous", "potassium", "temperature", "humidity", "ph", "rainfall"]
for ax, col in zip(axes.flat, cols):
    sns.histplot(df[col], kde=True, ax=ax)
    ax.set_xlabel(f"Ratio of {col.capitalize()}")
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, "univariate_distribution.png"))
plt.close()

plt.figure(figsize=(10, 5))
sns.countplot(data=df[cols])
plt.savefig(os.path.join(PLOTS_DIR, "feature_countplot.png"))
plt.close()

# ---------------------------------------------------------------------------
# 3. Bivariate analysis - humidity vs label
# ---------------------------------------------------------------------------
plt.figure(figsize=(8, 10))
sns.scatterplot(x=df["humidity"], y=df["label"])
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, "bivariate_humidity_label.png"))
plt.close()

# ---------------------------------------------------------------------------
# 4. Null value check
# ---------------------------------------------------------------------------
print("\nNull values per column:\n", df.isnull().sum())

# ---------------------------------------------------------------------------
# 5. Outlier handling (IQR method) - applied to phosphorous & potassium
# ---------------------------------------------------------------------------
plt.figure(figsize=(8, 4))
sns.boxplot(data=df[cols])
plt.savefig(os.path.join(PLOTS_DIR, "boxplot_before_outlier_removal.png"))
plt.close()

for col in ["phosphorous", "potassium"]:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    filt = (df[col] >= Q1 - 1.5 * IQR) & (df[col] <= Q3 + 1.5 * IQR)
    df = df.loc[filt]

print("\nShape after outlier removal:", df.shape)

# ---------------------------------------------------------------------------
# 6. Seasonal crop extraction
# ---------------------------------------------------------------------------
print("\nSummer crops:")
print(df[(df["temperature"] > 30) & (df["humidity"] > 50)]["label"].unique())
print("\nWinter crops:")
print(df[(df["temperature"] < 20) & (df["humidity"] > 30)]["label"].unique())
print("\nRainy crops:")
print(df[(df["rainfall"] > 200) & (df["humidity"] > 50)]["label"].unique())

# ---------------------------------------------------------------------------
# 7. Train / test split
# ---------------------------------------------------------------------------
y = df["label"]
x = df.drop(["label"], axis=1)

print("\nShape of x:", x.shape)
print("Shape of y:", y.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
print("x_train:", x_train.shape, " x_test:", x_test.shape)
print("y_train:", y_train.shape, " y_test:", y_test.shape)

# ---------------------------------------------------------------------------
# 8. K-Means clustering - Elbow method
# ---------------------------------------------------------------------------
wcss = []
for i in range(1, 11):
    km = KMeans(n_clusters=i, init="k-means++", max_iter=300, n_init=10, random_state=0)
    km.fit(x)
    wcss.append(km.inertia_)

plt.figure(figsize=(10, 4))
plt.plot(range(1, 11), wcss)
plt.title("The Elbow method", fontsize=20)
plt.xlabel("No of clusters")
plt.ylabel("wcss")
plt.savefig(os.path.join(PLOTS_DIR, "elbow_method.png"))
plt.close()

km = KMeans(n_clusters=4, init="k-means++", max_iter=300, n_init=10, random_state=0)
y_means = km.fit_predict(x)
cluster_df = pd.concat(
    [pd.DataFrame(y_means, columns=["cluster"]).reset_index(drop=True),
     df["label"].reset_index(drop=True)],
    axis=1,
)
for c in sorted(cluster_df["cluster"].unique()):
    print(f"\nCrops in cluster {c}:", cluster_df[cluster_df["cluster"] == c]["label"].unique())

# ---------------------------------------------------------------------------
# 9. Logistic Regression model
# ---------------------------------------------------------------------------
model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

cr = classification_report(y_test, y_pred)
print("\nClassification report:\n", cr)

with open(os.path.join(PLOTS_DIR, "classification_report.txt"), "w") as f:
    f.write(cr)

# ---------------------------------------------------------------------------
# 10. Save the trained model
# ---------------------------------------------------------------------------
with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

print(f"\nModel saved to {MODEL_PATH}")

# quick sanity check prediction
sample = pd.DataFrame(
    [[90, 42, 43, 20.87, 82.00, 6.50, 202.93]],
    columns=["nitrogen", "phosphorous", "potassium", "temperature", "humidity", "ph", "rainfall"],
)
print("\nSample prediction for rice-like conditions:", model.predict(sample))
