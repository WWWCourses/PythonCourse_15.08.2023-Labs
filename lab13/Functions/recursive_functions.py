# ------------- Recursion Function  = function wich calls itself ------------- #

# fact(4) = 4*3*2*1

# fact(n) = n*fact(n-1)
# fact(1) = 1

def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)

print( fact(1) ) # 1
print( fact(4) ) # 24