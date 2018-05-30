class mathdojo(object):
	def __init__(self):
		self.equals=10
	def add(self,*x):
		# print x
		for j in x:
			if type(j)==list:
				# print j
				for k in j:
					# print k
					self.equals+=k
			if type(j)==int:
				self.equals+=j


		# 	print i
		# print self.equals
		return self
	def subtract(self,*w):
		# print w
		self.equals2=0
		for i in w:
			if type(i)==int:
				self.equals2+=i
			if type(i)==list:
				for l in i:
					# print l
					self.equals2+=l
		# print self.equals2

			# print i
		# print self.equals2
		self.equals=self.equals-self.equals2
		return self
	def result(self):
		print self.equals
	# def md(self):
	# 	mathdojo(self)
	# 	print self.equals
	# 	return self
	# def md():
	# 	print self.add


md= mathdojo()

# md.add(3,4)

# # md.add(2).add(2,5).subtract(3,2).result()

md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()


# md.add([1,2], 3,4).subtract(3,2).result()

# md.subtract([1,2,3],3,2)

# .subtract(2,1).subtract(2,1)