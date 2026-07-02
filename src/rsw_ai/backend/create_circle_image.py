import cv2
import numpy as np


def create_circle_image(
    filename: str = "circle.png",
    width: int = 500,
    height: int = 500,
    center: tuple[int, int] | None = None,
    radius: int = 100,
    circle_color: tuple[int, int, int] = (0, 0, 0),
    background_color: tuple[int, int, int] = (255, 255, 255),
    thickness: int = 3,
) -> np.ndarray:
    """
    Create an image containing a circle and save it to a file.

    Parameters
    ----------
    filename : str
        Output image filename.

    width : int
        Width of the image in pixels.

    height : int
        Height of the image in pixels.

    center : tuple[int, int] | None
        Center of the circle as (x, y).

        If None, the circle will be placed at the
        center of the image.

    radius : int
        Radius of the circle in pixels.

    circle_color : tuple[int, int, int]
        Circle color in BGR format.

        Examples:
        - Black : (0, 0, 0)
        - White : (255, 255, 255)
        - Red   : (0, 0, 255)
        - Green : (0, 255, 0)
        - Blue  : (255, 0, 0)

    background_color : tuple[int, int, int]
        Background color in BGR format.

    thickness : int
        Thickness of the circle border.

        Use -1 to create a filled circle.

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

    # Use image center if not specified
    if center is None:
        center = (width // 2, height // 2)

    # Draw circle
    cv2.circle(
        image,
        center,
        radius,
        circle_color,
        thickness,
    )

    # Save image
    cv2.imwrite(filename, image)

    return image
