from pprint import pprint

def foo():
	x = 1
	y = 5
	print(f'x in foo: {x}')

def bar(x):
	x = 2
	print(f'x in bar: {x}')


x = 3
foo()
bar(9)
print(f'x in main: {x}')

pprint( globals() )