# --------------------------------- Open file -------------------------------- #
### Variant 1 - Not good:
# try:
# 	f = open('./test','r')

# 	content = f.read()
# 	print(content)
# 	content = f.read(4)
# 	print(content)
# except Exception as e:
# 	print('Error', e)
# finally:
# 	f.close()


### Variant 2:
# try:
# 	with open('testdhfjhfdjfd','r') as f:
# 		content = f.read()
# 		print(content)
# 		content = f.read(4)
# 		print(content)
# except FileNotFoundError as e:
# 	print('File not found')

# except Exception as e:
# 	print('Upps, something went wrong!', e)
# 	exit()

# ------------------------------ Read from file ------------------------------ #
### whole content or symbols
# with open('./test_in_cyr.txt','r', encoding='cp1251') as f:
# 	print(f.read())

### all lines in a list - not good for large files(2GB)
# with open('./test', 'r') as f:
# 	lines =  f.readlines()
# 	for line in lines:
# 		print(line.rstrip())

# print('*' * 50)

### all lines by a generator - good for large files
# with open('./test', 'r') as f:
# 	for line in f:
# 		print(line.rstrip())


###
# with open('./test', 'r') as f:
# 	print(f.readline())
# 	print(f.readline())

# ------------------------------ Write in Files ------------------------------ #
# 'w' => truncate entire file
# 'x' => Error, if file exists
with open('./test2.txt', 'w') as f:
	# write whole string into file
	f.write("""Line1
		 Line 2
		 Line 3""")


data = ['Ivan', 'Asen', 'Pesho']
with open('./persons.txt', 'w') as f:
	f.writelines([el+'\n' for el in data])


# ---------------- Example : copy picture with read and write ---------------- #
# with open('./images/calculator.png', 'rb') as rf:
# 	with open('./images/calculator_copy.png', 'wb') as wf:
# 		content = rf.read()
# 		wf.write(content)





