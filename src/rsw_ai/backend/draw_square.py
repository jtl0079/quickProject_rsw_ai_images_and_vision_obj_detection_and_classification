import cv2
import numpy as np


def draw_square(
    image: np.ndarray,
    center: tuple[int, int],
    side_length: int,
    rotation: float,
    color: tuple[int, int, int],
    thickness: int,
) -> None:
    """
    Draw a square on the given image.

    Parameters
    ----------
    image : numpy.ndarray
        Image to draw on (modified in-place).
    center : tuple[int, int]
        Center of the square (x, y).
    side_length : int
        Length of each side of the square.
    rotation : float
        Rotation angle in degrees (counter-clockwise).
    color : tuple[int, int, int]
        Square color in BGR format.
    thickness : int
        Border thickness. Use -1 for filled square.
    """
    cx, cy = center

    # Square vertices centered at origin
    points = np.array(
        [
            [-side_length / 2, -side_length / 2],  # top-left
            [side_length / 2, -side_length / 2],  # top-right
            [side_length / 2, side_length / 2],  # bottom-right
            [-side_length / 2, side_length / 2],  # bottom-left
        ],
        dtype=np.float32,
    )

    # Rotation matrix
    theta = np.radians(rotation)
    rotation_matrix = np.array(
        [
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)],
        ],
        dtype=np.float32,
    )

    # Rotate around origin
    points = points @ rotation_matrix.T

    # Translate to desired center
    points[:, 0] += cx
    points[:, 1] += cy

    points = points.astype(np.int32)

    # Draw the square
    if thickness == -1:
        cv2.fillPoly(image, [points], color)
    else:
        cv2.polylines(image, [points], isClosed=True, color=color, thickness=thickness)
