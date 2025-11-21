"""
Final step: Create a four-panel statistics meme demonstrating selection bias.
Assembles original image, stippled image, block letter, and masked image.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
import os


def create_statistics_meme(
    original_img: np.ndarray,
    stipple_img: np.ndarray, 
    block_letter_img: np.ndarray,
    masked_stipple_img: np.ndarray,
    output_path: str = "statistics_meme.png",
    dpi: int = 150,
    background_color: str = "white"
) -> None:
    """
    Create a four-panel statistics meme demonstrating selection bias.
    
    Parameters
    ----------
    original_img : np.ndarray
        Original grayscale image (Reality)
    stipple_img : np.ndarray
        Stippled image (Your Model) 
    block_letter_img : np.ndarray
        Block letter image (Selection Bias)
    masked_stipple_img : np.ndarray
        Masked stippled image (Estimate)
    output_path : str
        Path to save the output meme image
    dpi : int
        Output resolution in dots per inch
    background_color : str
        Background color for the meme ("white", "lightgray", etc.)
    """
    # Create figure with 1x4 subplots
    fig = plt.figure(figsize=(16, 4), facecolor=background_color)
    
    # Use GridSpec for better control
    gs = gridspec.GridSpec(1, 4, figure=fig, wspace=0.05, hspace=0)
    
    # Titles for each panel
    titles = ["Reality", "Your Model", "Selection Bias", "Estimate"]
    images = [original_img, stipple_img, block_letter_img, masked_stipple_img]
    
    # Create each subplot
    for i, (title, img) in enumerate(zip(titles, images)):
        ax = fig.add_subplot(gs[0, i])
        
        # Display image
        ax.imshow(img, cmap='gray', vmin=0, vmax=1)
        ax.axis('off')
        
        # Add title
        ax.set_title(title, fontsize=16, fontweight='bold', pad=10)
    
    # Add overall title
    fig.suptitle("Selection Bias & Missing Data", fontsize=20, fontweight='bold', y=0.95)
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig(output_path, dpi=dpi, bbox_inches='tight', facecolor=background_color)
    plt.close()
    
    print(f"Statistics meme saved to: {output_path}")
    print(f"Image size: {fig.get_size_inches()} inches at {dpi} DPI")


def create_statistics_meme_vertical(
    original_img: np.ndarray,
    stipple_img: np.ndarray, 
    block_letter_img: np.ndarray,
    masked_stipple_img: np.ndarray,
    output_path: str = "statistics_meme_vertical.png",
    dpi: int = 150,
    background_color: str = "white"
) -> None:
    """
    Create a vertical four-panel statistics meme (alternative layout).
    """
    # Create figure with 4x1 subplots
    fig = plt.figure(figsize=(6, 16), facecolor=background_color)
    
    # Use GridSpec for better control
    gs = gridspec.GridSpec(4, 1, figure=fig, wspace=0, hspace=0.1)
    
    # Titles for each panel
    titles = ["Reality", "Your Model", "Selection Bias", "Estimate"]
    images = [original_img, stipple_img, block_letter_img, masked_stipple_img]
    
    # Create each subplot
    for i, (title, img) in enumerate(zip(titles, images)):
        ax = fig.add_subplot(gs[i, 0])
        
        # Display image
        ax.imshow(img, cmap='gray', vmin=0, vmax=1)
        ax.axis('off')
        
        # Add title
        ax.set_title(title, fontsize=14, fontweight='bold', pad=10)
    
    # Add overall title
    fig.suptitle("Selection Bias & Missing Data", fontsize=18, fontweight='bold', y=0.98)
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig(output_path, dpi=dpi, bbox_inches='tight', facecolor=background_color)
    plt.close()
    
    print(f"Vertical statistics meme saved to: {output_path}")