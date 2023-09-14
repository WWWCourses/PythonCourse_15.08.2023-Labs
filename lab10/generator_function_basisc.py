### Normal Function
# def normal_function():
# 	while True:
# 		return 2



# # function call
# res = normal_function()
# print(res)

# # for el in normal_function(): # Error
# # 	print(el)

### Generator function
def num_generator(start, stop):
	print('Generator is called')
	num = start
	while True:
		if num<stop:
			yield num
			num+=1

num_gen = num_generator(1,10)



for el in num_generator(1,10):
	print(el)







