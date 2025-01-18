"""
Classes and utilities evaluating if a given text contains a quote from a movie
the list of quotes are programmatically defined in star_wars_quotes.json
it will select a random quote from the list and check if the given text contains it
otherwise it will return a failure message
"""
import json
import random
from typing import List
from git.police.rules.core import Rule, RuleOutput

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