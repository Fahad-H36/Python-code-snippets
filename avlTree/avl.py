

class AVLTree:
	# Constructor:
	def __init__(self,initval=None):
		self.value = initval
		if self.value:
			self.left = AVLTree()
			self.right = AVLTree()
			self.height = 1
		else:
			self.left = None
			self.right = None
			self.height = 0
		return

	def isempty(self):
		return (self.value == None)

	def isleaf(self):
		return (self.value != None and self.left == None and self.right == None)

	def getHeight(self):
		if not self:
			return 0

		return self.height

	def getBal(self):
		if not self:
			return 0
		if not self.isleaf():
			return self.left.getHeight() - self.right.getHeight()

	def insert(self, key):
		
			if self.isempty():
				self.value = key
				self.right = AVLTree()
				self.left = AVLTree()
				self.height = 1 				
				return self

			elif key < self.value:
				self.left = self.left.insert(key)
			else:
				self.right = self.right.insert(key)

			# if key == 1:
			# 	print(self.value)
			# 	print(self.left.value)
			# 	print(self.right.value)
		
			self.height = 1 + max(self.getHeight(),
							self.right.getHeight())

			if self.left != None and self.right != None:
				b = self.getBal()
				print(b)


				if b > 1 and key < self.left.value:
					return self.rightrotate()

				if b < -1 and key > self.right.value:
					return self.leftrotate()

				if b > 1 and key > self.left.value:
					self.left = self.left.leftrotate()
					return self.rightrotate()

				if b < -1 and key < self.r.value:
					self.right = self.right.rightrotate()
					return self.leftrotate()

			return




	def leftrotate(self):
		v = self.value
		vr = self.right.value
		tl = self.left
		trl = self.right.left
		trr = self.right.right
		newleft = AVLTree(v)
		newleft.left = tl
		newleft.right = trl
		self.value = vr
		self.right = trr
		self.left = AVLTree(v)
		return
	
	def rightrotate(self):
		v = self.value
		vl = self.left.value
		tr = self.right
		tlr = self.left.right
		tll = self.left.left
		newright = AVLTree(v)
		newright.right = tr
		newright.left = tlr
		self.value = vl
		self.left = tll
		self.right = AVLTree(v)
		return

	def inorder(self):
		if self.isempty():
			return([])
		else:
			return(self.left.inorder()+ [self.value]+ self.right.inorder())
	
	def preorder(self):
		if self.isempty():
			return([])
		else:
			return([self.value] + self.left.preorder()+ self.right.preorder())
	
	def postorder(self):
		if self.isempty():
			return([])
		else:
			return(self.left.postorder()+ self.right.postorder() + [self.value])


A = AVLTree()

A.insert(4)
A.insert(2)
A.insert(1)
# print(A.right.right)
# print(A.value)
# print(A.left.value)

# # A.insert(7)
# # A.insert(8)


# print(A.getBal())


print(A.inorder())
print(A.preorder())
print(A.postorder())