from TexSoup import TexSoup
from tex2jb import convert_tex_content_to_markdown
from tex2jb.to_markdown.tex_cmd import convert_label_cmd_to_markdown


def test_to_markdown():

    node = TexSoup(r"$\pi$").find("$")
    markdown_content = convert_tex_content_to_markdown(node)

    assert markdown_content == "$\\pi$"


def test_convert_label_cmd_to_markdown():

    tex_node = TexSoup(r"\label{thm:1}").find("label")
    markdown_content = convert_label_cmd_to_markdown(tex_node)

    assert markdown_content == ""
