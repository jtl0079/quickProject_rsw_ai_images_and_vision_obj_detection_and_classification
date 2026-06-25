import cv2
import numpy as np


def create_triangle_image(
    filename: str = "triangle.png",
    width: int = 500,
    height: int = 500,
    center: tuple[int, int] | None = None,
    side_length: int = 200,
    rotation: float = 0.0,
    triangle_color: tuple[int, int, int] = (0, 0, 0),
    background_color: tuple[int, int, int] = (255, 255, 255),
    thickness: int = 3,
) -> np.ndarray:
    """
    Create an image containing an equilateral triangle
    and save it to a file.

    Parameters
    ----------
    filename : str
        Output image filename.

    width : int
        Width of the image in pixels.

    height : int
        Height of the image in pixels.

    center : tuple[int, int] | None
        Center position of the triangle as (x, y).

        If None, the triangle will be placed at the
        center of the image.

    side_length : int
        Length of each side of the equilateral triangle.

    rotation : float
        Rotation angle in degrees.

        Counter-clockwise rotation around the
        triangle center.

    triangle_color : tuple[int, int, int]
        Triangle color in BGR format.

        Examples:
        - Black : (0, 0, 0)
        - White : (255, 255, 255)
        - Red   : (0, 0, 255)
        - Green : (0, 255, 0)
        - Blue  : (255, 0, 0)

    background_color : tuple[int, int, int]
        Background color in BGR format.

    thickness : int
        Thickness of the triangle border.

        Use -1 to create a filled triangle.

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

    # Default center
    if center is None:
        center = (width // 2, height // 2)

    cx, cy = center

    # Equilateral triangle height
    triangle_height = np.sqrt(3) / 2 * side_length

    # Triangle centered at origin
    points = np.array(
        [
            [0, -2 * triangle_height / 3],       # top
            [-side_length / 2, triangle_height / 3],  # bottom-left
            [side_length / 2, triangle_height / 3],   # bottom-right
        ],
        dtype=np.float32,
    )

    # Rotation matrix
    theta = np.radians(rotation)

    rotation_matrix = np.array(
        [
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta),  np.cos(theta)],
        ],
        dtype=np.float32,
    )

    # Rotate around origin
    points = points @ rotation_matrix.T

    # Translate to desired center
    points[:, 0] += cx
    points[:, 1] += cy

    points = points.astype(np.int32)

    # Draw triangle
    if thickness == -1:
        cv2.fillPoly(
            image,
            [points],
            triangle_color,
        )
    else:
        cv2.polylines(
            image,
            [points],
            isClosed=True,
            color=triangle_color,
            thickness=thickness,
        )

    # Save image
    cv2.imwrite(filename, image)

    return image
