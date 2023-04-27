from utils import logo, ask_to_continue
from engine import converter
from tkinter_gui import Display

print(logo)
running = ask_to_continue(output_text='Begin? (Y/N): ')
while running:
    text_input = input('Enter text to convert to morse code:\n').upper().strip()
    result = converter(text_input=text_input)
    print(f'Morse code:\n{result}')
    if ask_to_continue(output_text='Display the morse code? (Y/N): '):
        display = Display(morse_code=result)
    running = ask_to_continue(output_text='\nConvert again? (Y/N): ')

