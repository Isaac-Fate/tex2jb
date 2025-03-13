from pydantic import BaseModel


class ToMarkdownContext(BaseModel):

    exercise_numberings: list[str] = []
    current_exercise_index: int = 0
