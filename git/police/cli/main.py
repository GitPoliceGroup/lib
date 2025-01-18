import typer
from git.police.cli.tools.hello import hello as commandhello
from git.police.cli.tools.goodbye import goodbye as commandgoodbye
from git.police.cli.utils.camera import start_camera
from git.police.cli.tools.haiku import check_haiku as commandhaiku

app = typer.Typer()

@app.command()
def hello(name: str):
    commandhello(name)

@app.command()
def goodbye(name: str, formal: bool = False):
    commandgoodbye(name, formal)

@app.command()
def start_cam():
    start_camera()

@app.command()
def haiku(haiku: str):
    print(commandhaiku(haiku))
    return commandhaiku(haiku)

if __name__ == "__main__":
    app()
