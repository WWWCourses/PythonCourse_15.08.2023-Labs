names = ["Ivan", "Alex", "Maria", "Angel", ""]

# With comprehensions:
a_names = [name for name in names if name.startswith('A')]
# With filter:
a_names = filter(lambda name: name.startswith('A'), names)
print(list(a_names))