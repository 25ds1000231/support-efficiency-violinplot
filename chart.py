import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so

# ---------------------------------------------------------
# Business Context:
# Executive-ready visualization for Bosco Fay and Mohr's
# retail client, needed for QBR and board presentations.
# ---------------------------------------------------------

np.random.seed(42)

channels = ["Email", "Chat", "Phone", "Social Media"]

data = {
    "Channel": np.repeat(channels, 250),
    "ResponseTime": np.concatenate([
        np.random.normal(loc=45, scale=12, size=250),
        np.random.normal(loc=12, scale=4,  size=250),
        np.random.normal(loc=20, scale=6,  size=250),
        np.random.normal(loc=30, scale=10, size=250)
    ])
}

df = pd.DataFrame(data)
df["ResponseTime"] = df["ResponseTime"].clip(lower=0)

sns.set_style("whitegrid")
sns.set_context("talk")

# EXACT 512x512 px setup
fig = plt.figure(figsize=(8, 8), dpi=64)

sns.violinplot(
    data=df,
    x="Channel",
    y="ResponseTime",
    palette="Set2",
    cut=0,
    bw=0.3,
    linewidth=1.2,
)

plt.title(
    "Customer Support Response Time Distribution by Channel\n"
    "Prepared for Bosco Fay and Mohr – Retail Client Quarterly Review",
    fontsize=18,
    fontweight="bold"
)
plt.xlabel("Support Channel", fontsize=14)
plt.ylabel("Response Time (minutes)", fontsize=14)

plt.grid(axis="y", linestyle="--", alpha=0.6)

# FIX: Keep annotation **INSIDE** the axes
plt.text(
    0.5, 0.02,
    "Insight: Distribution patterns guide support-efficiency strategy.",
    fontsize=12,
    ha="center",
    transform=plt.gca().transAxes
)

# Do NOT use tight_layout()
# Do NOT use bbox_inches='tight'

fig.savefig("chart.png", dpi=64)

plt.close()
print("Chart saved as chart.png (exact 512 x 512 px)")
