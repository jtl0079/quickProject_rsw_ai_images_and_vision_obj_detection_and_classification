import cv2
import numpy as np
from rsw_ai.backend.draw_square import *

def create_square_image(
    filename: str = "square.png",
    width: int = 500,
    height: int = 500,
    center: tuple[int, int] | None = None,
    side_length: int = 200,
    rotation: float = 0.0,
    square_color: tuple[int, int, int] = (0, 0, 0),
    background_color: tuple[int, int, int] = (255, 255, 255),
    thickness: int = 3,
) -> np.ndarray:
    """
    Create an image containing a square and save it to a file.

    Parameters
    ----------
    filename : str
        Output image filename.
    width : int
        Width of the image in pixels.
    height : int
        Height of the image in pixels.
    center : tuple[int, int] | None
        Center position of the square as (x, y).
        If None, the square will be placed at the center of the image.
    side_length : int
        Length of each side of the square.
    rotation : float
        Rotation angle in degrees (counter-clockwise around square center).
    square_color : tuple[int, int, int]
        Square color in BGR format.
        Examples: Black (0,0,0), White (255,255,255), Red (0,0,255).
    background_color : tuple[int, int, int]
        Background color in BGR format.
    thickness : int
        Thickness of the square border. Use -1 to create a filled square.

    Returns
    -------
    numpy.ndarray
        The generated image.
    """
    # Create background image
    image = np.full(
        (height, width, 3),
        background_color,
        dtype=np.uint8,
    )

    if center is None:
        center = (width // 2, height // 2)

    # Delegate drawing to the extracted function
    draw_square(
        image=image,
        center=center,
        side_length=side_length,
        rotation=rotation,
        color=square_color,
        thickness=thickness,
    )

    # Save image
    cv2.imwrite(filename, image)

    return image