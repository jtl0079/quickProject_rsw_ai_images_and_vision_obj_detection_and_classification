import json

def create_annotation_json(
    filename: str,
    objects: dict
):
    """
    objects format:
    
    {
        "class": "1",
        "center":"[x,y]",
        "bbox": [x1, y1, x2, y2],
        "rotation" = 30,
        "object_color" = "",
        "background_color" = "",
        ""
            
    }
    """

    annotation = {
        "image": filename,
        "objects": objects
    }

    return annotation