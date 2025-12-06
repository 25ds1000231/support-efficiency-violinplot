import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ---------------------------------------------------------
# Business Context:
# A major retail client has engaged Bosco Fay and Mohr to 
# visualize the distribution and density of customer support 
# response times across different channels. This plot will 
# be used in executive presentations and board-level reports.
# ---------------------------------------------------------

# ------------------------------------
# Generate synthetic data
# ------------------------------------
np.random.seed(42)

channels = ["Email", "Chat", "Phone", "Social Media"]

# Realistic synthetic response-time distributions (in minutes)
data = {
    "Channel": np.repeat(channels, 250),
    "ResponseTime": np.concatenate([
        np.random.normal(loc=45, scale=12, size=250),  # Email
        np.random.normal(loc=12, scale=4,  size=250),  # Chat
        np.random.normal(loc=20, scale=6,  size=250),  # Phone
        np.random.normal(loc=30, scale=10, size=250)   # Social Media
    ])
}

df = pd.DataFrame(data)
df["ResponseTime"] = df["ResponseTime"].clip(lower=0)

# ------------------------------------
# Apply Seaborn best practices
# ------------------------------------
sns.set_style("whitegrid")       # Professional appearance
sns.set_context("talk")          # Presentation-ready font sizes

# ------------------------------------
# Create the figure (512x512 px)
# ------------------------------------
plt.figure(figsize=(8, 8))       # 8 in × 8 in → 512 px × 512 px at 64 DPI

# ------------------------------------
# Create Violin Plot
# ------------------------------------
sns.violinplot(
    data=df,
    x="Channel",
    y="ResponseTime",
    palette="Set2",   # Professional, colorblind-friendly palette
    cut=0,
    bw=0.3,
    linewidth=1.2
)

# ------------------------------------
# Style the chart for executive use
# ------------------------------------
plt.title(
    "Customer Support Response Time Distribution by Channel\n"
    "Prepared for Bosco Fay and Mohr – Retail Client Quarterly Review",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel("Support Channel", fontsize=14)
plt.ylabel("Response Time (minutes)", fontsize=14)

plt.grid(axis='y', linestyle='--', alpha=0.6)

# Business-context annotation
plt.text(
    0.5, -0.25,
    "Visualizing channel-level response time patterns to guide strategic\n"
    "recommendations for support efficiency improvements.",
    fontsize=12,
    ha="center",
    transform=plt.gca().transAxes
)

plt.tight_layout()

# ------------------------------------
# Save the chart
# ------------------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()

print("Chart saved as chart.png")
