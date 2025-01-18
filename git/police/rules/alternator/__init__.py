from git.police.rules.core import Rule, RuleOutput
import re

class AlternatorRule(Rule):
    def __init__(self):
        super().__init__("AlternatorChecker", "Commit Message should be with alternating uppercase and lowercase letters!")
    
    def __call__(self, message: str) -> RuleOutput:
        message = re.sub(r'[^a-zA-Z0-9]', '', message)

        for i in range(1, len(message)):
            if message[i].isupper() == message[i-1].isupper():
                return RuleOutput(
                    success = False,
                    message = "You need to submit a commit with alternating uppercase and lowercase letters!"
                )
        
        return RuleOutput(
            success = True,
            message = "Your commit message has alternating uppercase and lowercase letters!"
        )
