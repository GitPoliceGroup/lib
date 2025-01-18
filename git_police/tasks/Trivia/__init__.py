import random
import time
from git_police.tasks.core import Task, TaskOutput

class Trivia:
    def __init__(self):
        self.questions = [
            {
                "question": "Circuits can be wired in parallel or ______?",
                "correct_answer": "Series",
                "fake_answers": ["Sequential", "Alternating", "Dynamic"]
            },
            {
                "question": "How many bits are in a nibble?",
                "correct_answer": "4",
                "fake_answers": ["8", "2", "6"]
            },
            {
                "question": "How many buttons (excluding the control pad) did the original NES controller have?",
                "correct_answer": "4",
                "fake_answers": ["6", "2", "3"]
            },
            {
                "question": "How many fighters are playable in 'Street Fighter II'?",
                "correct_answer": "8",
                "fake_answers": ["6", "10", "12"]
            },
            {
                "question": "In the 'Extreme Battle' mini-game in 'Resident Evil 2', what characters are selectable?",
                "correct_answer": "Claire, Leon, Ada, and Chris",
                "fake_answers": ["Jill, Barry, Carlos, and Wesker", "Leon, Hunk, Rebecca, and Sherry", "Ada, Jill, Claire, and Brad"]
            },
            {
                "question": "In the game Joust, what animal was your mount?",
                "correct_answer": "An Ostrich",
                "fake_answers": ["A Dragon", "A Horse", "A Griffin"]
            },
            {
                "question": "In the original Contra, what gun would \"S\" get you?",
                "correct_answer": "Spread Gun",
                "fake_answers": ["Sniper Rifle", "Shotgun", "Stun Gun"]
            },
            {
                "question": "In the Sonic the Hedgehog series, what serves as your energy?",
                "correct_answer": "Rings",
                "fake_answers": ["Coins", "Crystals", "Stars"]
            },
            {
                "question": "In which Mega Man game did Mega Man first gain the ability to charge up his shots?",
                "correct_answer": "Mega Man 4",
                "fake_answers": ["Mega Man 3", "Mega Man 5", "Mega Man X"]
            },
            {
                "question": "Linux is a clone of what operating system?",
                "correct_answer": "UNIX",
                "fake_answers": ["Windows", "MS-DOS", "MacOS"]
            },
            {
                "question": "Name the final boss from each Final Fantasy game (1-8, in that order).",
                "correct_answer": "Chaos, Emperor from Hell, Dark Cloud, Zeromus, Deathgyunos, Kefka, Sephiroth, and Ultimecia",
                "fake_answers": ["Chaos, Emperor, Cloud of Darkness, Zeromus, Golbez, Sephiroth, Kefka, Ultimecia", "Chaos, Garland, Cloud of Darkness, Zemus, Kefka, Sephiroth, Ultimecia, Sin", "Warrior, Zemus, Tiamat, Kefka, Sephiroth, Cloud of Darkness, Garland, Ultimecia"]
            },
            {
                "question": "On what non-Nintendo console can you find Zelda games?",
                "correct_answer": "Philips CD-I",
                "fake_answers": ["Sega Genesis", "Atari 2600", "Sony PlayStation"]
            },
            {
                "question": "Samus Aran is the femme-fatale of which series of games?",
                "correct_answer": "Metroid",
                "fake_answers": ["Halo", "Star Fox", "Mass Effect"]
            },
            {
                "question": "The Sega Genesis game about two lost aliens looking for their spaceship was called what?",
                "correct_answer": "ToeJam and Earl",
                "fake_answers": ["Earthworm Jim", "Vectorman", "Ristar"]
            },
            {
                "question": "What did the letters in ROB (the old NES peripheral) stand for?",
                "correct_answer": "Robotic Operating Buddy",
                "fake_answers": ["Remote Operated Bot", "Robot Optical Buddy", "Rotating Optical Bot"]
            },
            {
                "question": "What does 'IBM' stand for?",
                "correct_answer": "International Business Machines",
                "fake_answers": ["Independent Business Machines", "Integrated Binary Modules", "Information-Based Machines"]
            },
            {
                "question": "What does CR-ROM stand for?",
                "correct_answer": "Compact Disk Read Only Memory",
                "fake_answers": ["Computer Disk Read-Only Mode", "Compact Readable Optical Memory", "Compact Recording Optical Media"]
            },
            {
                "question": "What does LED stand for?",
                "correct_answer": "Light Emitting Diode",
                "fake_answers": ["Luminous Electrical Device", "Low Energy Display", "Light Energy Diode"]
            },
            {
                "question": "What does the 'x' mean when referring to the speed of a CD-rom (eg. 32x)?",
                "correct_answer": "Times (faster than standard speed)",
                "fake_answers": ["Transfer rate", "Extended capacity", "Multiplication factor"]
            },
            {
                "question": "What entertainment product did Nintendo make before entering the video game business?",
                "correct_answer": "Playing cards",
                "fake_answers": ["Board games", "Toy trains", "Pinball machines"]
            },
            {
                "question": "What is a \"koopa?\"",
                "correct_answer": "A turtle",
                "fake_answers": ["A dragon", "A lizard", "A crab"]
            }
        ]
    
    def generate(self):
        question = random.choice(self.questions)
        qn_list = question["fake_answers"]
        rn = random.randint(0, 3)
        qn_list.insert(rn, question["correct_answer"])

        print(question["question"])
        for i in range(4):
            print(f"{i+1}. {qn_list[i]}")

        while True:
            try:
                answer = int(input("Enter your answer (1-4): "))
                if answer < 1 or answer > 4:
                    print("Invalid input. Please enter a number between 1 and 4.")
                else:
                    if qn_list[answer - 1] == question["correct_answer"]:
                        print("Correct!")
                        break
                    else:
                        print(f"Incorrect.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")

        return True


class TriviaGenerator(Task):
    def __init__(self):
        super().__init__("TriviaGenerator", "TRIVIA TIME!")

    def __call__(self):
        trivia_agent = Trivia()

        return trivia_agent.generate()