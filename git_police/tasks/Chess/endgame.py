import chess
import pandas as pd
import tkinter as tk
from tkinter import ttk
import chess.svg
import io
from cairosvg import svg2png
from PIL import Image, ImageTk
import time

class ChessBoardWindow:
    def __init__(self, data):
        self.flag = False
        self.data = data.sample().iloc[0]
        self.board = chess.Board(self.data["FEN"])
        self.moves = self.data["Moves"]
        self.time_left = 90
        self.start_time = time.time()
        self.window = tk.Tk()
        self.window.title("Chess Puzzle")
        
        # Center the window on the screen
        window_width = 500
        window_height = 600
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        position_top = 0
        position_right = int(screen_width / 2 - window_width / 2)
        self.window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        
        self.top_frame = ttk.Frame(self.window)
        self.top_frame.pack(fill=tk.X, pady=5)
                
        self.timer_label = ttk.Label(self.top_frame, text=f"{self.time_left}", font=("Helvetica", 14))
        self.timer_label.pack(side=tk.TOP, padx=10)
        
        self.board_image_label = ttk.Label(self.window)
        self.board_image_label.pack(padx=10, pady=10)
        
        self.status = ttk.Label(self.window, text=self.data["Result"], font=("Helvetica", 14))
        self.status.pack(pady=5)
        
        self.move_frame = ttk.Frame(self.window)
        self.move_frame.pack(pady=5)
        
        self.move_entry = ttk.Entry(self.move_frame, font=("Helvetica", 14), width=20)
        self.move_entry.pack(side=tk.LEFT, padx=5)
        self.move_entry.bind('<Return>', self.on_move_entered)
        
        self.submit_button = ttk.Button(self.move_frame, text="Submit", command=self.on_move_entered)
        self.submit_button.pack(side=tk.LEFT, padx=5)
        
        self.message_label = ttk.Label(self.window, text="Enter move of both sides", foreground="black", font=("Helvetica", 14))
        self.message_label.pack(pady=5)
        
        self.update_board()
        self.window.after(100, self.start_timer)  # Delay timer start
        self.window.protocol("WM_DELETE_WINDOW", self.prevent_close)
        self.window.mainloop()

        return self.flag
    
    def update_board(self):
        board_svg = chess.svg.board(self.board, coordinates=True)
        png_data = svg2png(bytestring=board_svg.encode('utf-8'))
        image_data = Image.open(io.BytesIO(png_data))
        self.board_photo = ImageTk.PhotoImage(image_data)
        self.board_image_label.config(image=self.board_photo)
    
    def on_move_entered(self, event=None):
        user_move = self.move_entry.get()
        if user_move != "":
            user_move = user_move.strip().lower().replace("/", " ").replace(";", " ").replace(",", " ")
        else:
            self.load_new_puzzle()
        print("Input:", user_move)
        correct_move = self.moves.lower()
        print("Ans:", correct_move)
        
        if user_move == correct_move:
            self.message_label.config(text="Correct move!", foreground="green")
            self.status.config(text="Congratulations! You win! Exiting in 2 seconds...")
            self.flag = True
            self.window.after(2000, self.window.destroy)
        else:
            self.message_label.config(text="Incorrect move. Loading new puzzle...", foreground="red")
            self.window.after(2000, self.load_new_puzzle)

    
    def load_new_puzzle(self):
        self.data = data.sample().iloc[0]
        self.board = chess.Board(self.data["FEN"])
        self.moves = self.data["Moves"]
        self.time_left = 90
        self.start_time = time.time()
        print(self.moves)
        self.update_board()
        self.status.config(text=self.data["Result"])
        self.move_entry.config(state='normal')
        self.move_entry.delete(0, tk.END)
        self.message_label.config(text="Enter move of both sides", foreground="black")
        self.start_time = time.time()
        self.window.after(100, self.start_timer)  # Delay timer start
    
    def start_timer(self):
        self.start_time = time.time()
        self.time_left = 90
        self.update_timer()
    
    def update_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        self.time_left = max(90 - elapsed_time, 0)
        self.timer_label.config(text=f"Time left: {self.time_left}")
        
        if self.time_left > 0:
            self.window.after(1000, self.update_timer)
        else:
            self.message_label.config(text="Time's up! Loading new puzzle...", foreground="red")
            self.window.after(2000, self.load_new_puzzle)
    
    def prevent_close(self):
        pass
"""
data = pd.read_csv("./puzzle_database.csv")
print(data.columns)  # Debugging line to print column names
# Main loop to load and display puzzles
flag = False
while not(flag):
    flag = ChessBoardWindow(data)
"""
