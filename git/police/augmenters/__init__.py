from git.police.augmenters.core import Augmenter

from git.police.augmenters.antonym import AntonymAugmenter
from git.police.augmenters.drunk_typing import DrunkTypingAugmenter
from git.police.augmenters.german import GermanAugmenter
from git.police.augmenters.pirate_speak import PirateAugmenter
from git.police.augmenters.yoda_speak import YodaSpeakAugmenter

__all__ = [
    "Augmenter",
    "AntonymAugmenter", "DrunkTypingAugmenter",
    "GermanAugmenter", "PirateAugmenter",
    "YodaSpeakAugmenter"
]