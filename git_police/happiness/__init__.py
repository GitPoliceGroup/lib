# git_police/happiness/__init__.py

from git_police.rules.core import Rule, RuleOutput

class HappinessChecker(Rule):
    def __init__(self):
        super().__init__("HappinessChecker", "You need to be happy!")
    
    def __call__(self) -> RuleOutput:
        from git_police.happiness.happiness import HappinessEnforcer
        # below is a list of Haiku objects
        print("Checking happiness...")
        try:
            test = HappinessEnforcer()
            answer = test.emotion_analysis()
                
            # return RuleOutput(
            #     success = True,
            #     message = f"You are happy!"
            # )
            return True
        except:
            return False
    
__all__ = [
    "HappinessChecker"
]