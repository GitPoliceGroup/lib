import typer
from commands.hello import hello as commandhello
from commands.goodbye import goodbye as commandgoodbye
from utils.camera import start_camera

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

if __name__ == "__main__":
    app()
