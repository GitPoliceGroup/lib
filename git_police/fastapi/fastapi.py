from fastapi import FastAPI
import random
from git_police.rules import (
    Rule,
    check_haiku, check_cc, check_star_wars, check_palindrome, check_alternator, check_piglatin,
)
from git_police.tasks import (coding_tips, insultor, fake_error, trivia_generator, chess_puzzle)
from git_police.augmenters import (AntonymAugmenter, DrunkTypingAugmenter, GermanAugmenter, PirateAugmenter, YodaSpeakAugmenter)
from git_police.happiness import HappinessChecker

rule_list = {
    "haiku": check_haiku,
    "conventional commits": check_cc,
    "starwars": check_star_wars,
    "palindrome": check_palindrome,
    "alternator": check_alternator,
    "piglatin": check_piglatin,
}

task_list = {
    "coding_tips": coding_tips,
    "insultor": insultor,
    "fake_error": fake_error,
    "trivia_generator": trivia_generator,
    "chess": chess_puzzle,
}

augmenter_list = {
    "antonym": AntonymAugmenter,
    "drunk_typing": DrunkTypingAugmenter,
    "german": GermanAugmenter,
    "pirate": PirateAugmenter,
    "yoda": YodaSpeakAugmenter,
}

# Create a FastAPI application
app = FastAPI()

@app.get("/random_n_rules")
def random_n_rules(n: int = 4):
    rule_options = list(rule_list.keys())
    rules_implemented = random.sample(rule_options, k=min(n, len(rule_options)))
    return {"array": rules_implemented}

@app.post("/check_rule")
def check_rule(name: str, message: str):
    if name not in rule_list:
        return {"success": False, "message": "Rule not found"}
    result = rule_list[name](message)
    return {
        "success": result.success,
        "message": result.message
    }

@app.get("/random_n_games")
def random_n_games(n: int = 2):
    task_options = list(task_list.keys())
    tasks_implemented = random.sample(task_options, k=min(n, len(task_options)))
    return {"array": tasks_implemented}

@app.post("/play_game")
def play_game(name: str):
    if name not in task_list:
        return {"success": False, "message": "Game not found"}
    result = task_list[name]()
    return {"success": result}

@app.get("/random_n_augs")
def random_n_augs(n: int = 3):
    augmenter_options = list(augmenter_list.keys())
    augmenters_implemented = random.sample(augmenter_options, k=min(n, len(augmenter_options)))
    return {"array": augmenters_implemented}

@app.post("/augment")
def augment(name: str, message: str):
    if name not in augmenter_list:
        return {"success": False, "message": "Augmenter not found"}
    augmented_message = augmenter_list[name]().augment(message)
    return {"success": True, "message": augmented_message}

@app.post("/play_emotion")
def play_emotion():
    happiness_checker = HappinessChecker()
    result = happiness_checker()
    return {"success": result}