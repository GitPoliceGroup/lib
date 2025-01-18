# git_police/augmenters/__init__.py

from git_police.augmenters.core import Augmenter

from git_police.augmenters.antonym import AntonymAugmenter
from git_police.augmenters.drunk_typing import DrunkTypingAugmenter
from git_police.augmenters.german import GermanAugmenter
from git_police.augmenters.pirate_speak import PirateAugmenter
from git_police.augmenters.yoda_speak import YodaSpeakAugmenter

__all__ = [
    "Augmenter",
    "AntonymAugmenter", "DrunkTypingAugmenter",
    "GermanAugmenter", "PirateAugmenter",
    "YodaSpeakAugmenter"
]