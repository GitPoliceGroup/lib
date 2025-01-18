print('running main.py')

import typer
import nltk
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('cmudict')

# Add all augmenters
from  git_police.augmenters import (AntonymAugmenter, DrunkTypingAugmenter, GermanAugmenter, PirateAugmenter, YodaSpeakAugmenter)

# Add all rules
from git_police.rules import (
    Rule,
    check_haiku, check_cc, check_star_wars, check_palindrome, check_alternator, check_piglatin,
)

rule_list = {
    "haiku" : check_haiku,
    "cc" : check_cc,
    "starwars" : check_star_wars,
    "palindrome" : check_palindrome,
    "alternator" : check_alternator,
    "piglatin" : check_piglatin,
}

# Add happiness checker
from git_police.happiness import HappinessChecker

# Add all background tasks
from git_police.background import PublicShamingTask

background_list = {
    "public_shaming" : PublicShamingTask
}

# Add all tasks
from git_police.tasks import (coding_tips, insultor, fake_error, trivia_generator)

task_list = {
    "coding_tips" : coding_tips,
    "insultor" : insultor,
    "fake_error" : fake_error,
    "trivia_generator" : trivia_generator,
}

# Add all augmenters
from git_police.augmenters import (AntonymAugmenter, DrunkTypingAugmenter, GermanAugmenter, PirateAugmenter, YodaSpeakAugmenter)
augmenter_list = {
    "antonym" : AntonymAugmenter,
    "drunk_typing" : DrunkTypingAugmenter,
    "german" : GermanAugmenter,
    "pirate" : PirateAugmenter,
    "yoda" : YodaSpeakAugmenter,
}

import random, os

app = typer.Typer()

@app.command()
def commit():

    # print("Starting Commit")

    # Randomized Selector
    # Rule Phase, change k for number of rules to implement
    rule_options = list(rule_list.keys())
    rules_implemented = random.choices(rule_options, k=4)

    # Augmentation Phase
    augmenter_options = list(augmenter_list.keys())
    augmenters_implemented = random.choices(augmenter_options, k=3)

    # Background Phase
    background_options = list(background_list.keys())
    background_implemented = random.choices(background_options, k=1)

    # Task Phase
    task_options = list(task_list.keys())
    task_implemented = random.choices(task_options, k=2)

    print(rules_implemented, augmenters_implemented, background_implemented, task_implemented)


    # Rudimentary Executor
    # Not sure how exactly we plan to implement this yet
    for background in background_implemented:
        background_list[background]()

    for rule in rules_implemented:
        rule_list[rule]()
    
    for augmenter in augmenters_implemented:
        augmenter_list[augmenter]()

    for task in task_implemented:
        task_list[task]()


    # Run the rules (Not edited)
    
    # n_rules = random.randint(0, 4)
    # print("Identifying", n_rules, "rules...")
    
    # rules = [methods[method] for method in options[:n_rules]]
    
    # print("Found", n_rules, "rules...\n")
    
    # message = input("Please enter your commit message: ")
    
    # for rule in rules:
    #     print("Assessing your message against the", rule.name, "rule...")
    #     while not (output := rule(message)).success:
    #         print("\n"+output.message)
    #         message = input("Please enter a new commit message: ")
        
    #     print("\n\n"+output.message)
    #     print("Passed", rule.name, "successfully!\n\n")
    
    
    # print("\n\nPassed all rules! Congratulations!")
    
    # actually handle the commit

if __name__ == "__main__":
    app()
