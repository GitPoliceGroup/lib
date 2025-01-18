from git.police.rules.core import Rule, RuleOutput
from git.police.rules.cc import CCRule
from git.police.rules.haiku import HaikuRule
from git.police.rules.quote import StarWarsRule

__all__ = [
    "Rule", "RuleOutput",
    "check_cc",
    "check_haiku",
    "check_star_wars"
]

check_cc = CCRule()
check_haiku = HaikuRule()
check_star_wars = StarWarsRule()