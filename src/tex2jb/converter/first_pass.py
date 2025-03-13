from TexSoup.data import TexNode
from typing import Optional
from pathlib import Path
from ..schemas import (
    JupyterBookToc,
    JupyterBookTocPart,
    JupyterBookTocChapter,
    JupyterBookTocSection,
)
from ..tex_env import TexEnvNumberingTracker, find_tex_env_label


def first_pass(
    document_node: TexNode,
) -> tuple[JupyterBookToc, list[Path], list[str], dict[str, str]]:

    # Jupyter Book TOC
    toc = JupyterBookToc()
    current_toc_part = JupyterBookTocPart()
    current_toc_chapter: Optional[JupyterBookTocChapter] = None

    # Current chapter title
    current_chapter_title: Optional[str] = None

    # Add the part
    toc.parts.append(current_toc_part)

    # Markdown file path for each page
    page_file_paths: list[Path] = []

    # Keep track of the exercise numberings
    exercise_numberings: list[str] = []
    exercise_numbering_tracker = TexEnvNumberingTracker()

    # Keep track of the URL path corresponding to each exercise with a label
    exercise_label_to_url_path: dict[str, str] = {}

    document_node: TexNode
    for tex_element in document_node.contents:

        if isinstance(tex_element, TexNode):

            # Get the node name
            node_name = tex_element.name

            if node_name in ("part", "part*"):
                # Get the part caption
                part_caption = str(tex_element.string)

                if current_toc_part.caption is None:
                    current_toc_part.caption = part_caption

                # Create a new part
                else:
                    new_toc_part = JupyterBookTocPart(
                        caption=part_caption,
                    )

                    # Add the new part
                    toc.parts.append(new_toc_part)

                    # Update the current part
                    current_toc_part = new_toc_part

            elif node_name in ("chapter", "chapter*"):
                # Get the chapter title
                chapter_title = str(tex_element.string)

                # Infer the page path
                page_path = Path(chapter_title) / "index.md"

                # Add the path
                page_file_paths.append(page_path)

                # Create a new chapter
                new_chapter = JupyterBookTocChapter(
                    file=page_path,
                )

                # Add the new chapter
                current_toc_part.chapters.append(new_chapter)

                # Update the current chapter
                current_toc_chapter = new_chapter

                # Update the current chapter title
                current_chapter_title = chapter_title

                # Update the exercise numbering tracker
                if node_name == "chapter":
                    exercise_numbering_tracker.increment_chapter()

            elif node_name in ("section", "section*"):
                # Get the section title
                section_title = str(tex_element.string)

                if current_chapter_title is None:
                    raise RuntimeError(
                        "no chapter is not found before the current section"
                    )

                # Infer the page path
                page_path = Path(current_chapter_title) / Path(
                    section_title
                ).with_suffix(".md")

                # Add the path
                page_file_paths.append(page_path)

                # Create a new section
                new_section = JupyterBookTocSection(
                    file=page_path,
                )

                # Add the new section
                current_toc_chapter.sections.append(new_section)

            elif node_name == "exercise":

                # Get the label
                label = find_tex_env_label(tex_element)

                if label is not None:
                    # Get the current page file path
                    current_page_file_path = page_file_paths[-1]

                    # Set the URL path for the exercise
                    exercise_label_to_url_path[label] = (
                        current_page_file_path.with_suffix(f".html#{label}")
                    )

                # Update the exercise numbering tracker
                exercise_numbering_tracker.increment_env()

                # Add the exercise numbering
                exercise_numberings.append(exercise_numbering_tracker.numbering)

    return (
        toc,
        page_file_paths,
        exercise_numberings,
        exercise_label_to_url_path,
    )
