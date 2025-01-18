from git.police.rules.core import Rule, RuleOutput

class PalindromeRule(Rule):
    def __init__(self):
        super().__init__("PalindromeChecker", "Commit Message should be a Palindrome!")
    
    def __call__(self, message: str) -> RuleOutput:
        if message == message[::-1]:
            return RuleOutput(
                success = True,
                message = f"Your commit message is a palindrome!"
            )
        
        return RuleOutput(
            success = False,
            message = "You need to submit a palindrome to create a commit!"
        )