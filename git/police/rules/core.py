from abc import ABC, abstractmethod

class Rule(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
    @abstractmethod
    def __call__(self, message: str) -> tuple[bool, str]:
        pass