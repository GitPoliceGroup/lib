from git.police.rules.haiku import HaikuRule

def check_haiku(message: str):
    rule = HaikuRule()
    
    result = rule(message)
    return result

def check_movie_quote(message: str):
    rule = MovieRule()
    
    result = rule(message)
    return result