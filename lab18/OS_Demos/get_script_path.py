import os

cwd = os.getcwd()

print(cwd)
print(__file__)
print(os.path.dirname(__file__))
print(os.path.abspath(os.path.dirname(__file__)))