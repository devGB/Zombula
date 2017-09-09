class  Triangles:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def getArea(self):
		area = self.width
		return area

class Square:
	def __imit__(self, size):
		self.size = size

	def getArea(self):
		area = self.size * self.size
		return area