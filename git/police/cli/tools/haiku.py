from git.police.cli.utils.haiku import *

def check_haiku(string: str):
    haikus = HaikuText(string).get_haikus()
    return haikus