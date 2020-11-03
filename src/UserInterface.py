import Deck
import Menu

class UserInterface():
	def __init__(self):
		pass


	def run(self):
		"""Present the main menu to the user and repeatedly prompt for a valid command"""
		print("Welcome to the Bingo! Deck Generator\n")
		menu = Menu.Menu("Main")
		menu.addOption("C", "Create a new deck")
		
		keepGoing = True
		while keepGoing:
			command = menu.show()
			if command == "C":
				self.__createDeck()
			elif command == "X":
				keepGoing = False


	def __createDeck(self):
		"""Command to create a new Deck"""
		# Get the user to specify the card size, max number, and number of cards
		card_size = self.__getNumberInput("enter the card size",3 , 15)
		max_number = self.__getNumberInput("enter the max number on card", 2 * (card_size ** 2), 4 * (card_size ** 2))
		number_cards = self.__getNumberInput("enter the number of cards", 3, 10000)
		
		# Create a new deck
		
		self.__m_currentDeck = Deck.Deck(card_size, number_cards, max_number)


		# Display a deck menu and allow use to do things with the deck
		self.__deckMenu()


	def __deckMenu(self):
		"""Present the deck menu to user until a valid selection is chosen"""
		menu = Menu.Menu("Deck")
		menu.addOption("P", "Print a card to the screen");
		menu.addOption("D", "Display the whole deck to the screen");
		menu.addOption("S", "Save the whole deck to a file");

		keepGoing = True
		while keepGoing:
			command = menu.show()
			command = command.upper()
			if command  == "P":
				self.__printCard()
			elif command == "D":
				print()
				self.__m_currentDeck.print()
			elif command == "S":
				self.__saveDeck()
			elif command == "X":
				keepGoing = False


	def __printCard(self):
		"""Command to print a single card"""
		cardToPrint = self.__getNumberInput("Id of card to print", 1, self.__m_currentDeck.getCardCount())
		if cardToPrint > 0:
			print()
			self.__m_currentDeck.print(idx=cardToPrint)


	def __saveDeck(self):
		"""Command to save a deck to a file"""
		fileName = self.__getStringInput("Enter output file name")
		if fileName != "":
			# TODO: open a file and pass to currentDeck.print()
			outputStream = open(fileName, 'w')
			self.__m_currentDeck.print(outputStream)
			outputStream.close()
			print("Done!")
	

	def __getStringInput(self, message):
		while True:
			temp = input(message + "\n")
			try:
				open(temp)
			except FileNotFoundError:
				print("file does not exist")
			else:
				return temp


	def __getNumberInput(self, message, start, end):
		while True:
			temp = input(message + " between {} and {}: ".format(start, end))
			if temp.isnumeric():
				if (start <= int(temp) <= end):
					if (int(temp) % 1 == 0):
						return int(temp)
					else:
						print("value must be an integer")
				else:
					print("value MUST be" + " between {} and {}: ".format(start, end))
			else:
				print("enter value as a number i.e. {}".format((start + end) // 2))
		
