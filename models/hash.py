from pydantic import BaseModel


class GenerateHashModel(BaseModel):
    string: str
