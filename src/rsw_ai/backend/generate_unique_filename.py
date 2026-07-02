from pathlib import Path
from datetime import datetime


def generate_unique_filename(filepath: str) -> str:
    """
    Generate an available filepath that does not already exist.

    The generated filename follows the format:

        {filename}_{current_time}_{seq}{extension}

    where:
        - filename     : Original filename without extension.
        - current_time : Current local time in YYYYMMDD_HHMMSS format.
        - seq          : Sequential number starting from 1.
                         If a generated filename already exists,
                         the sequence number is incremented until
                         an available filename is found.

    Parameters
    ----------
    filepath : str
        Target filepath used as the filename template.

    Returns
    -------
    str
        A filepath with a unique filename that does not already exist.

    Example
    -------
    Input:
        outputs/images/circle.png

    Output:
        outputs/images/circle_20260628_143210_1.png
    """

    path = Path(filepath)

    directory = path.parent
    filename = path.stem
    extension = path.suffix

    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

    seq = 1

    while True:
        candidate = directory / f"{filename}_{current_time}_{seq}{extension}"

        if not candidate.exists():
            return str(candidate)

        seq += 1
