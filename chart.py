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
    
    # Create figure
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
    
    # Save to temporary file
    plt.savefig("temp_chart.png", dpi=100)
    plt.close()
    
    # Open with PIL and FORCE resize to 512x512
    img = Image.open("temp_chart.png")
    
    # Create new image with EXACT size
    img_512 = img.resize((512, 512), Image.LANCZOS if hasattr(Image, 'LANCZOS') else 1)
    
    # Save the resized image
    img_512.save("chart.png", "PNG")
    
    # Close images
    img.close()
    img_512.close()
    
    # Delete temp file
    import os
    if os.path.exists("temp_chart.png"):
        os.remove("temp_chart.png")
    
    # Verify final size
    with Image.open("chart.png") as verify:
        w, h = verify.size
        print(f"Chart saved as chart.png")
        print(f"Dimensions: {w} x {h} pixels")
        
        if w == 512 and h == 512:
            print("✓ SUCCESS: Image is exactly 512x512 pixels!")
        else:
            print(f"✗ ERROR: Image is {w}x{h}, not 512x512")

if __name__ == "__main__":
    main()
