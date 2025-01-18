import typer
from git.police.rules import (
    Rule,
    check_haiku, check_cc, check_star_wars, check_palindrome, check_alternator, check_piglatin, check_happiness
)
from git.police.cli.utils.camera import start_camera
import random

app = typer.Typer()

methods: dict[str, Rule] = {
    "haiku": check_haiku,
    "cc": check_cc,
    "starwars": check_star_wars,
    "palindrome": check_palindrome,
    "alternator": check_alternator,
    "piglatin": check_piglatin,
    "happiness": check_happiness
}

options = list(methods.keys())

@app.command()
def start_cam():
    start_camera()

@app.command()
def haiku():
    message = input("Please enter your commit message: ")
    while not (output := check_haiku(message)).success:
        print("\n"+output.message)
        message = input("Please enter a new commit message: ")
    
    print("\n\n"+output.message)

@app.command()
def cc():
    message = input("Please enter your commit message: ")
    while not (output := check_cc(message)).success:
        print("\n"+output.message)
        message = input("Please enter a new commit message: ")
    
    print("\n\n"+output.message)

@app.command()
def starwars():
    message = input("Please enter your commit message: ")
    while not (output := check_star_wars(message)).success:
        print("\n"+output.message)
        message = input("Please enter a new commit message: ")
    
    print("\n\n"+output.message)

@app.command()
def palindrome():
    message = input("Please enter your commit message: ")
    while not (output := check_palindrome(message)).success:
        print("\n"+output.message)
        message = input("Please enter a new commit message: ")
    
    print("\n\n"+output.message)

@app.command()
def piglatin():
    message = input("Please enter your commit message: ")
    while not (output := check_piglatin(message)).success:
        print("\n"+output.message)
        message = input("Please enter a new commit message: ")
    
    print("\n\n"+output.message)

@app.command()
def alternator():
    message = input("Please enter your commit message: ")
    while not (output := check_alternator(message)).success:
        print("\n"+output.message)
        message = input("Please enter a new commit message: ")
    
    print("\n\n"+output.message)

@app.command()
def happiness():
    output = check_happiness()
    print(output)
    
    print("\n\n"+output.message)

@app.command()
def commit():
    print("Randomizing the rules to check for...")
    random.shuffle(options)
    
    n_rules = random.randint(0, 4)
    print("Identifying", n_rules, "rules...")
    
    rules = [methods[method] for method in options[:n_rules]]
    
    print("Found", n_rules, "rules...\n")
    
    message = input("Please enter your commit message: ")
    
    for rule in rules:
        print("Assessing your message against the", rule.name, "rule...")
        while not (output := rule(message)).success:
            print("\n"+output.message)
            message = input("Please enter a new commit message: ")
        
        print("\n\n"+output.message)
        print("Passed", rule.name, "successfully!\n\n")
    
    
    print("\n\nPassed all rules! Congratulations!")
    
    # actually handle the commit

if __name__ == "__main__":
    app()
