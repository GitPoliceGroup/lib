import typer
from git.police.rules import (
    check_haiku, check_cc, check_movie_quote
)
from git.police.cli.utils.camera import start_camera

app = typer.Typer()

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

if __name__ == "__main__":
    app()
