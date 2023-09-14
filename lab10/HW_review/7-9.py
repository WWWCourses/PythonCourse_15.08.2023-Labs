# Да се принтира матрица N*N, където:
#
#   1   8   9  16
#   2   7  10  15
#   3   6  11  14
#   4   5  12  13

def print_matrix(m):
	rows = len(m)
	cols = len(m[0])
	print('*' *rows*3)

	for i in range(rows):
		for j in range(cols):
			print(f'{m[i][j]:^3}', end='')
		print()

	print('*'*rows*3)

def solution_without_lists_using_increments(n):
	''' Visualisations
		N = 3
			0     1    2
		0: 1+5   6+1   7
		1: 2+3   5+3   8
		2: 3+1   4+5   9

		N = 4
		 	1     2    3   	4
		1: 1+7 	8+1	 9+7 	16
		2: 2+5 	7+3	10+5	15
		3: 3+3 	6+5	11+3	14
		4: 4+1	5+7	12+1	13

		N=5
			1     2     3     4   5
		1: 1+9  10+1  11+9  20+1  21
		2: 2+7   9+3  12+7  19+3  22
		3: 3+5   8+5  13+5  18+5  23
		4: 4+3   7+7  14+3  17+7  24
		5: 5+1   6+9  15+1  16+9  25
	'''

	rows = cols = n
	odd_increment = 2*n-1
	even_increment = 1

	for i in range(1,rows+1):
		number=i

		for j in range(1, cols+1):
			print(f'{number:>3}', end=' ')
			number = number+odd_increment if j%2 else number+even_increment

		# set increments for next row:
		odd_increment-=2
		even_increment+=2

		print('')

def solution_without_lists_using_values(n):
	""" Visualisations

	  N = 4
 	 	1   2   3   4
		1: 1 	 8	 9 	16
		2: 2 	 7	10	15
		3: 3 	 6	11	14
		4: 4	 5	12	13

		j is odd  => val = (j-1) * n + i
		j is even => val = (j*n) - (i-1)

	  N = 5
	   	1   2   3   4   5
		1: 1  10  11  20  21
		2: 2   9  12  19  22
		3: 3   8  13  18  23
		4: 4   7  14  17  24
		5: 5   6  15  16  25
	"""
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			if j % 2:
				number = (j-1) * n + i
			else:
				number = (j*n) - (i-1)

			print(f'{number:>3}', end=' ')
		print()

def solution_with_transposed_matrix(n):
	# create "normal" matrix:
	m = [[j+1 for j in range(i*n,i*n + n)] for i in range(0,n)]
	# print_matrix(m)

	# create transposed matrix with placeholders:
	transposed = [[0 for _ in range(n)] for _ in range(n)]

	#
	for i in range(n):
		for j in range(n):
			if i%2==0:
				# even rows=>transpose row
				transposed[j][i] = m[i][j]
			else:
				# odd rows=>transpose reversed row
				transposed[n-j-1][i] = m[i][j]

	print_matrix(transposed)

def solution_with_matrix_indexes(n):
	""" Visualisations:

	  N=4 (indexes only)
		0,0  0,1  0,2  0,3
		1,0  1,1  1,2  1,3
		2,0  2,1  2,2  2,3
		3,0  3,1  3,2  3,3
	"""
	### create 0 matrix, N*N, fill with index values for easy debugging:
	m = [[ f'0' for j in range(n)] for i in range(n)]

	### fill with values:
	row_idx = col_idx = 0

	for num in range(1, n*n+1):
		# print(row_idx, col_idx, num)
		m[row_idx][col_idx] = num

		if col_idx%2==0:
			#row_idx=0,1,2,3
			if row_idx<n-1:
				row_idx+=1
			else:
				col_idx+=1
		else:
			#row_idx=3,2,1,0
			if row_idx>0:
				row_idx-=1
			else:
				col_idx+=1

	print_matrix(m)

# solution_without_lists_using_increments(4)
# solution_without_lists_using_values(4)
# solution_with_transposed_matrix(4)
solution_with_matrix_indexes(4)


