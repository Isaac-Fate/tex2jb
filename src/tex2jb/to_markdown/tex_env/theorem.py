from TexSoup.data import TexNode
from typing import Optional
from ..context import ToMarkdownContext
from ..utils import remove_leading_white_spaces


def convert_theorem_env_to_markdown(
    theorem_env_node: TexNode,
    context: Optional[ToMarkdownContext] = None,
) -> str:

    # Get the environment name
    theorem_env_name = theorem_env_node.name

    # A list of markdown content strings
    markdown_contents: list[str] = []

    # Begin block template
    begin_block = "````{{prf:{theorem_env_name}}} {theorem_title}\n"

    # Get the theorem title from the args
    if len(theorem_env_node.args) > 0:
        theorem_title = str(theorem_env_node.args[0].string)

        # Clear the args so that it doesn't show up in the markdown of the environment contents
        theorem_env_node.args.clear()
    else:
        theorem_title = ""

    # Interpolate the begin block
    begin_block = begin_block.format(
        theorem_env_name=theorem_env_name,
        theorem_title=theorem_title,
    )

    markdown_contents.append(begin_block)

    # Label
    label_node = theorem_env_node.find("label")
    if label_node is not None:
        label = str(label_node.string)
        markdown_contents.append(f":label: {label}\n")

    # Convert the environment contents to markdown

    from ..tex_content import convert_tex_contents_to_markdown

    theorem_env_contents_markdown_content = convert_tex_contents_to_markdown(
        theorem_env_node.contents,
        context,
    )
    markdown_contents.append(theorem_env_contents_markdown_content)

    # End block
    end_block = "\n````\n"
    markdown_contents.append(end_block)

    # Join the markdown strings
    markdown_content = "".join(markdown_contents)

    return remove_leading_white_spaces(markdown_content)
