import tkinter as tk
from tkinter import messagebox
from random import randint

class NumberGuessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Number Guessing Game')
        self.root.geometry('350x250')
        self.guessnum = randint(1, 100)
        self.attempts = 0
        self.max_attempts = 10
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text='Guess the Number (1-100):', font=('Arial', 14)).pack(pady=10)
        self.entry = tk.Entry(self.root, font=('Arial', 14), justify='center')
        self.entry.pack(pady=5)
        self.entry.focus()
        self.feedback = tk.Label(self.root, text='', font=('Arial', 12))
        self.feedback.pack(pady=5)
        self.attempts_label = tk.Label(self.root, text='Attempts Made: 0 | Attempts Left: 10', font=('Arial', 10))
        self.attempts_label.pack(pady=5)
        self.submit_btn = tk.Button(self.root, text='Guess', font=('Arial', 12), command=self.check_guess)
        self.submit_btn.pack(pady=10)
        self.restart_btn = tk.Button(self.root, text='Restart', font=('Arial', 10), command=self.restart_game)
        self.restart_btn.pack(pady=5)
        self.root.bind('<Return>', lambda event: self.check_guess())

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            self.feedback.config(text='Please enter a valid number!')
            return
        guess = int(guess)
        self.attempts += 1
        if guess == self.guessnum:
            self.feedback.config(text='Correct! You guessed it!')
            self.end_game(win=True)
        elif guess < self.guessnum:
            self.feedback.config(text='Too low! Try again.')
        else:
            self.feedback.config(text='Too high! Try again.')
        self.attempts_label.config(text=f'Attempts Made: {self.attempts} | Attempts Left: {self.max_attempts - self.attempts}')
        if self.attempts >= self.max_attempts and guess != self.guessnum:
            self.end_game(win=False)
        self.entry.delete(0, tk.END)

    def end_game(self, win):
        if win:
            msg = f'Congratulations! You guessed the number {self.guessnum} in {self.attempts} attempts.'
        else:
            msg = f'Game Over! The number was {self.guessnum}.'
        messagebox.showinfo('Game Result', msg)
        self.submit_btn.config(state='disabled')
        self.entry.config(state='disabled')

    def restart_game(self):
        self.guessnum = randint(1, 100)
        self.attempts = 0
        self.feedback.config(text='')
        self.attempts_label.config(text=f'Attempts Made: 0 | Attempts Left: {self.max_attempts}')
        self.submit_btn.config(state='normal')
        self.entry.config(state='normal')
        self.entry.delete(0, tk.END)
        self.entry.focus()

if __name__ == '__main__':
    root = tk.Tk()
    app = NumberGuessingApp(root)
    root.mainloop()
