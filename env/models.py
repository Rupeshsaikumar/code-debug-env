from pydantic import BaseModel

class Observation(BaseModel):
    code: str
    error: str
    step: int
    difficulty: str
    language: str = "python"   # future-ready

class Action(BaseModel):
    fixed_code: str

class Reward(BaseModel):
    score: float