from typing import Optional
from TexSoup.data import TexNode, TexEnv


def is_tex_env(tex_node: TexNode) -> bool:

    return isinstance(tex_node.expr, TexEnv)


def find_tex_env_label(tex_node: TexNode) -> Optional[str]:

    if not is_tex_env(tex_node):
        return None

    # Find the label node
    label_node: Optional[TexNode] = tex_node.find("label")

    if label_node is None:
        return None

    # Get the label content
    label_node: TexNode
    label = str(label_node.string)

    return label


class TexEnvNumberingTracker:

    def __init__(self) -> None:

        self._chapter_number = 0
        self._env_number = 0

    @property
    def numbering(self) -> str:

        return f"{self._chapter_number}.{self._env_number}"

    def increment_chapter(self) -> None:

        self._chapter_number += 1

        # Reset the environment number
        self._env_number = 0

    def increment_env(self) -> None:

        self._env_number += 1
