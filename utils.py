import os

os.environ['TERM'] = 'xterm'

logo = '''

 _______ _______ _     _ _______      _______  _____                         
    |    |______  \___/     |            |    |     |                        
    |    |______ _/   \_    |            |    |_____|                        
                                                                             
 _______  _____   ______ _______ _______      _______  _____  ______  _______
 |  |  | |     | |_____/ |______ |______      |       |     | |     \ |______
 |  |  | |_____| |    \_ ______| |______      |_____  |_____| |_____/ |______
                                                                             

'''


def clear_console():
    """Clears console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def ask_to_continue(output_text: str) -> bool:
    """ Takes Y or N string input and returns bool value """
    print(output_text)
    while True:
        user_input = input()
        if user_input.capitalize() == 'Y':
            clear_console()
            return True
        elif user_input.capitalize() == 'N':
            clear_console()
            return False
        print('Invalid input')


morse_code_dict = {
    'A': '* ---   ',
    'B': '--- * * *   ',
    'C': '--- * --- *   ',
    'D': '--- * *   ',
    'E': '*   ',
    'F': '* * --- *   ',
    'G': '--- --- *   ',
    'H': '* * * *   ',
    'I': '* *   ',
    'J': '* --- --- ---   ',
    'K': '--- * ---   ',
    'L': '* --- * *   ',
    'M': '--- ---   ',
    'N': '--- *   ',
    'O': '--- --- ---   ',
    'P': '* --- --- *   ',
    'Q': '--- --- * ---   ',
    'R': '* --- *   ',
    'S': '* * *   ',
    'T': '---   ',
    'U': '* * ---   ',
    'V': '* * * ---   ',
    'W': '* --- ---   ',
    'X': '--- * * ---   ',
    'Y': '--- * --- ---   ',
    'Z': '--- --- * *   ',
    '1': '* --- --- --- ---   ',
    '2': '* * --- --- ---   ',
    '3': '* * * --- ---   ',
    '4': '* * * * ---   ',
    '5': '* * * * *   ',
    '6': '--- * * * *   ',
    '7': '--- --- * * *   ',
    '8': '--- --- --- * *   ',
    '9': '--- --- --- --- *   ',
    '0': '--- --- --- --- ---   ',
    ' ': '    '
}
