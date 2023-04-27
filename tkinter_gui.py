from tkinter import *


class Display:

    def __init__(self, morse_code: str):
        self.window = Tk()
        self.window.title('Morse Code')
        self.window.configure(background='black')
        self.window.config(width=600, height=600, padx=0, pady=0)
        self.flash_code(morse_code)
        self.window.mainloop()

    def flash_code(self, morse_code: str):
        canvas = Canvas(width=300, height=300, bg='white')
        canvas.pack()
        dot = canvas.create_oval(150, 150, 150, 150, width=30, fill='green')
        for char in morse_code:
            pass
