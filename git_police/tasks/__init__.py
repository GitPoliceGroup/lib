# git_police/tasks/__init__.py

from git_police.tasks.core import Task, TaskOutput

from git_police.tasks.CodingTips import CodingTipGenerator
from git_police.tasks.Insult import Insultor
from git_police.tasks.FakeError import FakeError
from git_police.tasks.Trivia import TriviaGenerator
from git_police.tasks.Chess import ChessPuzzleTask

coding_tips = CodingTipGenerator()
insultor = Insultor()
fake_error = FakeError()
trivia_generator = TriviaGenerator()
chess_puzzle = ChessPuzzleTask()

__all__ = [
    "Task", "TaskOutput",
    "coding_tips",
    "insultor",
    "fake_error",
    "trivia_generator",
    "chess_puzzle"
]