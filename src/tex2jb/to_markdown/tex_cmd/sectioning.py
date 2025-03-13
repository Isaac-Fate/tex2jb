from TexSoup.data import TexNode


def convert_sectioning_cmd_to_markdown(tex_node: TexNode) -> str:

    # Get the command name
    cmd_name = tex_node.name

    match cmd_name:
        case "chapter" | "chapter*" | "section" | "section*":
            prefix = "#"

        case "subsection" | "subsection*":
            prefix = "##"

        case "subsubsection" | "subsubsection*":
            prefix = "###"

    # Get the title
    args = tex_node.args
    if len(args) == 0:
        raise ValueError(f"argument of {cmd_name} is empty")
    title = args[0].string

    return f"{prefix} {title}\n"
