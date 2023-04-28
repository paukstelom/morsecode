from utils import morse_code_dict


def converter(text_input: str) -> list:
    """ Takes string of plain text and returns a list of morse code """
    morse_code_output = []
    for char in text_input:
        if char in morse_code_dict.keys():
            morse_code_output.extend(morse_code_dict[char])
            morse_code_output.append('3 Units')
            if char == ' ':
                morse_code_output.pop(-1)
                morse_code_output.pop(-2)
    return morse_code_output
