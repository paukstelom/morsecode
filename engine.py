from utils import morse_code_dict


def converter(text_input: str) -> str:
    """ Takes string of plain text and returns string of morse code """
    morse_code_output = ''
    for char in text_input:
        if char in morse_code_dict.keys():
            morse_code_output += morse_code_dict[char]
    return morse_code_output.rstrip()
