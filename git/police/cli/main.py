import typer
from git.police.cli.tools.hello import hello
from git.police.cli.tools.goodbye import goodbye
from git.police.cli.tools.haiku import check_haiku
from git.police.cli.tools.haiku2 import check_haiku as check_haiku2
from git.police.cli.utils.camera import start_camera

app = typer.Typer()

@app.command()
def hello(name: str):
    hello(name)

@app.command()
def goodbye(name: str, formal: bool = False):
    goodbye(name, formal)

@app.command()
def start_cam():
    start_camera()

@app.command()
def haiku(haiku: str):
    print(check_haiku(haiku))
    return check_haiku(haiku)

@app.command()
def haikus():
    message = input("Please enter your commit message: ")
    while not (output := check_haiku2(message)).success:
        print("\n"+output.message)
        message = input("Please enter a new commit message: ")
    
    print("\n\n"+output.message)

if __name__ == "__main__":
    app()
