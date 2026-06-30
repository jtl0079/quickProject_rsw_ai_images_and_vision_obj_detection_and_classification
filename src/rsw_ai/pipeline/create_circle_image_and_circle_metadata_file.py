# rsw_ai/pipeline/create_circle_image_and_circle_metadata_file.py

from rsw_ai.backend.create_circle_image import create_circle_image
from rsw_ai.backend.create_circle_metadata import create_circle_metadata
from rsw_ai.backend.create_metadata_file import create_metadata_file

from rsw_ai.pipeline.create_metadata_and_write_image_metadata import (
    create_metadata_and_write_image_metadata,
)


# NOTE
# 1. create_circle_image
# 2. create_metadata_and_write_image_metadata
# 3. write_circle_metadata
# 4. create_metadata_file

def create_circle_image_and_create_metadata_and_write_image_metadata_and_write_circle_metadata_and_create_metadata_file(
    filename: str = "circle.png",
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
    Create a circle image and automatically save the corresponding JSON metadata.

    Parameters
    ----------
    filename : str
        Output image filename.
    metadata_filename : str, optional
        Output JSON filename. If None, defaults to the image filename
        with its extension replaced by '.json'.
    width : int
        Image width in pixels.
    height : int
        Image height in pixels.
    center : tuple[int, int] | None
        Circle center coordinates (x, y). If None, the image center is used.
    radius : int
        Circle radius in pixels.
    circle_color : tuple[int, int, int]
        Circle color in BGR format.
    background_color : tuple[int, int, int]
        Background color in BGR format.
    thickness : int
        Border thickness. A value of -1 indicates a filled circle.

    Returns
    -------
    None
    """

    # 1. Create and save the image.
    create_circle_image(
        filename=filename,
        width=width,
        height=height,
        center=center,
        radius=radius,
        circle_color=circle_color,
        background_color=background_color,
        thickness=thickness,
    )

    # 2. Initialize metadata with image information.
    metadata = create_metadata_and_write_image_metadata(
        filename=filename,
        width=width,
        height=height,
    )

    # 3. Create and append the circle metadata.
    metadata["objects"].append(
        create_circle_metadata(
            object_id=0,
            center=center,
            radius=radius,
            color=circle_color,
            filled=(thickness == -1),
        )
    )

    # 4. Determine JSON output path and save.
    if metadata_filename is None:
        metadata_filename = filename.rsplit(".", 1)[0] + ".json"

    create_metadata_file(
        file_path=metadata_filename,
        metadata=metadata,
    )