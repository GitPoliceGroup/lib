import typer
from git.police.cli.tools.hello import hello as commandhello
from git.police.cli.tools.goodbye import goodbye as commandgoodbye


app = typer.Typer()

@app.command()
def hello(name: str):
    commandhello(name)

@app.command()
def goodbye(name: str, formal: bool = False):
    commandgoodbye(name, formal)
    

if __name__ == "__main__":
    app()
