def print_letter_A(width):
    if width < 3 or width % 2 == 0:
        print("Width must be an odd number greater than or equal to 3.")
        return

    middle = width // 2
    for i in range(0, width):
        if i == 0:
            print(' ' * middle + '*' * (middle + 1))
        elif i == middle:
            print('*' * width)
        elif i < middle:
            spaces = ' ' * (middle - i)
            print(spaces + '*' + ' ' * (2 * i - 1) + '*' + spaces)
        else:
            spaces = ' ' * (i - middle)
            print(spaces + '*' + ' ' * (2 * (width - i) - 1) + '*' + spaces)

# Get user input for the width of the 'A'
width = int(input("Enter the width of the letter A: "))
print_letter_A(width)