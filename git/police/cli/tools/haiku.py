from git.police.rules.haiku import HaikuRule

def check_haiku(message: str):
    rule = HaikuRule()
    
    result = rule(message)
    return result
