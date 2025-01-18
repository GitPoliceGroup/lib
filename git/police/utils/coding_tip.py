import random

class CodingTipGenerator:
    def __init__(self):
        self.file = "git/police/utils/coding_tips.txt"

    def generate(self):
        with open(self.file, 'r') as f:
            tips = f.readlines()
            random_tip = random.choice(tips)[:-2]
            return random_tip
    
if __name__ == "__main__":
    tip_generator = CodingTipGenerator()
    print(tip_generator.generate())