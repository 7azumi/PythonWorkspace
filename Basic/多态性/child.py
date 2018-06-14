from father import Father
from mother import Mother

class Child(Father, Mother):
	"""docstring for Child"""
	def __init__(self, money, faceValue):
		Father.__init__(self, money)
		Mother.__init__(self, faceValue)

	


