"""
Classes and utilities evaluating if a given text contains a quote from a movie
the list of quotes are programmatically defined in star_wars_quotes.json
it will select a random quote from the list and check if the given text contains it
otherwise it will return a failure message
"""
import json
import random
from git.police.rules.core import Rule, RuleOutput
import pathlib
import re

class StarWarsRule(Rule):
    def __init__(self):
        super().__init__("MovieQuoteChecker", "Commit Message should be a Quote from Star Wars!")
        self.quotes = self.load_quotes()
    
    def load_quotes(self) -> list[str]:
        with open(str(pathlib.Path(__file__).parent.resolve() / "star_wars_quotes.json")) as f:
            quotes = json.load(f)
        return quotes
    
    def format_text(self, text: str) -> str:
        return re.sub(r"\s\s+", "", re.sub(r"[^A-Za-z0-9 ]", "", text.lower()))
    
    def __call__(self, message: str) -> RuleOutput:
        for i in self.quotes:
            if self.format_text(i) in self.format_text(message):
                return RuleOutput(
                    success = True,
                    message = f"Found the quote: \"{i}\""
                )

        return RuleOutput(
            success = False,
            message = f"Commit message needs to contain a quote from Star Wars!"
       )