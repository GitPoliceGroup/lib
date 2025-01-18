import random
import time
from git_police.tasks.core import Task, TaskOutput

import csv, random

class FakeErrorGenerator:
    def __init__(self):
        self.file = "git_police/utils/git_error.csv"

    def generate(self):
        with open(self.file, 'r') as f:
            reader = csv.reader(f)
            comments = list(reader)
            random_comment = random.choice(comments)
            return '\n'.join(random_comment)

class FakeError(Task):
    def __init__(self):
        super().__init__("FakeErrorGenerator", "Fatal Error\n")
        self.generator = FakeErrorGenerator()
        
    def __call__(self):


        for i in range(10):
            time.sleep(4)
            print()
            print(self.generator.generate())
            print("Are you sure you want to continue (Y/N):")
            time.sleep(1)
            print("Y")

        return True

if __name__ == "__main__":
    fake_error_generator = FakeError()
    fake_error_generator()