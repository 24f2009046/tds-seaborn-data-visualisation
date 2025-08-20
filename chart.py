import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style and context for professional look
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate realistic synthetic data: customer engagement metrics
# For example, 5 customers over 7 days with engagement scores
np.random.seed(42)
data = pd.DataFrame(
    np.random.poisson(lam=5, size=(5, 7)),
    index=["Customer A", "Customer B", "Customer C", "Customer D", "Customer E"],
    columns=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
)

# Create matplotlib figure with 8x8 inches size which equals 512x512 pixels at 64 dpi
plt.figure(figsize=(8, 8))

# Create heatmap with annotations, colorbar, and a custom colormap
heatmap = sns.heatmap(
    data,
    annot=True,
    fmt="d",
    cmap="YlGnBu",
    linewidths=0.5,
    linecolor="gray",
    cbar_kws={"shrink": 0.8},
    square=True
)

# Set plot titles and labels
plt.title("Customer Engagement Heatmap (Weekly)", fontsize=18, pad=20)
plt.xlabel("Day of Week", fontsize=14)
plt.ylabel("Customer", fontsize=14)

# Adjust layout to ensure nothing is cut off
plt.subplots_adjust(left=0.15, right=0.85, top=0.85, bottom=0.15)

# Save figure as PNG, exactly 512x512 pixels, without bbox_inches='tight'
plt.savefig("chart.png", dpi=64)
plt.close()

print("Heatmap saved as chart.png")
