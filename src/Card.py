import sys

import NumberSet

class Card():
	def __init__(self, idnum, size, numberSet):
		"""Card constructor"""
		numberSet.randomize()
		self.__idnum = idnum 
		self.__size = size
		self.__card = []
		for i in range(size ** 2):
			self.__card.append(numberSet.getNext())
		if (size % 2 == 1):
			self.__card[(size * size)// 2] = "FREE!"

	def getId(self):
		"""Return an integer: the ID number of the card"""
		return self.__idnum


	def getSize(self):
		"""Return an integer: the size of one dimension of the card.
		A 3x3 card will return 3, a 5x5 card will return 5, etc.
		"""
		return self.__size


	def print(self, file=sys.stdout):
		"""void function:
		Prints a card to the screen or to an open file object"""
		for i in range(self.__size):
			print("+-----"* self.__size + "+", file=file)
			for j in range(self.__size):
				print("|{:^5}".format(self.__card[i * self.__size + j]),file=file, end="")
			print(file=file)
		print("+-----"* self.__size + "+", file=file)
		print(file=file)

