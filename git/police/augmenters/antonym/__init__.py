from git.police.augmenters.core import Augmenter
from nltk.corpus import wordnet

class AntonymAugmenter(Augmenter):
    def __init__(self):
        super().__init__("Opposite Meaning", "Changes each word in the commit message to its antonym.")

    def augment(self, message: str) -> str:
        def get_antonym(word):
            synsets = wordnet.synsets(word)
            for synset in synsets:
                for lemma in synset.lemmas():
                    if lemma.antonyms():
                        return lemma.antonyms()[0].name()
            return word  # Fallback to original word if no antonym is found

        return " ".join(get_antonym(word) for word in message.split())