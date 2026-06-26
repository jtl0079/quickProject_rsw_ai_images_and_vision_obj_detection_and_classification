import json
import os


def create_metadata_file(
    file_path: str,
    metadata: dict,
    create_dirs: bool = True,
    indent: int = 2,
    encoding: str = "utf-8",
) -> None:
    """
    Save a metadata dictionary as a JSON file.

    Parameters
    ----------
    file_path : str
        Full path to the output JSON file (including .json extension).
    metadata : dict
        Dictionary containing the metadata to save.
    create_dirs : bool
        If True, create parent directories if they do not exist.
    indent : int
        JSON indentation level (use None for compact output).
    encoding : str
        File encoding.
    """
    if create_dirs:
        os.makedirs(os.path.dirname(file_path) or ".", exist_ok=True)

    with open(file_path, "w", encoding=encoding) as f:
        json.dump(metadata, f, indent=indent, ensure_ascii=False)