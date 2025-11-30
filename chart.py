# chart.py
# Email: 25ds1000231@ds.study.iitm.ac.in
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import io

def main():
    print("Starting chart generation...")
    
    np.random.seed(42)
    df = pd.DataFrame({
        "Tier": np.random.choice(["Tier 1", "Tier 2", "Tier 3"], 500),
        "Resolution_Time": np.random.lognormal(mean=1.5, sigma=0.5, size=500)
    })
    
    print("Data created successfully")
    
    sns.set_style("whitegrid")
    sns.set_context("talk")
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 10))
    
    print("Creating violin plot...")
    
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
    
    # Save to BytesIO buffer (in memory, not to disk)
    print("Saving to memory buffer...")
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=100)
    buf.seek(0)
    plt.close()
    
    print("Opening image from buffer...")
    # Open from memory
    img = Image.open(buf)
    print(f"Original size: {img.size[0]} x {img.size[1]}")
    
    # Resize to EXACTLY 512x512
    print("Resizing to 512x512...")
    img_resized = img.resize((512, 512), Image.LANCZOS if hasattr(Image, 'LANCZOS') else 1)
    print(f"Resized to: {img_resized.size[0]} x {img_resized.size[1]}")
    
    # Save as PNG with exact dimensions
    print("Saving chart.png...")
    img_resized.save("chart.png", format='PNG', optimize=False)
    
    # Close buffer
    buf.close()
    
    print("\nVerifying saved file...")
    # Verify the actual saved file
    verify = Image.open("chart.png")
    w, h = verify.size
    verify.close()
    
    print(f"\n{'='*50}")
    print(f"FINAL RESULT:")
    print(f"File: chart.png")
    print(f"Dimensions: {w} x {h} pixels")
    print(f"{'='*50}\n")
    
    if w == 512 and h == 512:
        print("✓ SUCCESS: Image is exactly 512x512 pixels!")
        return 0
    else:
        print(f"✗ ERROR: Image is {w}x{h} instead of 512x512")
        print("\nAttempting force fix...")
        
        # One more attempt - force it
        force_img = Image.open("chart.png")
        force_resized = force_img.resize((512, 512), 1)
        force_resized.save("chart.png", format='PNG')
        force_img.close()
        force_resized.close()
        
        # Check again
        final_check = Image.open("chart.png")
        final_w, final_h = final_check.size
        final_check.close()
        print(f"After force fix: {final_w} x {final_h}")
        
        if final_w == 512 and final_h == 512:
            print("✓ Force fix successful!")
            return 0
        else:
            print("✗ Force fix failed")
            return 1

if __name__ == "__main__":
    exit(main())
