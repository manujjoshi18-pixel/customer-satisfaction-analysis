import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate realistic customer satisfaction score dataset
np.random.seed(42)

categories = ['Electronics', 'Home Furnishing', 'Grocery', 'Apparel', 'Sports']
means = [4.2, 4.0, 4.6, 3.9, 4.3]

scores = []
for mean in means:
    scores.append(np.random.normal(loc=mean, scale=0.25, size=30))

avg_scores = [np.mean(s) for s in scores]

df = pd.DataFrame({
    'Product Category': categories,
    'Average Satisfaction': avg_scores
})

# Styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Create figure
fig = plt.figure(figsize=(8, 8), dpi=64)
ax = fig.add_subplot(111)

sns.barplot(
    data=df,
    x='Product Category',
    y='Average Satisfaction',
    palette='viridis',
    ax=ax
)

ax.set_title("Average Customer Satisfaction by Product Category")
ax.set_xlabel("Product Category")
ax.set_ylabel("Avg Satisfaction Score")

# Force exact 512x512 output
fig.set_size_inches(8, 8)
fig.savefig("chart.png", dpi=64, bbox_inches=None)

plt.show()
