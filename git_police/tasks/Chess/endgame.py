import chess
import pandas as pd
import tkinter as tk
from tkinter import ttk

class ChessBoardWindow:
    def __init__(self, board, moves):
        self.board = board
        self.moves = moves
        self.current_move_index = 0
        self.window = tk.Tk()
        self.window.title("Chess Puzzle")
        
        self.canvas = tk.Canvas(self.window, width=400, height=400)
        self.canvas.pack(padx=10, pady=10)
        
        self.status = ttk.Label(self.window, text="Enter your move:")
        self.status.pack(pady=5)
        
        self.move_entry = ttk.Entry(self.window)
        self.move_entry.pack(pady=5)
        self.move_entry.bind('<Return>', self.on_move_entered)
        
        self.timer_label = ttk.Label(self.window, text="Time left: 30")
        self.timer_label.pack(pady=5)
        
        self.update_board()
        self.start_timer()
        self.window.protocol("WM_DELETE_WINDOW", self.prevent_close)
        self.window.mainloop()
    
    def update_board(self):
        self.canvas.delete("all")
        colors = ["#f0d9b5", "#b58863"]
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                self.canvas.create_rectangle(col * 50, row * 50, (col + 1) * 50, (row + 1) * 50, fill=color)
        
        piece_symbols = {
            'p': '♟', 'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚',
            'P': '♙', 'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔'
        }
        
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                symbol = piece_symbols[piece.symbol()]
                row, col = divmod(square, 8)
                x = col * 50 + 25
                y = (7 - row) * 50 + 25
                self.canvas.create_text(x, y, text=symbol, font=("Arial", 32))
    
    def on_move_entered(self, event):
        user_move = self.move_entry.get().strip().lower()
        correct_move = self.moves[self.current_move_index].lower()
        
        if user_move == correct_move:
            self.board.push_san(user_move)
            self.update_board()
            self.current_move_index += 1
            if self.current_move_index >= len(self.moves):
                self.status.config(text="Congratulations! You win!")
                self.window.after(2000, self.window.destroy)
            else:
                self.status.config(text="Thinking...")
                self.window.after(1000, self.make_computer_move)
        else:
            self.load_new_puzzle()
    
    def make_computer_move(self):
        self.board.push_san(self.moves[self.current_move_index])
        self.update_board()
        self.current_move_index += 1
        self.status.config(text="Enter your move:")
        self.move_entry.config(state='normal')
        self.move_entry.delete(0, tk.END)
        self.start_timer()
    
    def load_new_puzzle(self):
        data = pd.read_csv("git_police/tasks/Chess/puzzle_database.csv")
        random_puzzle = data.sample().iloc[0]
        self.board = chess.Board(random_puzzle['FEN'])
        self.moves = random_puzzle['Moves'].split()
        self.current_move_index = 0
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
            self.on_move_entered(None)
    
    def prevent_close(self):
        pass

data = pd.read_csv("git_police/tasks/Chess/puzzle_database.csv")
# Main loop to load and display puzzles
while True:
    random_puzzle = data.sample().iloc[0]
    board = chess.Board(random_puzzle['FEN'])
    moves = random_puzzle['Moves'].split()
    ChessBoardWindow(board, moves)
