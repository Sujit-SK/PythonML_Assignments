import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os

# ── Load Dataset ──────────────────────────────────────────────────────────────
base_dir = os.path.join(os.path.dirname(__file__), "..", "..", "Dataset")
df = pd.read_csv(os.path.join(base_dir, "student_performance_ml.csv"))
print("Dataset Shape:", df.shape)
print(df.head())

# ── Derive absences from Attendance (100 - Attendance) ────────────────────────
df["absences"] = 100 - df["Attendance"]

# ── Select Features ───────────────────────────────────────────────────────────
# Mapping to assignment features:
#   PreviousScore  → G1 / G2  (prior grades)
#   FinalResult    → G3       (final grade)
#   StudyHours     → studytime
#   AssignmentsCompleted (inverted) → failures proxy
#   absences       → derived from Attendance
features = ["PreviousScore", "FinalResult", "StudyHours", "AssignmentsCompleted", "absences"]
X = df[features].copy()
print("\nSelected Features:")
print(X.describe())

# ── Scale Features ────────────────────────────────────────────────────────────
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ── Elbow Method to Confirm k=3 ───────────────────────────────────────────────
inertias = []
for k in range(1, 9):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)

plt.figure(figsize=(7, 4))
plt.plot(range(1, 9), inertias, marker="o")
plt.title("Elbow Method – Optimal k")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.tight_layout()
plt.show()

# ── KMeans Clustering (k=3) ───────────────────────────────────────────────────
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X_scaled)

# ── Map Raw Cluster IDs to Meaningful Labels ──────────────────────────────────
# Use centroid of FinalResult to order clusters:
# highest FinalResult mean → Top Performers, lowest → Struggling, middle → Average
centroids = pd.DataFrame(scaler.inverse_transform(kmeans.cluster_centers_), columns=features)
centroids["raw_cluster"] = [0, 1, 2]

rank = centroids.sort_values("FinalResult", ascending=False)["raw_cluster"].tolist()
label_map = {
    rank[0]: "Top Performers",
    rank[1]: "Average Students",
    rank[2]: "Struggling Students",
}
df["Performance Group"] = df["Cluster"].map(label_map)

# ── Cluster Summary ───────────────────────────────────────────────────────────
print("\n── Cluster Centroids (original scale) ──")
print(centroids[features + ["raw_cluster"]].to_string(index=False))

print("\n── Student Count per Group ──")
print(df["Performance Group"].value_counts())

print("\n── Group Statistics ──")
print(df.groupby("Performance Group")[features].mean().round(2))

# ── Visualisation 1: FinalResult vs Absences ─────────────────────────────────
colors = {"Top Performers": "green", "Average Students": "orange", "Struggling Students": "red"}

plt.figure(figsize=(8, 5))
for group, grp_df in df.groupby("Performance Group"):
    plt.scatter(grp_df["FinalResult"], grp_df["absences"],
                label=group, color=colors[group], alpha=0.6, edgecolors="k", linewidths=0.3)
plt.title("Student Clusters: Final Result vs Absences")
plt.xlabel("Final Result")
plt.ylabel("Absences (100 - Attendance)")
plt.legend()
plt.tight_layout()
plt.show()

# ── Visualisation 2: Study Hours vs Final Result ──────────────────────────────
plt.figure(figsize=(8, 5))
for group, grp_df in df.groupby("Performance Group"):
    plt.scatter(grp_df["StudyHours"], grp_df["FinalResult"],
                label=group, color=colors[group], alpha=0.6, edgecolors="k", linewidths=0.3)
plt.title("Student Clusters: Study Hours vs Final Result")
plt.xlabel("Study Hours")
plt.ylabel("Final Result")
plt.legend()
plt.tight_layout()
plt.show()

# ── Visualisation 3: Assignments Completed vs Final Result ────────────────────
plt.figure(figsize=(8, 5))
for group, grp_df in df.groupby("Performance Group"):
    plt.scatter(grp_df["AssignmentsCompleted"], grp_df["FinalResult"],
                label=group, color=colors[group], alpha=0.6, edgecolors="k", linewidths=0.3)
plt.title("Student Clusters: Assignments Completed vs Final Result")
plt.xlabel("Assignments Completed")
plt.ylabel("Final Result")
plt.legend()
plt.tight_layout()
plt.show()

print("\nClustering complete. Students have been grouped into:")
for group in ["Top Performers", "Average Students", "Struggling Students"]:
    count = (df["Performance Group"] == group).sum()
    print(f"  {group}: {count} students")
