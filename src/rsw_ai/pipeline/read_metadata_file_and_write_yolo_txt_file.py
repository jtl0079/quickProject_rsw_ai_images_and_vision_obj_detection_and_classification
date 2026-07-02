from pathlib import Path

from rsw_ai.backend.read_metadata_file import read_metadata_file
from rsw_ai.backend.metadata_to_yolo_txt import metadata_to_yolo_txt
from rsw_ai.backend.write_text_file import write_text_file


# NOTE
#
# 1. read_metadata_file
# 2. metadata_to_yolo_txt
# 3. write_text_file
#
# Canonical Name:
#   read_metadata_file_and_metadata_to_yolo_txt_and_write_text_file
#
# Alias (used for filename/module name)
#   read_metadata_file_and_write_yolo_txt_file
#
# Reason
# Canonical name exceeds the filename length guideline.


def read_metadata_file_and_write_yolo_txt_file(
    metadata_file: str | Path,
    output_file: str | Path,
) -> None:

    metadata = read_metadata_file(metadata_file)

    yolo_lines = metadata_to_yolo_txt(metadata)

    write_text_file(
        output_file=output_file,
        lines=yolo_lines,
    )
