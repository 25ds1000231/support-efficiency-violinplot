# chart.py
# Email: 25ds1000231@ds.study.iitm.ac.in
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

def main():
    np.random.seed(42)
    df = pd.DataFrame({
        "Tier": np.random.choice(["Tier 1", "Tier 2", "Tier 3"], 500),
        "Resolution_Time": np.random.lognormal(mean=1.5, sigma=0.5, size=500)
    })
    
    sns.set_style("whitegrid")
    sns.set_context("talk")
    
    # Create figure with specific size to get close to 512x512
    fig, ax = plt.subplots(figsize=(6, 6), dpi=100)
    
    sns.violinplot(
        data=df,
        x="Tier",
        y="Resolution_Time",
        palette="Set2",
        inner="quartile",
        cut=0,
        ax=ax
    )
    
    ax.set_title("Support Resolution Time by Tier")
    ax.set_xlabel("Support Tier")
    ax.set_ylabel("Resolution Time (hours)")
    
    # Tight layout to remove extra whitespace
    plt.tight_layout()
    
    # Save to a temporary buffer first
    fig.canvas.draw()
    
    # Convert to a Pillow image
    img = Image.frombytes(
        "RGB",
        fig.canvas.get_width_height(),
        fig.canvas.tostring_rgb()
    )
    plt.close(fig)
    
    # Resize to EXACTLY 512x512 using LANCZOS (or Resampling.LANCZOS for newer Pillow)
    try:
        # For newer Pillow versions (>=10.0.0)
        img = img.resize((512, 512), Image.Resampling.LANCZOS)
    except AttributeError:
        # For older Pillow versions
        img = img.resize((512, 512), Image.LANCZOS)
    
    img.save("chart.png")
    print("Chart saved successfully as chart.png (512x512 pixels)")

if __name__ == "__main__":
    main()
