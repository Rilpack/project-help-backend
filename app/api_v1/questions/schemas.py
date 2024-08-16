from pydantic import BaseModel
from typing import List

from app.api_v1.choices.schemas import ChoiceBase


class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]
