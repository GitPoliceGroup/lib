from git.police.rules.core import Rule, RuleOutput
from git.police.rules.quote.movie import *

class MovieRule(Rule):
    def __init__(self):
        super().__init__("MovieQuoteChecker", "Commit Message should be a Quote from Star Wars!")
        self.quotes = self.load_quotes()
    
    def load_quotes(self) -> List[str]:
        with open("star_wars_quotes.json") as f:
            quotes = json.load(f)
        return quotes
    
    def __call__(self, message: str) -> RuleOutput:
        quote = random.choice(self.quotes)
        
        if quote in message:
            return RuleOutput(
                success = True,
                message = f"Found the quote: {quote}"
            )
        
        return RuleOutput(
            success = False,
            message = f"Commit message needs to contain the quote: {quote}"
       )