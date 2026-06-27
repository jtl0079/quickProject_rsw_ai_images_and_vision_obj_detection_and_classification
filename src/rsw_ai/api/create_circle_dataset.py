# src/rsw_ai/api/create_circle_dataset.py

from rsw_ai.pipeline.create_circle_image_and_create_metadata_and_write_image_metadata_and_write_circle_metadata_and_create_metadata_file import (
    create_circle_image_and_create_metadata_and_write_image_metadata_and_write_circle_metadata_and_create_metadata_file,
)


def create_circle_dataset(
    filename: str = "circle.png",
    json_filename: str | None = None,
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

    create_circle_image_and_create_metadata_and_write_image_metadata_and_write_circle_metadata_and_create_metadata_file(
        filename=filename,
        json_filename=json_filename,
        width=width,
        height=height,
        center=center,
        radius=radius,
        circle_color=circle_color,
        background_color=background_color,
        thickness=thickness,
    )