
import cv2
import numpy as np


def draw_triangle(
    image: np.ndarray,
    center: tuple[int, int],
    side_length: int,
    rotation: float,
    color: tuple[int, int, int],
    thickness: int,
) -> None:
    """
    Draw an equilateral triangle on the given image.

    Parameters
    ----------
    image : numpy.ndarray
        Image to draw on (modified in-place).
    center : tuple[int, int]
        Center of the triangle (x, y).
    side_length : int
        Length of each side of the equilateral triangle.
    rotation : float
        Rotation angle in degrees (counter-clockwise).
    color : tuple[int, int, int]
        Triangle color in BGR format.
    thickness : int
        Border thickness. Use -1 for filled triangle.
    """
    cx, cy = center

    # Height of equilateral triangle
    triangle_height = np.sqrt(3) / 2 * side_length

    # Triangle vertices centered at origin
    points = np.array(
        [
            [0, -2 * triangle_height / 3],          # top
            [-side_length / 2, triangle_height / 3], # bottom-left
            [side_length / 2, triangle_height / 3],  # bottom-right
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

    # Draw the triangle
    if thickness == -1:
        cv2.fillPoly(image, [points], color)
    else:
        cv2.polylines(
            image, [points], isClosed=True, color=color, thickness=thickness
        )