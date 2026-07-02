from typing import Any

from rsw_ai.backend.create_metadata import create_metadata
from rsw_ai.backend.write_image_metadata import write_image_metadata


def create_metadata_and_write_image_metadata(
    filename: str,
    width: int,
    height: int,
) -> dict[str, Any]:
    """
    Create an empty metadata dictionary and initialize the image metadata.

    Parameters:
        filename: Name of the image file.
        width: Image width in pixels.
        height: Image height in pixels.

    Returns:
        Initialized metadata dictionary.
    """

    metadata = create_metadata()

    write_image_metadata(
        metadata=metadata,
        filename=filename,
        width=width,
        height=height,
    )

    return metadata
