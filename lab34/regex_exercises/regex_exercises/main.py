# ---------------------------------- TASK 1 ---------------------------------- #
import re

def is_valid_username(username):
    """Validate username based on specified criteria:

    Criteria:
            1. Username Length: 3 to 15 characters inclusive.
            2. Allowed Characters: Only alphanumeric characters, dashes (-), and underscores (_).
            3. Starting Character: Must start with a letter (either uppercase or lowercase).
            4. Ending Character: Must not end with an underscore or dash.

    Args:
            username (string)

    Return:
            bool: True if username match the given criteria, else: False
    """
    rx_str = r'''
        ^[A-Za-z]       # rule 3
        [\w-]{1,13}     # rule 1
        [A-Za-z0-9]$    # rule
    '''
    rx = re.compile(rx_str, re.VERBOSE)
    return bool(rx.search(username))

def custom_capitalization(input_str, letter):
    """ Capitalizes every word starting with a specific letter

    Args:
        string (string): input string,
        letter (string): word starting with letter to be capitalized
    Return:
        string: capitalized string
    """
    rx = re.compile(rf'^({letter}\w+)')

    words = input_str.split()
    capitalized_list = []

    for w in words:
        capitalized_w = rx.sub( lambda m: m.group(1).capitalize(), w)
        capitalized_list.append(capitalized_w)

    return ' '.join(capitalized_list)


def uppercase_I(input_str):
    # re.sub(pattern, repl, string)
    rx_i = re.compile(r'\bi\b')
    words_with_g = {
        'god': 'God',
        'george': 'George'
    }
    repl = 'I'
    res_i = rx_i.sub(repl, input_str)

    for key,value in words_with_g.items():
        print(key, value)
        res_i=res_i.replace(key, value)

    return res_i



if __name__ == "__main__":
    res = custom_capitalization('an apple a day keeps the doctor away', 'a')
    print(res)