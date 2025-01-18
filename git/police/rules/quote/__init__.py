from git.police.rules.core import Rule, RuleOutput
from git.police.rules.quote.movie import *

class MovieRule(Rule):
    def __init__(self):
        super().__init__("MovieQuoteChecker", "Commit Message should be a Quote from Star Wars!")
    
    def __call__(self, message: str) -> RuleOutput:
        # below is a list of Haiku objects
        haikus = HaikuText(message).get_haikus()
        
        if len(haikus) > 0:
            return RuleOutput(
                success = True,
                message = f"Found {len(haikus)} Haikus!"
            )
        
        return RuleOutput(
            success = False,
            message = "You need to submit a Haiku to create a commit!"
        )