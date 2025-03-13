from TexSoup.data import TexNode
from typing import Optional
from ..context import ToMarkdownContext


def convert_exercise_env_to_markdown(
    exercise_env_node: TexNode,
    context: Optional[ToMarkdownContext] = None,
) -> str:

    assert context is not None, "context is required"

    # A list of markdown content strings
    markdown_contents: list[str] = []

    # Begin block template
    begin_block = "````{{admonition}} Exercise {exercise_numbering}\n:class: exercise\n"

    # Get the current exercise index
    current_exercise_index = context.current_exercise_index

    # Increment the current exercise index
    context.current_exercise_index += 1

    # Interpolate the begin block
    begin_block = begin_block.format(
        exercise_numbering=context.exercise_numberings[current_exercise_index],
    )

    markdown_contents.append(begin_block)

    # Label
    label_node = exercise_env_node.find("label")
    if label_node is not None:
        label = str(label_node.string)
        markdown_contents.append(f":label: {label}\n")

    # Convert the environment contents to markdown

    from ..tex_content import convert_tex_contents_to_markdown

    exercise_env_contents_markdown_content = convert_tex_contents_to_markdown(
        exercise_env_node.contents,
        context,
    )
    markdown_contents.append(exercise_env_contents_markdown_content)

    # End block
    end_block = "\n````\n"
    markdown_contents.append(end_block)

    # Join the markdown strings
    markdown_content = "".join(markdown_contents)

    return markdown_content
