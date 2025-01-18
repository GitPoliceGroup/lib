from git import Repo as oldRepo
from pathlib import Path

class Repo(oldRepo):
    def __init__(self, path: str):
        current_path = Path(path)
        while not (current_path / ".git").exists():
            current_path = current_path.parent
        
        super().__init__(str(current_path))
    
    def get_commit_files(self):
        # Should inherit from git.Repo
        changedFiles = [item.a_path for item in self.index.diff('HEAD')]
        return changedFiles
    
    def get_changes_as_text(self):
        # Should inherit from git.Repo
        changedFiles = self.get_commit_files()
        changeText = ""

        for file in changedFiles:
            try:
                f = open(file, "r")
                changeText += file + "\n" + f.read() + "\n\n"
            except:
                print(f"failed to read File: {file}")

        return changeText

    def get_diffs_as_text(self):
        # Should inherit from git.Repo
        diffs = self.index.diff('HEAD', create_patch=True)
        diffText = ""

        for diff in diffs:
            diffText += diff.a_path + "\n" + diff.diff.decode("utf-8") + "\n\n"

        return diffText