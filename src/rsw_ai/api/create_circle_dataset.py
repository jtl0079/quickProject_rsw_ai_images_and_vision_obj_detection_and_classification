# src/rsw_ai/api/create_circle_dataset.py

from rsw_ai.pipeline.create_circle_image_and_circle_metadata_file import (
    create_circle_image_and_create_circle_metadata_file,
)


def create_circle_dataset(
    image_filename: str = "circle.png",
    metadata_filename: str | None = None,
    width: int = 500,
    height: int = 500,
    center: tuple[int, int] | None = None,
    radius: int = 100,
    circle_color: tuple[int, int, int] = (0, 0, 0),
    background_color: tuple[int, int, int] = (255, 255, 255),
    thickness: int = 3,
) -> None:
    """
    Create a circle dataset consisting of an image and its metadata.
    """

    create_circle_image_and_create_circle_metadata_file(
        image_filename=image_filename,
        metadata_filename=metadata_filename,
        width=width,
        height=height,
        center=center,
        radius=radius,
        circle_color=circle_color,
        background_color=background_color,
        thickness=thickness,
    )