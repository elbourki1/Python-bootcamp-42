

class Vector(object):
	def __str__(self):
		return "(Vector " + '[%s]' % ', '.join(map(str,self.items)) + ")"
	def __init__(self,arg):
		self.arg = arg
		if isinstance(arg,list):
			self.init1(arg)
		elif isinstance(arg,int):
			self.init2(arg)
		elif isinstance(arg,range):
			self.init3(arg)
		else:
			raise TypeError
	def init1(self, arg):
		self.items = arg
		self.size = len(arg)
	def init2(self, arg):
		self.size = arg
		self.items = list(range(3))
	def init3(self, arg):
		self.items = list(arg)
		self.size = len(arg)
	def __add__(self, other):
		if self.size < other.size:
			
		return Vector(self.items + other.items)

vector = Vector(5)

print(vector)
print(Vector(range(5)) + Vector(9))
t = [0,1,2] * 5
print(t)