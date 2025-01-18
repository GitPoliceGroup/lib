import typer
from commands.hello import hello as commandhello
from commands.goodbye import goodbye as commandgoodbye

app = typer.Typer()

@app.command()
def hello(name: str):
    commandhello(name)

@app.command()
def goodbye(name: str, formal: bool = False):
    commandgoodbye(name, formal)
    

if __name__ == "__main__":
    app()
