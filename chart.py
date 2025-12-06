import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ---------------------------------------------------------
# Business Context:
# A major retail client has engaged Bosco Fay and Mohr to
# analyze and visualize customer support response times
# across support channels. This violin plot will be used in
# executive presentations, board reports, and strategic
# planning documents for the upcoming Quarterly Review.
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
# Apply Seaborn Best Practices
# ------------------------------------
sns.set_style("whitegrid")    # Clean, professional
sns.set_context("talk")       # Presentation-ready text sizes

# ------------------------------------
# Create the figure (EXACT 512x512 px)
# ------------------------------------
# 8 inches * 64 dpi = 512 px
fig = plt.figure(figsize=(8, 8), dpi=64)

# ------------------------------------
# Violin Plot
# ------------------------------------
sns.violinplot(
    data=df,
    x="Channel",
    y="ResponseTime",
    palette="Set2",    # Colorblind-friendly, professional
    cut=0,
    bw=0.3,
    linewidth=1.2
)

# ------------------------------------
# Executive-Level Styling
# ------------------------------------
plt.title(
    "Customer Support Response Time Distribution by Channel\n"
    "Prepared for Bosco Fay and Mohr – Retail Client Quarterly Review",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel("Support Channel", fontsize=14)
plt.ylabel("Response Time (minutes)", fontsize=14)

# Subtle y-grid lines
plt.grid(axis="y", linestyle="--", alpha=0.6)

# Business annotation
plt.text(
    0.5, -0.22,
    "This visualization supports strategic decision-making and highlights\n"
    "channel-specific response time patterns for the upcoming Quarterly Review.",
    fontsize=12,
    ha="center",
    transform=plt.gca().transAxes
)

# IMPORTANT:
# - Do NOT use tight_layout()
# - Do NOT use bbox_inches='tight'
# Both will shrink the pixel size below 512×512.

# ------------------------------------
# Save the chart (EXACT 512x512 px)
# ------------------------------------
fig.savefig("chart.png", dpi=64)

plt.close()

print("Chart saved as chart.png (512 x 512 px)")
