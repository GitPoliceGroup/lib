import typer
from git.police.cli.tools.haiku import check_haiku
from git.police.cli.tools.conventional_commits import check_cc
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
def conventional_commits():
    message = input("Please enter your commit message: ")
    while not (output := check_cc(message)).success:
        print("\n"+output.message)
        message = input("Please enter a new commit message: ")
    
    print("\n\n"+output.message)

if __name__ == "__main__":
    app()
