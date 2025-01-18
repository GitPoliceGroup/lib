import chess
import chess.svg
import pandas as pd
import tkinter as tk
from tkinter import ttk
import random

class ChessBoardWindow:
    def __init__(self, board, moves):
        self.board = board
        self.moves = moves
        self.current_move_index = 0
        self.window = tk.Tk()
        self.window.title("Chess Puzzle")
        
        # Create a text widget for displaying ASCII board
        self.board_display = tk.Text(self.window, height=15, width=40, font=('Courier', 14))
        self.board_display.pack(padx=10, pady=10)
        
        # Create status label, input field, and timer
        self.status = tk.Label(self.window, text="Enter your move:")
        self.status.pack(pady=5)
        
        self.move_entry = tk.Entry(self.window)
        self.move_entry.pack(pady=5)
        self.move_entry.bind('<Return>', self.on_move_entered)
        
        self.timer_label = tk.Label(self.window, text="Time left: 30")
        self.timer_label.pack(pady=5)
        
        # Initialize board and start timer
        self.update_board()
        self.start_timer()
        
        # Prevent window closing
        self.window.protocol("WM_DELETE_WINDOW", self.prevent_close)
        self.window.mainloop()
    
    def update_board(self):
        # Update the chess board display using ASCII representation
        self.board_display.delete('1.0', tk.END)
        self.board_display.insert('1.0', str(self.board))
    
    def on_move_entered(self, event):
        user_move = self.move_entry.get().strip().lower()
        correct_move = self.moves[self.current_move_index].lower()
        
        if user_move == correct_move:
            # Make the user's move
            self.board.push_san(user_move)
            self.update_board()
            self.current_move_index += 1
            
            if self.current_move_index >= len(self.moves):
                # Puzzle completed
                self.status.config(text="Congratulations! You win!")
                self.window.after(2000, self.window.destroy)
            else:
                # Computer's turn
                self.status.config(text="Thinking...")
                self.move_entry.config(state='disabled')
                self.window.after(1000, self.make_computer_move)
        else:
            # Wrong move, load new puzzle
            self.load_new_puzzle()
    
    def make_computer_move(self):
        # Make computer's move
        self.board.push_san(self.moves[self.current_move_index])
        self.update_board()
        self.current_move_index += 1
        
        # Reset for user's turn
        self.status.config(text="Enter your move:")
        self.move_entry.config(state='normal')
        self.move_entry.delete(0, tk.END)
        self.start_timer()
    
    def load_new_puzzle(self):
        # Load a new random puzzle
        data = pd.read_csv("git_police/tasks/Chess/puzzle_database.csv")
        random_puzzle = data.sample(n=1).iloc[0]
        self.board = chess.Board(random_puzzle['FEN'])
        self.moves = random_puzzle['Moves'].split()
        self.current_move_index = 0
        
        # Reset the interface
        self.update_board()
        self.status.config(text="Enter your move:")
        self.move_entry.config(state='normal')
        self.move_entry.delete(0, tk.END)
        self.start_timer()
    
    def start_timer(self):
        self.time_left = 30
        self.update_timer()
    
    def update_timer(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Time left: {self.time_left}")
            self.time_left -= 1
            self.window.after(1000, self.update_timer)
        else:
            # Time's up, treat as wrong move
            self.on_move_entered(None)
    
    def prevent_close(self):
        # Prevent window from closing
        pass

# Main loop to load and display puzzles
data = pd.read_csv("git_police/tasks/Chess/puzzle_database.csv")
while True:
    random_puzzle = data.sample(n=1).iloc[0]
    board = chess.Board(random_puzzle['FEN'])
    moves = random_puzzle['Moves'].split()
    ChessBoardWindow(board, moves)