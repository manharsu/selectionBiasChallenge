"""
Step 4: Create a block letter for the statistics meme.
Generates a block letter (default "S") matching image dimensions.
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os


def create_block_letter_s(
    height: int, 
    width: int, 
    letter: str = "S", 
    font_size_ratio: float = 0.9
) -> np.ndarray:
    """
    Create a block letter matching image dimensions.
    
    Parameters
    ----------
    height : int
        Height of the output image
    width : int
        Width of the output image
    letter : str
        Letter to create (default "S")
    font_size_ratio : float
        Ratio of font size to image height (0.0 to 1.0)
    
    Returns
    -------
    letter_img : np.ndarray
        Binary letter image as 2D array (height, width) 
        with values in [0, 1] where 0.0 = black letter, 1.0 = white background
    """
    # Create a white background image
    img = Image.new('L', (width, height), color=255)
    draw = ImageDraw.Draw(img)
    
    # Calculate font size based on image height
    font_size = int(height * font_size_ratio)
    
    # Try multiple font paths
    font_paths = [
        # Common system fonts
        "/System/Library/Fonts/Helvetica.ttc",  # macOS
        "/System/Library/Fonts/Arial.ttf",      # macOS
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",  # Linux
        "C:/Windows/Fonts/arialbd.ttf",         # Windows
        "C:/Windows/Fonts/arial.ttf",           # Windows
    ]
    
    font = None
    for font_path in font_paths:
        try:
            if os.path.exists(font_path):
                # Handle .ttc files (TrueType collections)
                if font_path.endswith('.ttc'):
                    font = ImageFont.truetype(font_path, font_size, index=0)
                else:
                    font = ImageFont.truetype(font_path, font_size)
                print(f"Using font: {font_path}")
                break
        except Exception as e:
            continue
    
    # If no system font found, use default
    if font is None:
        try:
            font = ImageFont.load_default()
            print("Using default font")
        except:
            # Create a simple block letter using drawing primitives
            print("Creating block letter using drawing primitives")
            return _create_simple_block_letter(height, width, letter)
    
    # Calculate text position to center it
    try:
        # Try to get text bbox for more accurate centering
        bbox = draw.textbbox((0, 0), letter, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
    except:
        # Fallback estimation
        text_width = width * 0.6
        text_height = height * 0.8
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Draw the letter in black
    draw.text((x, y), letter, fill=0, font=font)
    
    # Convert to numpy array and normalize to [0, 1]
    letter_array = np.array(img, dtype=np.float32) / 255.0
    
    # Invert so letter is black (0.0) on white background (1.0)
    # PIL draws black text on white, so we're already in the right format
    
    print(f"Created block letter '{letter}' with size {height}x{width}")
    return letter_array


def _create_simple_block_letter(height: int, width: int, letter: str = "S") -> np.ndarray:
    """
    Fallback function to create a simple block letter using drawing primitives.
    """
    img = Image.new('L', (width, height), color=255)
    draw = ImageDraw.Draw(img)
    
    # Create a simple S shape using rectangles and ellipses
    center_x, center_y = width // 2, height // 2
    letter_width = width * 0.6
    letter_height = height * 0.8
    
    if letter.upper() == "S":
        # Draw a simple S shape using rectangles
        thickness = max(5, min(width, height) // 10)
        
        # Top curve
        draw.ellipse([
            center_x - letter_width//2, 
            center_y - letter_height//2,
            center_x + letter_width//2, 
            center_y
        ], outline=0, fill=255, width=thickness)
        
        # Bottom curve  
        draw.ellipse([
            center_x - letter_width//2, 
            center_y,
            center_x + letter_width//2, 
            center_y + letter_height//2
        ], outline=0, fill=255, width=thickness)
    
    # Convert to numpy array
    letter_array = np.array(img, dtype=np.float32) / 255.0
    return letter_array