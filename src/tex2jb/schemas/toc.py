from pydantic import BaseModel
from pydantic.functional_serializers import PlainSerializer
from typing import Annotated, Optional
from pathlib import Path


SerializablePath = Annotated[
    Path,
    PlainSerializer(
        lambda path: str(path),
        return_type=str,
    ),
]


class JupyterBookTocSection(BaseModel):

    file: SerializablePath


class JupyterBookTocChapter(BaseModel):

    file: SerializablePath
    sections: list[JupyterBookTocSection] = []


class JupyterBookTocPart(BaseModel):

    caption: Optional[str] = None
    chapters: list[JupyterBookTocChapter] = []


class JupyterBookToc(BaseModel):

    format: str = "jb-book"
    root: SerializablePath = Path("intro")
    parts: list = []
