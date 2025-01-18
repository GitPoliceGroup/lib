# git_police/happiness/__init__.py

from git_police.rules.core import Rule, RuleOutput

class HappinessRule(Rule):
    def __init__(self):
        super().__init__("HappinessChecker", "You need to be happy!")
    
    def __call__(self) -> RuleOutput:
        from git_police.happiness.happiness import HappinessEnforcer
        # below is a list of Haiku objects
        test = HappinessEnforcer()
        while not test.emotion_analysis():
            print("You need to be happy!")
            
        return RuleOutput(
            success = True,
            message = f"You are happy!"
        )