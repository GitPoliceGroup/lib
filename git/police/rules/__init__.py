from git.police.rules.core import Rule, RuleOutput
from git.police.rules.cc import CCRule
from git.police.rules.haiku import HaikuRule
from git.police.rules.starwars import StarWarsRule
from git.police.rules.piglatin import PigLatinRule
from git.police.rules.palindrome import PalindromeRule

__all__ = [
    "Rule", "RuleOutput",
    "check_cc",
    "check_haiku",
    "check_star_wars",
    "check_piglatin"
    "check_palindrome",
]

check_cc = CCRule()
check_haiku = HaikuRule()
check_star_wars = StarWarsRule()
check_piglatin = PigLatinRule()
check_palindrome = PalindromeRule()
