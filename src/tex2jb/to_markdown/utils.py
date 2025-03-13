def remove_leading_white_spaces(text: str) -> str:

    lines = text.split("\n")
    stripped_lines = [line.lstrip() for line in lines]

    return "\n".join(stripped_lines)
