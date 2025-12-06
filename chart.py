# chart.py
# Email: 25ds1000231@ds.study.iitm.ac.in
#
# This script generates a Seaborn violinplot showing
# support resolution time distribution by support tier.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def generate_data(n_samples: int = 500) -> pd.DataFrame:
    """Generate synthetic support efficiency data."""
    np.random.seed(42)

    # Simulate support tiers with realistic proportions
    tiers = np.random.choice(
        ["Tier 1", "Tier 2", "Tier 3"],
        size=n_samples,
        p=[0.5, 0.3, 0.2],
    )

    # Lognormal distribution to mimic skewed resolution times
    resolution_time = np.random.lognormal(
        mean=1.5,  # center
        sigma=0.5,  # spread
        size=n_samples,
    )

    df = pd.DataFrame(
        {
            "Tier": tiers,
            "Resolution_Time": resolution_time,
        }
    )
    return df


def create_violinplot(df: pd.DataFrame) -> None:
    """Create a Seaborn violinplot and save chart.png as 512x512."""

    # Professional Seaborn styling
    sns.set_style("whitegrid")
    sns.set_context("talk")

    # 8x8 inches with dpi=64 -> 512x512 pixels
    plt.figure(figsize=(8, 8))

    sns.violinplot(
        data=df,
        x="Tier",
        y="Resolution_Time",
        palette="Set2",
        inner="quartile",
        cut=0,
    )

    plt.title("Support Resolution Time by Tier")
    plt.xlabel("Support Tier")
    plt.ylabel("Resolution Time (hours)")

    # Save directly as required by the guidelines
    plt.savefig("chart.png", dpi=64, bbox_inches="tight")
    plt.close()


def main() -> None:
    df = generate_data()
    create_violinplot(df)
    print("Generated chart.png (512x512 using 8x8 @ 64 dpi)")


if __name__ == "__main__":
    main()
