from git_police.augmenters.core import Augmenter

class PirateAugmenter(Augmenter):
    def __init__(self):
        super().__init__("Pirate Translator", "Turns the commit message into pirate speak.")

    def augment(self, message: str) -> str:
        pirate_words = {
            "fix": "fix tha blasted",
            "code": "yer code",
            "error": "mistake o' the sea",
            "add": "add 'em",
            "remove": "plunder",
            "pointer": "pointy thing"
        }
        return " ".join(pirate_words.get(word.lower(), word) for word in message.split())