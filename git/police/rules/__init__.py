from git.police.rules.cc import CCRule
from git.police.rules.haiku import HaikuRule
from git.police.rules.quote import MovieRule

__all__ = [
    "check_cc",
    "check_haiku"
]

check_cc = CCRule()
check_haiku = HaikuRule()
check_movie_quote = MovieRule()