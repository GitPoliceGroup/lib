from abc import ABC, abstractmethod
from pydantic import BaseModel

class RuleOutput(BaseModel):
    success: bool
    message: str

class Rule(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
    @abstractmethod
    def __call__(self, message: str) -> RuleOutput:
        pass