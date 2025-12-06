# chart.py
# Email: 25ds1000231@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

def main():
    # Generate realistic synthetic data for support efficiency analysis
    np.random.seed(42)
    
    # Create data with different resolution times per tier
    tier1 = np.random.lognormal(mean=1.3, sigma=0.4, size=250)
    tier2 = np.random.lognormal(mean=1.5, sigma=0.45, size=150)
    tier3 = np.random.lognormal(mean=1.7, sigma=0.5, size=100)
    
    df = pd.DataFrame({
        'Support_Tier': ['Tier 1']*250 + ['Tier 2']*150 + ['Tier 3']*100,
        'Resolution_Time_Hours': np.concatenate([tier1, tier2, tier3])
    })
    
    # Set professional Seaborn styling
    sns.set_style("whitegrid")
    sns.set_context("talk")
    
    # Create figure with specified size
    plt.figure(figsize=(8, 8))
    
    # Create violinplot
    sns.violinplot(
        data=df,
        x='Support_Tier',
        y='Resolution_Time_Hours',
        palette='Set2',
        inner='quartile'
    )
    
    # Add titles and labels
    plt.title('Support Resolution Time by Tier', fontsize=16, fontweight='bold')
    plt.xlabel('Support Tier', fontsize=14)
    plt.ylabel('Resolution Time (hours)', fontsize=14)
    
    # Save with specified parameters
    plt.savefig('chart.png', dpi=64, bbox_inches='tight')
    plt.close()
    
    # Resize to EXACTLY 512x512 pixels
    img = Image.open('chart.png')
    img_resized = img.resize((512, 512), Image.LANCZOS if hasattr(Image, 'LANCZOS') else 1)
    img_resized.save('chart.png')
    img.close()
    img_resized.close()
    
    # Verify dimensions
    verify = Image.open('chart.png')
    w, h = verify.size
    verify.close()
    
    print(f"Generated chart.png ({w}x{h} pixels)")
    
    if w == 512 and h == 512:
        print("✓ Chart is exactly 512x512 pixels")
    else:
        print(f"⚠ Warning: Chart is {w}x{h}, expected 512x512")

if __name__ == "__main__":
    main()
