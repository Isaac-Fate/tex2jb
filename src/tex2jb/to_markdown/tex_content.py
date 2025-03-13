from TexSoup.data import TexNode, Token, TexEnv, TexCmd
from typing import Optional
from .context import ToMarkdownContext
from .tex_token import convert_tex_token_to_markdown
from .tex_cmd import convert_sectioning_cmd_to_markdown


def convert_tex_content_to_markdown(
    tex_content: TexNode | Token,
    context: Optional[ToMarkdownContext] = None,
) -> str:

    if isinstance(tex_content, TexNode):

        # Hanlde environment
        if isinstance(tex_content.expr, TexEnv):

            # Get the environment name
            env_name = tex_content.name

            match env_name:

                # Theorem environment
                case (
                    "theorem"
                    | "proposition"
                    | "lemma"
                    | "corollary"
                    | "example"
                    | "proof"
                ):

                    from .tex_env import convert_theorem_env_to_markdown

                    return convert_theorem_env_to_markdown(
                        tex_content,
                        context,
                    )

                # Exercise environment
                case "exercise":

                    from .tex_env import convert_exercise_env_to_markdown

                    return convert_exercise_env_to_markdown(
                        tex_content,
                        context,
                    )

                # Math environment
                case (
                    "align"
                    | "align*"
                    | "alignat"
                    | "alignat*"
                    | "equation"
                    | "equation*"
                    | "multline"
                    | "multline*"
                ):

                    # Delay the import to avoid circular import
                    from .tex_env import convert_math_env_to_markdown

                    return convert_math_env_to_markdown(
                        tex_content,
                        context,
                    )

                # Unkown environment
                case _:
                    return str(tex_content)

        # Hanlde command
        elif isinstance(tex_content.expr, TexCmd):

            # Get the command name
            cmd_name = tex_content.name

            match cmd_name:

                # Sectioning
                case (
                    "chapter"
                    | "chapter*"
                    | "section"
                    | "section*"
                    | "subsection"
                    | "subsection*"
                    | "subsubsection"
                    | "subsubsection*"
                ):
                    return convert_sectioning_cmd_to_markdown(tex_content)

                # Set empty strings for these commands
                case (
                    "maketitle"
                    | "frontmatter"
                    | "mainmatter"
                    | "tableofcontents"
                    | "label"
                    | "noindent"
                    | "nonumber"
                    | "item"
                    | "par"
                ):
                    return ""

                # Display the other command as it is
                case _:
                    return str(tex_content)

        else:
            return str(tex_content)

    elif isinstance(tex_content, Token):
        return convert_tex_token_to_markdown(tex_content)

    else:
        raise ValueError(f"unkown tex content type: {type(tex_content)}")


def convert_tex_contents_to_markdown(
    tex_contents: list[TexNode | Token],
    context: Optional[ToMarkdownContext] = None,
) -> str:

    markdown_contents: list[str] = []
    for tex_content in tex_contents:
        markdown_content = convert_tex_content_to_markdown(
            tex_content,
            context,
        )
        markdown_contents.append(markdown_content)

    markdown_content = "".join(markdown_contents)

    return markdown_content
