from TexSoup.data import TexNode
from typing import Optional
from ..context import ToMarkdownContext


def convert_math_env_to_markdown(
    math_env_node: TexNode,
    context: Optional[ToMarkdownContext] = None,
) -> str:

    # A list of markdown content strings
    markdown_contents: list[str] = []

    # Begin block template
    begin_block = "```{math}\n"

    markdown_contents.append(begin_block)

    # Ge the environment name
    math_env_name = math_env_node.name

    # Begin environment
    begin_env = f"\\begin{{{math_env_name}}}\n"
    markdown_contents.append(begin_env)

    # Label
    label_node = math_env_node.find("label")
    if label_node is not None:
        label = str(label_node.string)
        markdown_contents.append(f":label: {label}\n")

    # Convert the environment contents to markdown

    from ..tex_content import convert_tex_contents_to_markdown

    exercise_env_contents_markdown_content = convert_tex_contents_to_markdown(
        math_env_node.contents,
        context,
    )
    markdown_contents.append(exercise_env_contents_markdown_content)

    # End environment
    end_env = f"\\end{{{math_env_name}}}"
    markdown_contents.append(end_env)

    # End block
    end_block = "\n```\n"
    markdown_contents.append(end_block)

    # Join the markdown strings
    markdown_content = "".join(markdown_contents)

    return markdown_content
