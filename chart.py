# chart_imageio.py
# Email: 25ds1000231@ds.study.iitm.ac.in
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import imageio.v3 as iio
from PIL import Image

def main():
    np.random.seed(42)
    df = pd.DataFrame({
        "Tier": np.random.choice(["Tier 1", "Tier 2", "Tier 3"], 500),
        "Resolution_Time": np.random.lognormal(mean=1.5, sigma=0.5, size=500)
    })
    
    sns.set_style("whitegrid")
    sns.set_context("talk")
    
    fig, ax = plt.subplots(figsize=(8, 8))
    
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
    plt.tight_layout()
    
    # Save using matplotlib first
    plt.savefig("temp.png", dpi=100, bbox_inches='tight')
    plt.close()
    
    # Read with imageio
    img_array = iio.imread("temp.png")
    
    # Resize using PIL
    img = Image.fromarray(img_array)
    img = img.resize((512, 512), Image.Resampling.LANCZOS if hasattr(Image.Resampling, 'LANCZOS') else 1)
    
    # Convert back to array and save with imageio
    img_array_resized = np.array(img)
    iio.imwrite("chart.png", img_array_resized)
    
    # Verify
    import os
    os.remove("temp.png")
    
    final = Image.open("chart.png")
    print(f"Final size: {final.size}")
    final.close()

if __name__ == "__main__":
    main()
