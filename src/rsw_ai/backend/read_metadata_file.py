import json
from pathlib import Path
from typing import Any


def read_metadata_file(filepath: str | Path) -> dict[str, Any]:
    """
    Read a metadata JSON file.

    Parameters
    ----------
    filepath : str | Path
        Metadata JSON filepath.

    Returns
    -------
    dict
        Parsed JSON data.
    """
    with Path(filepath).open("r", encoding="utf-8") as f:
        return json.load(f)
