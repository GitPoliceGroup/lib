from git_police.augmenters.core import Augmenter
from git_police.augmenters.german.german import GermanTranslator

class GermanAugmenter(Augmenter):
    def __init__(self):
        super().__init__(
            "German",
            "Translates the commit message to German."
        )
        
        self.translator = GermanTranslator()
    
    def augment(self, message: str) -> str:
        return self.translator.translate(message)