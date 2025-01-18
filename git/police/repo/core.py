import git
from pathlib import Path

class Repo(git.Repo):
    def __init__(self, path: str):
        current_path = Path(path)
        while not (current_path / ".git").exists():
            current_path = current_path.parent
        
        super().__init__(str(current_path))
    
    def get_commit_files():
        pass