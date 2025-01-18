from abc import ABC, abstractmethod
from pydantic import BaseModel

class TaskOutput(BaseModel):
    success: bool

class Task(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
    @abstractmethod
    def __call__(self) -> TaskOutput:
        pass