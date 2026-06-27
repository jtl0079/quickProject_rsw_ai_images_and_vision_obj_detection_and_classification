from typing import Any

def create_metadata() -> dict[str, Any]:
    return {
        "image": {},        # the each file's metadata
        "objects": [],      # the list of objs, and inside each of obj metadata
    }