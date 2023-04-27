from utils import morse_code_dict, logo, ask_to_continue

print(logo)
running = ask_to_continue('Begin? (Y/N): ')
while running:
    text_input = input('Enter text to convert to morse code:\n').upper().strip()

    morse_code_output = ''
    for char in text_input:
        if char in morse_code_dict.keys():
            morse_code_output += morse_code_dict[char]
    print(f'Morse code:')
    print(morse_code_output.rstrip())
    running = ask_to_continue('\nConvert again? (Y/N): ')
