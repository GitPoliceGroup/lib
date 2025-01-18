from git.police.rules.core import Rule, RuleOutput

class PigLatinRule(Rule):
    def __init__(self):
        super().__init__("PigLatinChecker", "Commit Message should be in Pig Latin!")
    
    def __call__(self, message: str) -> RuleOutput:
        words = message.split()
        for word in words:
            if not self.is_pig_latin(word):
                return RuleOutput(
                    success = False,
                    message = "Your commit message must be in Pig Latin!"
                )
        return RuleOutput(
            success = True,
            message = "Your commit message is in Pig Latin!"
        )
    
    def is_pig_latin(self, word: str) -> bool:
        vowels = "aeiou"
        if word[-2:] == "ay" and (word[:-2][0] in vowels or word[:-2][-1] in vowels):
            return True
        return False