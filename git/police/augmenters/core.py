from abc import ABC, abstractmethod

class Augmenter(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def augment(self, message: str) -> str:
        pass