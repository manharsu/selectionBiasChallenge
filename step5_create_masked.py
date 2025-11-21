"""
Step 5: Create a masked stippled image by applying the block letter mask.
This represents the biased estimate after selection bias removes data points.
"""

import numpy as np


def create_masked_stipple(
    stipple_img: np.ndarray, 
    mask_img: np.ndarray, 
    threshold: float = 0.5
) -> np.ndarray:
    """
    Apply a block letter mask to the stippled image to demonstrate selection bias.
    
    Parameters
    ----------
    stipple_img : np.ndarray
        Stippled image as 2D array (height, width) with values in [0, 1]
        where 0.0 = black dot, 1.0 = white background
    mask_img : np.ndarray  
        Mask image as 2D array (height, width) with values in [0, 1]
        where 0.0 = black (mask area), 1.0 = white (keep area)
    threshold : float
        Threshold for determining mask area (pixels below threshold are masked)
    
    Returns
    -------
    masked_stipple : np.ndarray
        Masked stippled image where stipples in mask area are removed
        Same format as stipple_img: 0.0 = black dot, 1.0 = white background
    """
    # Ensure both images have the same shape
    if stipple_img.shape != mask_img.shape:
        raise ValueError(f"Image shapes don't match: stipple {stipple_img.shape}, mask {mask_img.shape}")
    
    # Create a copy of the stipple image
    masked_stipple = stipple_img.copy()
    
    # Identify mask areas (where mask is dark, below threshold)
    mask_areas = mask_img < threshold
    
    # In mask areas, remove stipples by setting to white background (1.0)
    # Note: In stipple_img, 0.0 = black dot (stipple), 1.0 = white background
    # We want to remove stipples in mask areas, so set those pixels to 1.0 (white)
    masked_stipple[mask_areas] = 1.0
    
    print(f"Applied mask to stippled image")
    print(f"Masked areas: {np.sum(mask_areas)} pixels ({np.sum(mask_areas) / mask_areas.size * 100:.1f}% of image)")
    print(f"Remaining stipples: {np.sum(masked_stipple == 0.0)}")
    
    return masked_stipple