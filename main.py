from morse_code_dict import morse_code_dict

running = True
while running:
    text_input = input('Enter text:\n').upper().strip()

    morse_code_output = ''
    for char in text_input:
        if char in morse_code_dict.keys():
            morse_code_output += morse_code_dict[char]
    print(morse_code_output.rstrip())

