import io
from typing import List

from fastapi import UploadFile
from PyPDF2 import PdfFileMerger


def merge_files(files: List[UploadFile]) -> bytes:
    output_stream = io.BytesIO()
    merger = PdfFileMerger()
    for file in files:
        merger.append(file.file)
    merger.write(output_stream)
    output = output_stream.getvalue()
    output_stream.close()
    return output
