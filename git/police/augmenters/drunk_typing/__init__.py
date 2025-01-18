from git.police.augmenters.core import Augmenter
import random

class DrunkTypingAugmenter(Augmenter):
    def __init__(self):
        super().__init__("Drunk Typing", "Adds random typos and capitalization to the commit.")

    def augment(self, message: str) -> str:
        def drunkify(word):
            word = "".join(
                char.upper() if random.random() > 0.7 else char.lower()
                for char in word
            )
            if random.random() > 0.5:
                word = word + random.choice("asdfghjkl")
            return word

        return " ".join(drunkify(word) for word in message.split())