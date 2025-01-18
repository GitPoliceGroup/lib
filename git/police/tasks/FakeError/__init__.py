import random
import time
from git.police.tasks.core import Task, TaskOutput

import csv, random

class FakeErrorGenerator:
    def __init__(self):
        self.file = "git/police/utils/scathing_code_reviews.csv"

    def generate(self):
        with open(self.file, 'r') as f:
            reader = csv.reader(f)
            comments = list(reader)
            random_comment = random.choice(comments)
            return random_comment[0]

class FakeErrorGenerator(Task):
    def __init__(self):
        super().__init__("FakeErrorGenerator", "Fatal Error\n")
        self.scathing_comment_generator = FakeErrorGenerator()
        
    def __call__(self):
        for i in range(10):
            time.sleep(2)
            print(self.scathing_comment_generator.generate())

        return True