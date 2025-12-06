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

    # Support tier distribution
    tiers = np.random.choice(
        ["Tier 1", "Tier 2", "Tier 3"],
        size=n_samples,
        p=[0.5, 0.3, 0.2],
    )

    # Skewed resolution times (log-normal)
    # Tier 1 fastest, Tier 3 slowest
    tier_to_mean = {"Tier 1": 1.3, "Tier 2": 1.5, "Tier 3": 1.7}
    means = np.array([tier_to_mean[t] for t in tiers])

    resolution_time = np.random.lognormal(
        mean=means,
        sigma=0.4,
    )

    df = pd.DataFrame(
        {
            "Support_Tier": tiers,
            "Resolution_Time_Hours": resolution_time,
        }
    )
    return df


def create_violinplot(df: pd.DataFrame) -> None:
    """Create a Seaborn violinplot and save chart.png as 512x512."""

    # Simple, standard seaborn theme
    sns.set_theme(style="whitegrid")

    # 8x8 inches at 64 dpi -> 512 x 512 pixels
    plt.figure(figsize=(8, 8))

    sns.violinplot(
        data=df,
        x="Support_Tier",
        y="Resolution_Time_Hours",
    )

    plt.title("Support Resolution Time by Tier")
    plt.xlabel("Support Tier")
    plt.ylabel("Resolution Time (hours)")

    # EXACT save line per guidelines
    plt.savefig("chart.png", dpi=64, bbox_inches="tight")
    plt.close()


def main() -> None:
    df = generate_data()
    create_violinplot(df)
    print("Generated chart.png (512x512 using 8x8 @ 64 dpi)")


if __name__ == "__main__":
    main()
