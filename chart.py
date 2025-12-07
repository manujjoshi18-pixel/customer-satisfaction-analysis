import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate realistic customer satisfaction score dataset
np.random.seed(42)

categories = ['Electronics', 'Home Furnishing', 'Grocery', 'Apparel', 'Sports']

# Generate scores per category individually
means = [4.2, 4.0, 4.6, 3.9, 4.3]

scores = []
for mean in means:
    scores.append(np.random.normal(loc=mean, scale=0.25, size=30))

# Convert to mean score per category
avg_scores = [np.mean(s) for s in scores]

df = pd.DataFrame({
    'Product Category': categories,
    'Average Satisfaction': avg_scores
})

# Apply professional seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk")

plt.figure(figsize=(8, 8))  # 8 inches × 64 dpi = 512px

sns.barplot(
    data=df,
    x='Product Category',
    y='Average Satisfaction',
    palette='viridis'
)

plt.title("Average Customer Satisfaction by Product Category", fontsize=16)
plt.xlabel("Product Category")
plt.ylabel("Avg Satisfaction Score")

# Save figure with exact resolution
plt.savefig('chart.png', dpi=64, bbox_inches='tight')

plt.show()
