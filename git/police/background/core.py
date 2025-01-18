from abc import ABC, abstractmethod

class BackgroundTask(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass