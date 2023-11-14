class Thread:
	def __init__(self, target, args) -> None:
		print('Now I\'ll start the thread')
		self.target = target

	def start(self):
		# print( self.target )
		self.target()



def work_hard(delay):
	print('work_hard')




tr1 = Thread(target=work_hard, args=(1000, ) )

tr1.start()







# def caller(target):
# 	print('I will call the target...')
# 	target()

# def foo():
# 	print('Foo')

# caller(target=foo())
# # caller(target=foo())
# # caller(target=5)
