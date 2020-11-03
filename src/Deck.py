import sys

import Card
import NumberSet

class Deck():
	def __init__(self, cardSize, cardCount, numberMax):
		"""Deck constructor"""	
		self.__m_cards = []
		for i in range(cardCount):
			self.__m_cards.append(Card.Card(i, cardSize, NumberSet.NumberSet(numberMax)))
		
			
	def getCardCount(self):
		"""Return an integer: the number of cards in this deck"""
		return len(self.__m_cards)


	def getCard(self, n):
		"""Return card N from the deck"""
		card = None
		n -= 1
		if 0 <= n < self.getCardCount():
			card = self.__m_cards[n]
		return card;


	def print(self, file=sys.stdout, idx=None):
		"""void function: Print cards from the Deck

		If an index is given, print only that card.
		Otherwise, print each card in the Deck
		"""
		if idx is None:
			for idx in range(1, self.getCardCount() + 1):
				c = self.getCard(idx)
				c.print(file)
			print('', file=file)
		else:
			self.getCard(idx).print(file)

