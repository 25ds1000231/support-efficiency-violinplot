import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ---------------------------------------------------------
# Business Context:
# A major retail client engaged Bosco Fay and Mohr to analyze
# the distribution of customer support response times across
# support channels. This visualization is designed for
# executive-level presentations and board reports.
# ---------------------------------------------------------

# ------------------------------------
# Generate synthetic data
# ------------------------------------
np.random.seed(42)

channels = ["Email", "Chat", "Phone", "Social Media"]

# Synthetic response-time distributions (in minutes)
# Modeled to mimic real-world support operations
data = {
    "Channel": np.repeat(channels, 250),
    "ResponseTime": np.concatenate([
        np.random.normal(loc=45, scale=12, size=250),   # Email: slower, higher variance
        np.random.normal(loc=12, scale=4, size=250),    # Chat: faster, low variance
        np.random.normal(loc=20, scale=6, size=250),    # Phone: moderate
        np.random.normal(loc=30, scale=10, size=250)    # Social Media: variable
    ])
}

df = pd.DataFrame(data)

# Ensure no negative response times
df["ResponseTime"] = df["ResponseTime"].clip(lower=0)

# ------------------------------------
# Create the figure (512x512 px)
# ------------------------------------
plt.figure(figsize=(8, 8))  # 8x8 inches at 64 DPI → 512x512 px

sns.set_theme(style="whitegrid")

# ------------------------------------
# Create Violin Plot
# ------------------------------------
sns.violinplot(
    data=df,
    x="Channel",
    y="ResponseTime",
    palette="Set2",
    cut=0,
    bw=0.3,
    linewidth=1.2
)

# ------------------------------------
# Style the chart with executive-level polish
# ------------------------------------
plt.title(
    "Distribution of Customer Support Response Times Across Channels\n"
    "Prepared for Bosco Fay and Mohr – Retail Client Quarterly Business Review",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Support Channel", fontsize=12)
plt.ylabel("Response Time (minutes)", fontsize=12)

# Add subtle gridlines for clarity
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Add annotation for business relevance
plt.text(
    0.5, -0.25,
    "This visualization highlights channel-specific response time patterns to support strategic\n"
    "recommendations for efficiency improvements ahead of the client's quarterly business review.",
    fontsize=10,
    ha="center",
    transform=plt.gca().transAxes
)

plt.tight_layout()

# ------------------------------------
# Save output
# ------------------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()

print("Chart saved as chart.png")
