

def create_circle_metadata(
    filename: str,
    width: int,
    height: int,
    center: tuple[int, int] | None,
    radius: int,
    circle_color: tuple[int, int, int],
    thickness: int,
) -> dict:
    """
    Create a metadata dictionary in the Dataset Generator format for a circle.

    Parameters
    ----------
    filename : str
        Image filename used in the metadata.
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
    thickness : int
        Border thickness. A value of -1 indicates a filled circle.

    Returns
    -------
    dict
        Metadata dictionary containing image information and object annotations.
    """
    # Determine the actual center.
    if center is None:
        center = (width // 2, height // 2)
    cx, cy = center

    # Compute the bounding box and object dimensions.
    xmin = cx - radius
    ymin = cy - radius
    xmax = cx + radius
    ymax = cy + radius
    obj_width = 2 * radius
    obj_height = 2 * radius

    return {
        "image": {
            "filename": filename,
            "width": width,
            "height": height,
        },
        "objects": [
            {
                "id": 0,
                "class": "circle",
                "center": [cx, cy],
                "bbox": {
                    "xmin": xmin,
                    "ymin": ymin,
                    "xmax": xmax,
                    "ymax": ymax,
                },
                "width": obj_width,
                "height": obj_height,
                "radius": radius,
                "rotation": 0,
                "color": list(circle_color),
                "filled": thickness == -1,
            }
        ],
    }