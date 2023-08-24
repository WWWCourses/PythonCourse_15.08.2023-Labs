# ------------------------------ String Literal ------------------------------ #

# print('hi')
# print("hi")
# # multiline strings
# print("""
# hi
# againg
# """)
# print('''
# hi
# againg
# ''')



# --------------------------- Strings are immutable -------------------------- #
# user_name = 'ivan'
# x = user_name.upper()

# print(x)
# print(user_name)


# # RAM:
# # 	str1=> 0x265:'hi'

# ----------------------------- Escape Sequences ----------------------------- #
# sentence = 'Tom\'s pub is the best!'
# print(sentence) # Tom's pub is the best!

# print('1. a\na')
# print('*'*30)
# print('2.a\ta')
# print('3.iv\ba')
# print('4.\'')
# print('5.\"')
# print('6.\\')
# print("""Line 1
# Line 2
# Line 3""")
# print("\n")
# print('Line1\nLine2\nLine3')

# print('\N{SNAKE}')

# ---------------------------- Strings Operations ---------------------------- #
### Concatenation:
# user_name = 'Ada'
# user_surname  = 'Byron'

# user_full_name = user_name + ' ' + user_surname
# print( user_full_name )

# print( 3 + 3.14 )
# print( '3' + '3.14')  # '33.14'
# # print( '3' + 2 ) # Error

### Repetition
# print( '~8&' * 30)
# print( 30 * '~')

# ----------------------------- String Formating ----------------------------- #
### 1. with f strings

# print( f'{2}+{3}' ) # 2+3
# user_name = 'Ada'
# user_surname = 'Byron'

# print( f'Hello, {user_name} {user_surname}!' )
# Hello, Ada Byron!

# print( '2+3')
# print( f'{2+3}')
# print( f'2+3')


# TODO: make it work and explain
fruit = 'orange'
# print('|{:^10}|'.format(fruit))
# print(f'|{fruit:^10}|')
# print('abc'.center(9))
# print(f'{"abc":^9s}')


### 2. with format method:
# fruit = input('Enter fruit name: ')
# fruit = 'apple'

# # fruit_formated = "'"+fruit+"'"
# fruit_formated = "'{}'".format('iva')

# print(fruit_formated) # 'iva'
# print('{}+{}'.format(2,3)) # 2+3
# print('{} + {}'.format(2,3))

# fruit = 'orange'
# print('|{:<10}|'.format(fruit))
# print('|{:^10}|'.format(fruit))

### 3. with % - OLD VARIANT

# print('{}+{}'.format(2,3)) # 2+3
# print('%d+%d' % (2,3)) # 2+3

# fruit = 'orange'
# print( '|%.10s|' % (fruit) )



# ------------------------------ Strings Methods ----------------------------- #

### ''.title()
# str1 = 'ala bala a b c'
# str1 = str1.title()
# print( str1 )

# ### lower()
# print( 'ala BALA'.lower() )

### replace()
# str1 = 'ala bala a b c'
# # task: replace 'ala' with '@' in str1
# str1 = str1.replace('ala', '@', 1)
# print(str1)

### find()
# string indexing
# str1 = 'abc'
# print( str1[0] )
# print( str1[1] )


# str1 = 'abc'
# print( str1.find('a') )
# print( str1.find('y') )

# str.find(sub[, start[, end]])
# print( 'abc'.find('a') )
# print( 'abc'.find('a', ) )



### strip()
# print( '    abc 	'.strip() + '!')


### split()
# text = 'Sentence1.Sentence2.Sentence3'

# result = text.split('.')
# print(result)

# text = '1-2-3'
# print( text.split('-'))

### startswith():

# user_name = 'Iva'

# print( user_name.startswith()


### str.center(width[, fillchar])

# ### TODO: explain center
# print('abc dfe'.center(3))
# print('abc dfe'.center(3, '@'))

# print('abc'.center(9))
# print('abc'.center(9,'*'))











