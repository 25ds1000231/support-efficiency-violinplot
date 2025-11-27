# chart.py
# Email: 25ds1000231@ds.study.iitm.ac.in

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image  # for precise 512x512 resizing
import os


def generate_data(n=500) -> pd.DataFrame:
    """Generate synthetic support efficiency data."""
    np.random.seed(42)

    tiers = np.random.choice(["Tier 1", "Tier 2", "Tier 3"], size=n, p=[0.5, 0.3, 0.2])
    resolution_time = np.random.lognormal(mean=1.5, sigma=0.5, size=n)

    return pd.DataFrame(
        {
            "Support_Tier": tiers,
            "Resolution_Time_Hours": resolution_time,
        }
    )


def make_violinplot(df: pd.DataFrame, raw_path: str = "chart_raw.png") -> None:
    """Create a Seaborn violinplot and save a raw PNG (any size)."""

    sns.set_style("whitegrid")
    sns.set_context("talk")

    # Reasonable size; we will resize later anyway
    plt.figure(figsize=(8, 8))

    sns.violinplot(
        data=df,
        x="Support_Tier",
        y="Resolution_Time_Hours",
        palette="Set2",
        inner="quartile",
        cut=0,
    )

    plt.title("Support Resolution Time Distribution by Tier")
    plt.xlabel("Support Tier")
    plt.ylabel("Resolution Time (hours)")
    plt.xticks(rotation=15)

    # Save initial image (size may NOT be 512x512 yet)
    plt.savefig(raw_path, dpi=100)
    plt.close()


def force_512_png(raw_path: str = "chart_raw.png", final_path: str = "chart.png") -> None:
    """Resize the raw plot to exactly 512x512 pixels."""

    img = Image.open(raw_path)
    img = img.resize((512, 512), Image.LANCZOS)
    img.save(final_path, format="PNG")

    # Optional: clean up the raw file
    try:
        os.remove(raw_path)
    except OSError:
        pass


def main() -> None:
    df = generate_data()
    make_violinplot(df)
    force_512_png()


if __name__ == "__main__":
    main()
