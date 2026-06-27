
from typing import Any
from rsw_ai.backend.create_object_metadata import create_object_metadata


# /object/class = circle
def create_circle_metadata(
    object_id: int,
    center: tuple[int, int],
    radius: int,
    rotation: float = 0.0,
    color: tuple[int, int, int] = (0, 0, 0),
    filled: bool = False,
) -> dict[str, Any]:
    bbox = {
        "xmin": center[0] - radius,
        "ymin": center[1] - radius,
        "xmax": center[0] + radius,
        "ymax": center[1] + radius,
    }

    obj = create_object_metadata(
        object_id=object_id,
        object_class="circle",
        center=center,
        bbox=bbox,
        rotation=rotation,
        color=color,
        filled=filled,
    )
    obj["radius"] = radius
    return obj