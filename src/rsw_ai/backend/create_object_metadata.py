from typing import Any


def create_object_metadata(
    object_id: int,
    object_class: str,
    center: tuple[int, int],
    bbox: dict[str, int],
    rotation: float = 0.0,
    color: tuple[int, int, int] = (0, 0, 0),
    filled: bool = False,
) -> dict[str, Any]:
    width = bbox["xmax"] - bbox["xmin"]
    height = bbox["ymax"] - bbox["ymin"]

    return {
        "id": object_id,
        "class": object_class,
        "center": [center[0], center[1]],
        "bbox": {
            "xmin": bbox["xmin"],
            "ymin": bbox["ymin"],
            "xmax": bbox["xmax"],
            "ymax": bbox["ymax"],
        },
        "width": width,
        "height": height,
        "rotation": rotation,
        "color": [color[0], color[1], color[2]],
        "filled": filled,
    }
