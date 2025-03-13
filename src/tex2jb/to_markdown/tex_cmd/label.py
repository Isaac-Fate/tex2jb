from TexSoup.data import TexNode


def convert_label_cmd_to_markdown(tex_node: TexNode) -> str:
    """The markdown content for the label command is an empty string
    since the label should be handled in the environment.

    Parameters
    ----------
    tex_node : TexNode
        The label command node.

    Returns
    -------
    str
        Markdown content.
    """

    return ""
