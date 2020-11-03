import random

class NumberSet():
	def __init__(self, size):
		"""NumberSet constructor"""
		self.__size = size
		self.__list = [i + 1 for i in range(size)]


	def getSize(self):
		"""Return an integer: the size of the NumberSet"""
		return self.__size
		

	def get(self, index):
		"""Return an integer: get the number from this NumberSet at an index"""
		if (len(self.__list) == 0):
			return None
		else:
			return self.__list[index]



	def randomize(self):
		"""void function: Shuffle this NumberSet"""
		random.shuffle(self.__list)




	def getNext(self):
		"""Return an integer: when called repeatedly return successive values
		from the NumberSet until the end is reached, at which time 'None' is returned"""
		if (len(self.__list) == 0):
			return None
		else:
			return self.__list.pop(0)

