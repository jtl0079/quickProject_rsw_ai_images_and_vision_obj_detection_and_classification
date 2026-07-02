from typing import Any


def write_image_metadata(
    metadata: dict[str, Any],
    filename: str,
    width: int,
    height: int,
) -> None:
    metadata["image"] = {
        "filename": filename,
        "width": width,
        "height": height,
    }
