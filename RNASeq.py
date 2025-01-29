import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

# Load the dataset
file_path = "GSE71585_RefSeq_RPKM.csv.gz"
df = pd.read_csv(file_path, compression="gzip")

# Set the gene column as the index
df.set_index(df.columns[0], inplace=True)

# Convert to numeric values (in case of any string formatting issues)
df = df.apply(pd.to_numeric, errors='coerce')

# Summary statistics
print("Dataset Shape:", df.shape)
print("Summary Statistics:\n", df.describe())

# Plot histogram of expression values
plt.figure(figsize=(10, 5))
sns.histplot(df.values.flatten(), bins=100, kde=True)
plt.yscale("log")
plt.xlabel("Expression Level (RPKM)")
plt.ylabel("Frequency (log scale)")
plt.title("Distribution of Gene Expression Levels")
plt.show()

# Heatmap of the top 50 most variable genes
top_genes = df.var(axis=1).nlargest(50).index
plt.figure(figsize=(12, 8))
sns.heatmap(df.loc[top_genes], cmap="viridis", xticklabels=False)
plt.title("Heatmap of Top 50 Most Variable Genes")
plt.show()

# PCA analysis
pca = PCA(n_components=2)
pca_result = pca.fit_transform(df.T)  # Transpose to analyze samples

plt.figure(figsize=(8, 6))
sns.scatterplot(x=pca_result[:, 0], y=pca_result[:, 1])
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA of Gene Expression Data")
plt.show()
