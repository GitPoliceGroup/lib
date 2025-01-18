from git_police.rules.core import Rule, RuleOutput
import re

class CCRule(Rule):
    def validate_and_split_commit(self, message):
        pattern = r"^(?P<type>build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test|¯\\_\(ツ\)_\/¯)(?P<scope>\(\w+\))?(?P<breaking>!)?(?P<subject>:\s.*)?|^(?P<merge>Merge \w+)"

        '''
        Group 0 (entire match): The entire matched string (i.e., the full commit message).
        Group 1 (type): The commit type (e.g., feat, fix).
        Group 2 (scope): The optional scope (e.g., (auth)).
        Group 3 (breaking): The optional breaking change marker (!).
        Group 4 (subject): The optional subject (e.g., : add login functionality).
        Group 5 (merge): Matches the "Merge <branch>" format.
        '''

        match = re.match(pattern, message)
        
        if match and match.group(0):
            return match
        else:
            return None

    def __init__(self):
        super().__init__("CC_Checker", "Commit Message should be adhere to Conventional Commits!")
    
    def __call__(self, message: str) -> RuleOutput:
        if self.validate_and_split_commit(message):
            return RuleOutput(
                success = True,
                message = f"Adheres to conventional commits!"
            )
        
        return RuleOutput(
            success = False,
            message = "You need to adhere to conventional commits!"
        )