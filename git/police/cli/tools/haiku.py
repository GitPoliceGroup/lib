from git.police.rules.haiku.haiku import *

def check_haiku(string: str):
    haikus = HaikuText(string).get_haikus()
    return len(haikus) == 1