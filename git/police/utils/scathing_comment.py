import csv, random

class ScathingCommentGenerator:
    def __init__(self):
        self.file = "git/police/utils/scathing_code_reviews.csv"

    

    def generate(self):
        with open(self.file, 'r') as f:
            reader = csv.reader(f)
            comments = list(reader)
            random_comment = random.choice(comments)
            return random_comment[0]

if __name__ == "__main__":
    scathing_comment_generator = ScathingCommentGenerator()
    print(scathing_comment_generator.generate())
