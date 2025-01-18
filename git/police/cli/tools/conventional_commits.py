from git.police.rules.conventional_commits import CCRules

def check_cc(message: str):
    rule = CCRules()
    
    result = rule(message)
    return result
