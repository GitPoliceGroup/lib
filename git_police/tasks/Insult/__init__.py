import random
import time
from git_police.tasks.core import Task, TaskOutput

import csv, random

class ScathingCommentGenerator:
    def __init__(self):
        self.file = "git_police/utils/scathing_code_reviews.csv"

    def generate(self):
        with open(self.file, 'r') as f:
            reader = csv.reader(f)
            comments = list(reader)
            random_comment = random.choice(comments)
            return random_comment[0]

class Insultor(Task):
    def __init__(self):
        super().__init__("Insultor", "I have to comment on your egregious code!")
        self.scathing_comment_generator = ScathingCommentGenerator()
        
    def __call__(self):
        for i in range(10):
            time.sleep(2)
            print(self.scathing_comment_generator.generate())

        return True

if __name__ == "__main__":
    i = Insultor()
    i()