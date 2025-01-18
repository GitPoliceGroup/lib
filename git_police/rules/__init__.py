# git_police/rules/__init__.py

from git_police.rules.core import Rule, RuleOutput
from git_police.rules.cc import CCRule
from git_police.rules.haiku import HaikuRule
from git_police.rules.starwars import StarWarsRule
from git_police.rules.piglatin import PigLatinRule
from git_police.rules.palindrome import PalindromeRule
from git_police.rules.alternator import AlternatorRule

__all__ = [
    "Rule", "RuleOutput",
    "check_cc",
    "check_haiku",
    "check_star_wars",
    "check_piglatin"
    "check_palindrome",
    "check_alternator",
    "check_happiness"
]

check_cc = CCRule()
check_haiku = HaikuRule()
check_star_wars = StarWarsRule()
check_piglatin = PigLatinRule()
check_palindrome = PalindromeRule()
check_alternator = AlternatorRule()
