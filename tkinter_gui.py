import time
from tkinter import *

from utils import play_sound

UNIT = 0.1


class Display:

    def __init__(self, morse_code: list):
        self.morse_code = morse_code
        self.window = Tk()
        self.window.title('Morse Code')
        self.window.configure(background='black')
        self.window.config(width=600, height=600, padx=0, pady=0)
        self.canvas = Canvas(width=300, height=300, background='black')
        self.dot = self.canvas.create_oval(150, 150, 150, 150, width=30, outline='black')
        self.window.after(1000, self.flash_code)
        self.canvas.pack()
        self.window.mainloop()

    def flash_code(self):
        for char in self.morse_code:
            time.sleep(UNIT)
            print(char)
            if char == '*':
                self.beep(length='short')
            elif char == '---':
                self.beep(length='long')
            elif char == '7 Units':
                time.sleep(7 * UNIT)
            elif char == '3 Units':
                time.sleep(3 * UNIT)

    def beep(self, length: str):
        self.turn_on()
        self.window.update()
        play_sound(length=length)
        if length == 'short':
            time.sleep(UNIT)
        else:
            time.sleep(UNIT * 3)
        self.turn_off()
        self.window.update()

    def turn_on(self):
        self.canvas.itemconfig(self.dot, outline='white')

    def turn_off(self):
        self.canvas.itemconfig(self.dot, outline='black')
