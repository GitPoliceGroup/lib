import typer
from git.police.cli.tools.hello import hello
from git.police.cli.tools.goodbye import goodbye
from git.police.cli.tools.haiku import check_haiku

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

if __name__ == "__main__":
    app()
