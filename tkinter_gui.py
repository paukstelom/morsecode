import time
from tkinter import *

UNIT = 0.4


class Display:

    def __init__(self, morse_code: str):
        self.morse_code = morse_code
        self.window = Tk()
        self.window.title('Morse Code')
        self.window.configure(background='black')
        self.window.config(width=600, height=600, padx=0, pady=0)
        self.canvas = Canvas(width=300, height=300, background='black')
        self.dot = self.canvas.create_oval(150, 150, 150, 150, width=30, outline='black')
        self.window.after(2000, self.flash_code)
        self.canvas.pack()
        self.window.mainloop()

    def flash_code(self):
        for char in self.morse_code:
            if char == ' ':
                self.turn_off()
                time.sleep(UNIT)
                self.window.update()
                print(char)
            else:
                self.turn_on()
                time.sleep(UNIT)
                self.window.update()
                print(char)
        self.turn_off()

    def turn_on(self):
        self.canvas.itemconfig(self.dot, outline='white')

    def turn_off(self):
        self.canvas.itemconfig(self.dot, outline='black')
