import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Generate synthetic data
np.random.seed(0)  # for reproducibility
data = np.random.rand(200, 4) * 100  # Generate values between 0 and 100
target = np.random.randint(0, 2, size=200)  # Binary target (0 or 1)

# 2. Load into DataFrame
column_names = ["feat1", "feat2", "feat3", "feat4"]
df = pd.DataFrame(data, columns=column_names)
df["target"] = target

# 3. Normalize each feature column to [0, 1]
df_norm = df.copy()
for col in column_names:
    min_val = df[col].min()
    max_val = df[col].max()
    df_norm[col] = (df[col] - min_val) / (max_val - min_val)

# 4. Encode labels into 'label_encoded' column (0 → 0, 1 → 1)
df_norm["label_encoded"] = df_norm["target"]  # Already 0 and 1, but clearly mapped here

# 5a. Histogram of one normalized feature (feat1)
plt.figure(figsize=(8, 5))
sns.histplot(df_norm["feat1"], bins=20, kde=True, color='skyblue')
plt.title("Histogram of Normalized Feature: feat1")
plt.xlabel("Normalized feat1")
plt.ylabel("Frequency")

# 5b. Scatter plot of two features colored by label_encoded
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df_norm, x="feat2", y="feat3", hue="label_encoded", palette="Set1")
plt.title("Scatter Plot of feat2 vs feat3")
plt.xlabel("Normalized feat2")
plt.ylabel("Normalized feat3")
plt.legend(title="Label Encoded")

# 5c. Box plot comparing feat4 distribution across label_encoded
plt.figure(figsize=(8, 5))
sns.boxplot(x="label_encoded", y="feat4", data=df_norm, palette="Set2")
plt.title("Box Plot of feat4 by Label Encoded")
plt.xlabel("Label Encoded")
plt.ylabel("Normalized feat4")

# Display all plots
plt.tight_layout()
plt.show()
