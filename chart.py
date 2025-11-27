# chart.py
# Email: 25ds1000231@ds.study.iitm.ac.in

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def generate_synthetic_data(n_samples=500):
    np.random.seed(42)

    tiers = np.random.choice(
        ["Tier 1 - Frontline", "Tier 2 - Specialist", "Tier 3 - Escalation"],
        size=n_samples,
        p=[0.5, 0.3, 0.2]
    )

    channels = np.random.choice(
        ["Email", "Chat", "Phone"],
        size=n_samples,
        p=[0.4, 0.35, 0.25]
    )

    base_times = {
        "Tier 1 - Frontline": 2.0,
        "Tier 2 - Specialist": 5.0,
        "Tier 3 - Escalation": 12.0,
    }

    channel_adjust = {"Email": 1.5, "Chat": -0.5, "Phone": 0.0}

    resolution_times = []
    for t, c in zip(tiers, channels):
        mu = base_times[t] + channel_adjust[c]
        val = np.random.lognormal(mean=np.log(mu), sigma=0.45)
        resolution_times.append(val)

    return pd.DataFrame({
        "Support_Tier": tiers,
        "Channel": channels,
        "Resolution_Time_Hours": resolution_times,
    })


def create_violinplot(df):
    sns.set_style("whitegrid")
    sns.set_context("talk")

    # 8"x8" @ 64 DPI => 512x512 pixels
    plt.figure(figsize=(8, 8))

    ax = sns.violinplot(
        data=df,
        x="Support_Tier",
        y="Resolution_Time_Hours",
        hue="Channel",
        palette="Set2",
        inner="quartile",
        cut=0,
        linewidth=1,
    )

    ax.set_title("Support Resolution Time by Tier and Channel", pad=15)
    ax.set_xlabel("Support Tier")
    ax.set_ylabel("Resolution Time (hours)")

    plt.xticks(rotation=15)

    # Legend inside the axes so the layout doesn't shrink
    plt.legend(title="Channel", loc="upper right")

    # Very important: NO bbox_inches='tight'
    plt.savefig("chart.png", dpi=64)

    plt.close()


if __name__ == "__main__":
    df = generate_synthetic_data()
    create_violinplot(df)
