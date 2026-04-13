import tkinter as tk
import random

class GameApp:
    def __init__(self, master):
        self.master = master
        master.title("Games Site")

        self.label = tk.Label(master, text="Welcome to the Games Site!", font=('Helvetica', 16))
        self.label.pack(pady=20)

        self.menu_frame = tk.Frame(master)
        self.menu_frame.pack(pady=20)

        self.tic_tac_toe_button = tk.Button(self.menu_frame, text="Tic-Tac-Toe", command=self.play_tic_tac_toe)
        self.tic_tac_toe_button.grid(row=0, column=0, padx=10)

        self.number_guessing_button = tk.Button(self.menu_frame, text="Number Guessing Game", command=self.play_number_guessing)
        self.number_guessing_button.grid(row=0, column=1, padx=10)

    def play_tic_tac_toe(self):
        # Basic Tic-Tac-Toe game logic (Simplified)
        self.label.config(text="Playing Tic-Tac-Toe")
        # Here you would normally start the Tic-Tac-Toe game UI

    def play_number_guessing(self):
        self.label.config(text="Guess a number between 1 and 10!")
        self.secret_number = random.randint(1, 10)
        self.user_input = tk.Entry(self.master)
        self.user_input.pack(pady=10)
        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=10)

    def check_guess(self):
        guess = int(self.user_input.get())
        if guess < self.secret_number:
            self.label.config(text="Too low! Try again.")
        elif guess > self.secret_number:
            self.label.config(text="Too high! Try again.")
        else:
            self.label.config(text="Congratulations! You guessed it!")
            self.reset_game()

    def reset_game(self):
        self.user_input.delete(0, tk.END)
        self.submit_button.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()