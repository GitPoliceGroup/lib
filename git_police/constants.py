from pathlib import Path

def get_home_path():
    return str(Path.home() / ".git-police")