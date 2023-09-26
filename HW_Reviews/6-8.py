# Задача 8. Да се принтира буквата A на екрана както е дадено по-долу:
#   ****
#  *    *
# *      *
# ********
# *      *
# *      *
# *      *

def print_letter_A_1(width):
    symbol = "*"
    top_symbols = width//2+1 if width%2 else width//2
    top_spaces = (width-top_symbols)//2
    top_rows = (width-top_symbols)//2
    bottom_rows = top_rows+1


    # Print top part
    print(' '*top_spaces + symbol*top_symbols)
    for i in range(top_rows):
        row_start_spaces = top_spaces - 1
        row_middle_spaces = top_symbols
        print(' '*row_start_spaces + '*' + ' '*row_middle_spaces + '*')

    # Print middle
    print('*'*width)

    # Print bottom
    for i in range(bottom_rows):
        bottom_row_spaces = width - 2
        print('*' + ' '*bottom_row_spaces + '*')




# Get user input for the width of the 'A'
width = int(input("Enter the width of the letter A: "))
print_letter_A_1(width)