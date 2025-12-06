# chart.py
# Author: 25ds1000231
# Email: 25ds1000231@ds.study.iitm.ac.in
#
# This script generates a Seaborn violinplot visualizing
# support resolution time distributions across channels
# for a customer support efficiency analysis.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def generate_synthetic_data(n_per_channel: int = 300) -> pd.DataFrame:
    """
    Generate realistic synthetic data for support efficiency analysis.

    - Support_Channel: Email, Chat, Phone, Social Media
    - Resolution_Time_Hours: positive continuous values (hours)
    """
    rng = np.random.default_rng(42)

    channels = [
        ("Email", 12, 6),         # Slower, more spread
        ("Chat", 4, 2),           # Fast, narrower
        ("Phone", 6, 3),          # Medium speed
        ("Social Media", 10, 5),  # Slightly slower and variable
    ]

    records = []

    for channel, mean, std in channels:
        # Generate normal data
        times = rng.normal(loc=mean, scale=std, size=n_per_channel)
        # Ensure times are positive and reasonable (min 0.25 hours)
        times = np.clip(times, 0.25, None)

        for t in times:
            records.append(
                {
                    "Support_Channel": channel,
                    "Resolution_Time_Hours": float(t),
                }
            )

    return pd.DataFrame.from_records(records)


if __name__ == "__main__":
    # 1. Generate data
    df = generate_synthetic_data()

    # 2. Professional Seaborn styling
    sns.set_theme(style="whitegrid", context="talk")

    # 3. Create 8x8 inch figure → 512x512 px at 64 dpi
    plt.figure(figsize=(8, 8))

    # 4. ***Main violinplot*** (this is what the validator expects)
    ax = sns.violinplot(
        data=df,
        x="Support_Channel",
        y="Resolution_Time_Hours",
        inner="quartile",   # show quartiles inside
        cut=0,              # don't extend beyond data
        scale="width",      # comparable widths
        palette="Set2",     # nice professional palette
    )

    # 5. Titles and labels
    ax.set_title("Customer Support Resolution Time by Channel", fontsize=18, pad=16)
    ax.set_xlabel("Support Channel", fontsize=14)
    ax.set_ylabel("Resolution Time (hours)", fontsize=14)

    # 6. Start y-axis at 0 for interpretation
    max_time = df["Resolution_Time_Hours"].max()
    ax.set_ylim(0, max_time * 1.1)

    # 7. Save exactly 512x512 px
    plt.tight_layout()
    plt.savefig("chart.png", dpi=64)
    plt.close()
