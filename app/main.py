from io import BytesIO
from typing import List

from fastapi import FastAPI, Response, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from app.utils.merge_files import merge_files

app = FastAPI(
    title="MergePDFFiles",
    description="Given several PDF files, merge them into one",
    version="0.0.1",
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post(
    "/merge",
    responses={200: {"content": {"application/pdf": {}}}},
    response_class=Response,
)
async def merge(files: List[UploadFile]) -> Response:
    result = merge_files(files)
    return Response(content=result, media_type="application/pdf")
