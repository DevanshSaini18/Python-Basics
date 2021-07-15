class SlowMatrix:

	## The constructor
	# @param matrix A 2d Python list containing data
	def __init__(self, matrix):
		self.matrix = matrix

	## Matrix multiplication
	# @param self SlowMatrix1
	# @param mat2 SlowMatrix2
	def __matmul__(self, mat2):
		row1,col1 = len(self.matrix),len(self.matrix[0])
		row2,col2 = len(mat2.matrix),len(mat2.matrix[0])
		result = []
		if col1!=row2:
			print("Operation not possible")
			return
		else:
			for i in range(row1):
				li = []
				for k in range(col2):
					sum_of_ele = 0
					for j in range(col1):
						sum_of_ele = sum_of_ele + self.matrix[i][j]*mat2.matrix[j][k]
					li.append(sum_of_ele)
				result.append(li)
		return SlowMatrix(result)

	## Element wise multiplication
	# @param self SlowMatrix1
	# @param mat2 SlowMatrix2
	def __mul__(self, mat2):
		row1,col1 = len(self.matrix),len(self.matrix[0])
		row2,col2 = len(mat2.matrix),len(mat2.matrix[0])
		result = []
		if row1!=row2 or col1 != col2:
			print("Operation not possible, Dimensions found diffrent")
			return
		else:
			for i in range(row1):
				li = []
				for j in range(col1):
					li.append(self.matrix[i][j]*mat2.matrix[i][j])
				result.append(li)
		return SlowMatrix(result)

	## Element wise addition
	# @param self SlowMatrix1
	# @param mat2 SlowMatrix2
	def __add__(self, mat2):
		row1,col1 = len(self.matrix),len(self.matrix[0])
		row2,col2 = len(mat2.matrix),len(mat2.matrix[0])
		result = []
		if row1!=row2 or col1 != col2:
			print("Operation not possible, Dimensions found diffrent")
			return
		else:
			for i in range(row1):
				li = []
				for j in range(col1):
					li.append(self.matrix[i][j]+mat2.matrix[i][j])
				result.append(li)
		return SlowMatrix(result)

	## Element wise subtraction
	# @param self SlowMatrix1
	# @param mat2 SlowMatrix2
	def __sub__(self, mat2):
		row1,col1 = len(self.matrix),len(self.matrix[0])
		row2,col2 = len(mat2.matrix),len(mat2.matrix[0])
		result = []
		if row1!=row2 or col1 != col2:
			print("Operation not possible, Dimensions found diffrent")
			return
		else:
			for i in range(row1):
				li = []
				for j in range(col1):
					li.append(self.matrix[i][j]-mat2.matrix[i][j])
				result.append(li)
		return SlowMatrix(result)


	## Equality operator
	# @param self SlowMatrix1
	# @param mat2 SlowMatrix2
	def __eq__(self, mat2):
		same = True
		row1,col1 = len(self.matrix),len(self.matrix[0])
		row2,col2 = len(mat2.matrix),len(mat2.matrix[0])
		if row1!=row2 or col1!=col2:
			same = False
		else:
			for i in range(row1):
				for j in range(col1):
					same = same and (self.matrix[i][j]==mat2.matrix[i][j])
					if same == 0:
						break
				if same == 0:
					break;
		return same


	## Calculate transpose
	def transpose(self):
		result = []
		row,col = len(self.matrix),len(self.matrix[0])
		for j in range(col):
			li = []
			for i in range(row):
				li.append(self.matrix[i][j])
			result.append(li)
		return SlowMatrix(result)

	## Creates a SlowMatrix of 1s
	# @param shape A python pair (row, col)
	def ones(shape):
		result = []
		row,col = shape
		for j in range(col):
			li = []
			for i in range(row):
				li.append(1)
			result.append(li)
		obj = SlowMatrix(result)
		return obj

	## Creates a SlowMatrix of 0s
	# @param shape A python pair (row, col)
	def zeros(shape):
		result = []
		row,col = shape
		for j in range(col):
			li = []
			for i in range(row):
				li.append(0)
			result.append(li)
		obj = SlowMatrix(result)
		return obj

	## Returns i,jth element
	# @param key A python pair (i,j)
	def __getitem__(self, key):
		return (self.matrix)[key[0]][key[1]]

	## Sets i,jth element
	# @param key A python pair (i,j)
	# #param value Value to set
	def __setitem__(self, key, value):
		self.matrix[key[0]][key[1]] = value
		return

	## Converts SlowMatrix to a Python string
	def __str__(self):
		str1 = ""
		for r in self.matrix:
			for c in r:
				str1 = str1 + str(c) + " "
			str1 = str1 + "\n"
		return str1
