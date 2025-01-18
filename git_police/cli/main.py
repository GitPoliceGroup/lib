import typer
import nltk
import ssl
import subprocess
import time
import sys
from contextlib import redirect_stdout

ssl._create_default_https_context = ssl._create_unverified_context

# Suppress nltk.download output
with open('/dev/null', 'w') as fnull:
    with redirect_stdout(fnull):
        nltk.download('cmudict', quiet=True)


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
def commit(
    message: str = typer.Option("", "--message", "-m", help="Commit message"),
    all: bool = typer.Option(False, "--all", "-a", help="Stage all changes"),
    interactive: bool = typer.Option(False, "--interactive", help="Interactive staging"),
    patch: bool = typer.Option(False, "--patch", help="Select hunks interactively"),
    amend: bool = typer.Option(False, "--amend", help="Amend the last commit"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Show what would be done"),
    no_verify: bool = typer.Option(False, "--no-verify", help="Bypass pre-commit hooks"),
):

    # Randomized Selector
    # Rule Phase, change k for number of rules to implement

    rule_options = list(rule_list.keys())
    rules_implemented = random.sample(rule_options, k=4)

    # Augmentation Phase
    augmenter_options = list(augmenter_list.keys())
    augmenters_implemented = random.sample(augmenter_options, k=3)

    # Background Phase
    background_options = list(background_list.keys())
    background_implemented = random.sample(background_options, k=1)

    # Task Phase
    task_options = list(task_list.keys())
    task_implemented = random.sample(task_options, k=2)

    # Print route map?
    print()
    print("Due to prior complaints about your commit comments, you will now have to meet the following requirements before commiting: ")
    for item in rules_implemented + augmenters_implemented + background_implemented + task_implemented:
        print(item)
    print()
    print()
    # Rudimentary Executor
    # Not sure how exactly we plan to implement this yet

    # Commit Message Loop
    for background in background_implemented:
        background_list[background]()

    # Commit Message Rule Loop
    # The external while loop is to enforce that they pass all test cases, else they go all the way back! :>
    # CC:    feat(auth): add login functionality

    # Skip_here added for testing purposes

    skip_here = True

    if(not skip_here):
        passed = False
        newmessage = ""
        while (not passed):
            # This loop is the cascading loops that enforce each individual rule
            for rule in rules_implemented:
                test_pass = rule_list[rule](message)
                while(test_pass.success == False):
                    print(test_pass.message)
                    newmessage = input("Please edit your commit message: ")
                    
                    test_pass = rule_list[rule](newmessage)

            passed = True

            # Commented out as might be impossible

            # for rule in rules_implemented:
            #     test_pass = rule_list[rule](message)
            #     if(test_pass.success == False):
            #         passed = False
        message = newmessage

        print("Congrats! You have passed this part")

    skip_here = True
                
    if(not skip_here):
        # Running Augmentors
        print("WARNING: Style issues detected...")
        print("Automatically fixing commit messages...")
        for augmenter in augmenters_implemented:
            print(f"\nApplying {augmenter} ...")

            message = augmenter_list[augmenter]().augment(message)
            print(f"New Message: {message}")
            time.sleep(2)


    skip_here = False
    
    if(not skip_here):
    # Running Tasks
        for task in task_implemented:
            # print(f"\nRunning {task}...") The task will handle its own printing
            passed = task_list[task]()
            while(not passed):
                print("\nYou failed the task!")
                passed = task_list[task]()

    print("\nYou have passed all the tests! You may now commit!\n")
    # Construct git commit command
    git_command = ["git", "commit"]
    if message:
        git_command += ["-m", message]
    if all:
        git_command.append("-a")
    if interactive:
        git_command.append("--interactive")
    if patch:
        git_command.append("--patch")
    if amend:
        git_command.append("--amend")
    if dry_run:
        git_command.append("--dry-run")
    if no_verify:
        git_command.append("--no-verify")

    # Run the git commit command
    try:
        subprocess.run(git_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running git commit: {e}")


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
