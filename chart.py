# chart.py
# Email: 25ds1000231@ds.study.iitm.ac.in
#
# This script generates a Seaborn violinplot showing
# support resolution time distribution by support tier.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image


def generate_data(n_samples=500):
    """Generate synthetic support efficiency data."""
    np.random.seed(42)

    tiers = np.random.choice(
        ["Tier 1", "Tier 2", "Tier 3"],
        size=n_samples,
        p=[0.5, 0.3, 0.2],
    )

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


def create_violinplot(df):
    """Create a Seaborn violinplot and save chart.png as 512x512."""

    # Professional Seaborn styling
    sns.set_style("whitegrid")
    sns.set_context("talk")

    # Figure size can be anything; we'll resize later
    plt.figure(figsize=(6, 6))

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

    # Save a temporary image first
    temp_file = "chart_temp.png"
    plt.savefig(temp_file, dpi=100)
    plt.close()

    # Force final PNG to be exactly 512x512
    img = Image.open(temp_file)
    img = img.resize((512, 512), Image.LANCZOS)
    img.save("chart.png")


def main():
    df = generate_data()
    create_violinplot(df)
    print("Generated chart.png (512x512)")


if __name__ == "__main__":
    main()
