# chart.py
# Author: 25ds1000231
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
    - Channel: Email / Chat / Phone
    - Resolution_Time_Hours: continuous time-to-resolution

    Business logic:
    - Tier 1 usually resolves faster than Tier 2, which is faster than Tier 3.
    - Email tends to be slower than Chat, Phone is in-between.
    """
    rng = np.random.default_rng(42)

    tiers = rng.choice(
        ["Tier 1 - Frontline", "Tier 2 - Specialist", "Tier 3 - Escalation"],
        size=n_samples,
        p=[0.5, 0.3, 0.2],
    )

    channels = rng.choice(
        ["Email", "Chat", "Phone"],
        size=n_samples,
        p=[0.4, 0.35, 0.25],
    )

    # Base typical resolution times (in hours) by tier
    base_by_tier = {
        "Tier 1 - Frontline": 2.0,
        "Tier 2 - Specialist": 5.0,
        "Tier 3 - Escalation": 12.0,
    }

    # Channel adjustments (email slightly slower, chat slightly faster)
    channel_adjust = {
        "Email": 1.5,
        "Chat": -0.5,
        "Phone": 0.0,
    }

    resolution_times = []
    for tier, channel in zip(tiers, channels):
        mu = base_by_tier[tier] + channel_adjust[channel]
        # Log-normal to simulate positive skew (some very long resolutions)
        val = rng.lognormal(mean=np.log(mu), sigma=0.45)
        resolution_times.append(val)

    df = pd.DataFrame(
        {
            "Support_Tier": tiers,
            "Channel": channels,
            "Resolution_Time_Hours": resolution_times,
        }
    )

    return df


def create_violinplot(df: pd.DataFrame, output_path: str = "chart.png") -> None:
    """
    Create a violinplot using Seaborn to visualize the distribution of
    resolution times by support tier and channel.

    Requirements:
    - Use sns.violinplot()
    - Professional styling and labels
    - 512x512 pixels output (8x8 inches at 64 dpi)
    """

    # Professional Seaborn styling
    sns.set_style("whitegrid")
    sns.set_context("talk")  # slightly larger fonts, presentation-friendly

    # 8x8 inches with 64 DPI => 512x512 pixels
    plt.figure(figsize=(8, 8))

    ax = sns.violinplot(
        data=df,
        x="Support_Tier",
        y="Resolution_Time_Hours",
        hue="Channel",
        palette="Set2",
        inner="quartile",   # show quartiles inside the violin
        cut=0,              # don't extend beyond data range
        linewidth=1,
    )

    ax.set_title(
        "Support Resolution Time by Tier and Channel",
        fontsize=16,
        pad=18,
    )
    ax.set_xlabel("Support Tier", fontsize=14)
    ax.set_ylabel("Resolution Time (hours)", fontsize=14)

    # Rotate x labels for readability
    plt.xticks(rotation=15)

    # Legend outside the plot for clarity
    plt.legend(
        title="Channel",
        loc="upper left",
        bbox_to_anchor=(1.02, 1.0),
        borderaxespad=0.0,
    )

    plt.tight_layout()

    # 8 in * 64 dpi = 512 pixels; bbox_inches="tight" keeps layout tidy
    plt.savefig(output_path, dpi=64, bbox_inches="tight")
    plt.close()


def main() -> None:
    # 1. Generate synthetic business data
    df = generate_synthetic_data(n_samples=500)

    # 2. Create violinplot and export as PNG
    create_violinplot(df, output_path="chart.png")


if __name__ == "__main__":
    main()
