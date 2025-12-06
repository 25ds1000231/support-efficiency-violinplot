# chart.py
# Email: 25ds1000231@ds.study.iitm.ac.in
#
# This script generates a Seaborn violinplot visualizing
# support resolution time distributions across tiers and channels
# for a customer support efficiency analysis.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def generate_synthetic_data(n_samples: int = 500) -> pd.DataFrame:
    """
    Generate realistic synthetic data for support efficiency analysis.

    - Support_Tier: Tier 1 / Tier 2 / Tier 3
    - Support_Channel: Phone / Email / Chat
    - Resolution_Time_Hours: continuous, skewed (log-normal) with
      different typical times per tier & channel.
    """
    np.random.seed(42)

    tiers = np.random.choice(
        ["Tier 1", "Tier 2", "Tier 3"],
        size=n_samples,
        p=[0.5, 0.3, 0.2],
    )

    channels = np.random.choice(
        ["Phone", "Email", "Chat"],
        size=n_samples,
        p=[0.4, 0.35, 0.25],
    )

    # Base log-mean times by tier (Tier 1 fastest, Tier 3 slowest)
    tier_to_mean = {"Tier 1": 1.3, "Tier 2": 1.5, "Tier 3": 1.7}
    channel_to_adjust = {"Phone": 0.0, "Email": 0.1, "Chat": -0.05}

    means = [
        tier_to_mean[t] + channel_to_adjust[c]
        for t, c in zip(tiers, channels)
    ]

    # Generate lognormal resolution times in hours
    resolution_times = np.random.lognormal(
        mean=np.array(means),
        sigma=0.4,
    )

    df = pd.DataFrame(
        {
            "Support_Tier": tiers,
            "Support_Channel": channels,
            "Resolution_Time_Hours": resolution_times,
        }
    )
    return df


def create_violinplot(df: pd.DataFrame) -> None:
    """
    Create a Seaborn violinplot and save chart.png as 512x512
    (8x8 inches at 64 DPI).
    """

    # Professional Seaborn styling
    sns.set_theme(style="whitegrid", context="talk")

    # 8x8 inches @ 64 dpi -> 512x512 pixels
    plt.figure(figsize=(8, 8))

    sns.violinplot(
        data=df,
        x="Support_Tier",
        y="Resolution_Time_Hours",
        hue="Support_Channel",
        split=True,
        inner="quartile",
    )

    plt.title("Support Resolution Time by Tier and Channel")
    plt.xlabel("Support Tier")
    plt.ylabel("Resolution Time (hours)")

    # Move legend outside if needed (not required, but neat)
    plt.legend(title="Channel", loc="upper right")

    # Save exactly as per the guidelines
    plt.savefig("chart.png", dpi=64, bbox_inches="tight")
    plt.close()


def main() -> None:
    df = generate_synthetic_data()
    create_violinplot(df)
    print("Generated chart.png (512x512 using 8x8 @ 64 dpi)")


if __name__ == "__main__":
    main()
