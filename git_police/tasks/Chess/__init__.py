import chess
import pandas as pd
import tkinter as tk
import random

from git_police.tasks.core import Task, TaskOutput

class ChessPuzzleTask(Task):
    def __init__(self):
        data = pd.read_csv("./puzzle_database.csv")
        ChessBoardWindow(data)
    return True

# class ChessPuzzleTask(Task):
#     def __init__(self):
#         super().__init__(
#             name="Chess Puzzle",
#             description="Solve the chess puzzle by entering the correct moves in algebraic notation"
#         )
#         self.puzzle_solved = False

#     def __call__(self):
#         data = pd.read_csv("git_police/tasks/Chess/puzzle_database.csv")
#         random_puzzle = data.sample(n=1).iloc[0]
#         board = chess.Board(random_puzzle['FEN'])
#         moves = random_puzzle['Moves'].split()
        
#         window = ChessBoardWindow(board, moves, self)
#         return TaskOutput(success=self.puzzle_solved)

# class ChessBoardWindow:
#     def __init__(self, board, moves, task):
#         self.board = board
#         self.moves = moves
#         self.task = task
#         self.current_move_index = 0
#         self.window = tk.Tk()
#         self.window.title("Chess Puzzle")
        
#         # Create a text widget for displaying ASCII board
#         self.board_display = tk.Text(self.window, height=15, width=40, font=('Courier', 14))
#         self.board_display.pack(padx=10, pady=10)
        
#         # Create status label, input field, and timer
#         self.status = tk.Label(self.window, text="Enter your move:")
#         self.status.pack(pady=5)
        
#         self.move_entry = tk.Entry(self.window)
#         self.move_entry.pack(pady=5)
#         self.move_entry.bind('<Return>', self.on_move_entered)
        
#         self.timer_label = tk.Label(self.window, text="Time left: 30")
#         self.timer_label.pack(pady=5)
        
#         self.update_board()
#         self.start_timer()
#         self.window.protocol("WM_DELETE_WINDOW", self.prevent_close)
#         self.window.mainloop()
    
#     def update_board(self):
#         self.board_display.delete('1.0', tk.END)
#         self.board_display.insert('1.0', str(self.board))
    
#     def on_move_entered(self, event):
#         user_move = self.move_entry.get().strip().lower()
#         correct_move = self.moves[self.current_move_index].lower()
        
#         if user_move == correct_move:
#             self.board.push_san(user_move)
#             self.update_board()
#             self.current_move_index += 1
            
#             if self.current_move_index >= len(self.moves):
#                 self.status.config(text="Congratulations! You win!")
#                 self.task.puzzle_solved = True
#                 self.window.after(2000, self.window.destroy)
#             else:
#                 self.status.config(text="Thinking...")
#                 self.move_entry.config(state='disabled')
#                 self.window.after(1000, self.make_computer_move)
#         else:
#             self.load_new_puzzle()
    
#     def make_computer_move(self):
#         self.board.push_san(self.moves[self.current_move_index])
#         self.update_board()
#         self.current_move_index += 1
        
#         self.status.config(text="Enter your move:")
#         self.move_entry.config(state='normal')
#         self.move_entry.delete(0, tk.END)
#         self.start_timer()
    
#     def load_new_puzzle(self):
#         data = pd.read_csv("git_police/tasks/Chess/puzzle_database.csv")
#         random_puzzle = data.sample(n=1).iloc[0]
#         self.board = chess.Board(random_puzzle['FEN'])
#         self.moves = random_puzzle['Moves'].split()
#         self.current_move_index = 0
        
#         self.update_board()
#         self.status.config(text="Enter your move:")
#         self.move_entry.config(state='normal')
#         self.move_entry.delete(0, tk.END)
#         self.start_timer()
    
#     def start_timer(self):
#         self.time_left = 30
#         self.update_timer()
    
#     def update_timer(self):
#         if self.time_left > 0:
#             self.timer_label.config(text=f"Time left: {self.time_left}")
#             self.time_left -= 1
#             self.window.after(1000, self.update_timer)
#         else:
#             self.on_move_entered(None)
    
#     def prevent_close(self):
#         pass

# if __name__ == "__main__":
#     print("Running ChessPuzzleTask...")
#     task = ChessPuzzleTask()
#     print("Loaded")
#     task()
