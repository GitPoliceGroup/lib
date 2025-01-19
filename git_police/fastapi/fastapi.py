from fastapi import FastAPI
import random
from git_police.rules import (
    Rule,
    check_haiku, check_cc, check_star_wars, check_palindrome, check_alternator, check_piglatin,
)
from git_police.tasks import (coding_tips, insultor, fake_error, trivia_generator, chess_puzzle)
from git_police.augmenters import (AntonymAugmenter, DrunkTypingAugmenter, GermanAugmenter, PirateAugmenter, YodaSpeakAugmenter)
from git_police.happiness import HappinessChecker
from pydantic import BaseModel

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

class APIOutput(BaseModel):
    success: bool
    message: str | None = None

# Create a FastAPI application
app = FastAPI()

@app.get("/rules")
def random_n_rules() -> list[str]:
    n = random.randint(3, 5)
    rule_options = list(rule_list.keys())
    rules_implemented = random.sample(rule_options, k=min(n, len(rule_options)))
    return rules_implemented


@app.get("/check_rule")
def check_rule(rule: str, message: str) -> APIOutput:
    if rule not in rule_list:
        return BaseModel(**{"success": False, "message": "Rule not found"})
    result = rule_list[rule](message)
    return BaseModel({
        "success": result.success,
        "message": result.message
    })

@app.get("/games")
def random_n_games() -> list[str]:
    n = random.randint(1, 3)
    task_options = list(task_list.keys())
    tasks_implemented = random.sample(task_options, k=min(n, len(task_options)))
    return tasks_implemented

@app.get("/play_game")
def play_game(game: str):
    if game not in task_list:
        return {"success": False, "message": "Game not found"}
    result = task_list[game]()
    return {"success": result}

@app.get("/augs")
def random_n_augs():
    n = random.randint(1, 3)
    augmenter_options = list(augmenter_list.keys())
    augmenters_implemented = random.sample(augmenter_options, k=min(n, len(augmenter_options)))
    return augmenters_implemented

@app.get("/augment")
def augment(aug: str, message: str):
    if aug not in augmenter_list:
        return {"success": False, "message": "Augmenter not found"}
    augmented_message = augmenter_list[aug]().augment(message)
    return {"success": True, "message": augmented_message}

@app.post("/play_emotion")
def play_emotion():
    happiness_checker = HappinessChecker()
    result = happiness_checker()
    return {"success": result}