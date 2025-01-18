import random
import time
from git_police.tasks.core import Task, TaskOutput

class CodingTipGenerator(Task):
    def __init__(self):
        super().__init__("CodingTipGenerator", "Im here to give you coding tips!")
        self.file = "git_police/utils/coding_tips.txt"

    def generate(self):
        with open(self.file, 'r') as f:
            tips = f.readlines()
            random_tip = random.choice(tips)[:-2]
            return random_tip
        
    def __call__(self):
        for i in range(10):
            time.sleep(2)
            print(self.generate())

        return True