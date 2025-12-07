import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so

# ------------------------------
# Data Generation (Realistic)
# ------------------------------

np.random.seed(42)

channels = ["Email", "Chat", "Phone", "Social Media"]

# Email – long-tail lognormal, occasional slow responses
email_times = np.random.lognormal(mean=np.log(35), sigma=0.4, size=250)

# Chat – fast, low variance, gamma distribution
chat_times = np.random.gamma(shape=4, scale=3, size=250)

# Phone – moderate skew, slight tail
phone_times = np.random.normal(loc=22, scale=6, size=250)
phone_times += np.abs(np.random.normal(0, 4, size=250)) * 0.3

# Social Media – bimodal (auto reply + human follow-up)
fast_auto = np.random.normal(loc=10, scale=3, size=150)
slow_human = np.random.normal(loc=45, scale=12, size=100)
social_times = np.concatenate([fast_auto, slow_human])

data = {
    "Channel": np.repeat(channels, 250),
    "ResponseTime": np.concatenate([
        email_times,
        chat_times,
        phone_times,
        social_times
    ])
}

df = pd.DataFrame(data)
df["ResponseTime"] = df["ResponseTime"].clip(lower=0)

# ------------------------------
# Seaborn Styling
# ------------------------------

sns.set_style("whitegrid")        # Professional background
sns.set_context("talk")           # Presentation-ready text

# ------------------------------
# Figure Setup (512 × 512 px)
# ------------------------------

fig = plt.figure(figsize=(8, 8))  # 8 in * 64 dpi = 512 px
plt.rcParams['savefig.dpi'] = 64  # Ensures 512×512 output

# ------------------------------
# Violin Plot
# ------------------------------

sns.violinplot(
    data=df,
    x="Channel",
    y="ResponseTime",
    palette="Set2",
    cut=0,
    bw=0.25,
    linewidth=1.2,
)

plt.title("Customer Support Response Time Distribution by Channel",
          fontsize=18, fontweight="bold")
plt.xlabel("Support Channel", fontsize=14)
plt.ylabel("Response Time (minutes)", fontsize=14)

plt.grid(axis="y", linestyle="--", alpha=0.6)

# ------------------------------
# Save EXACT 512×512 (with tight bounding box)
# ------------------------------

plt.savefig("chart.png", dpi=64, bbox_inches='tight')
plt.close()

print("Chart saved as chart.png (exact 512x512, seaborn violinplot)")

