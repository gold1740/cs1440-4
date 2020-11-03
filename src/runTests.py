import unittest

from tests import TestCard, TestDeck, TestMenu, TestNumberSet

suite = unittest.TestSuite()

tests = (TestCard.TestCard, TestDeck.TestDeck, TestMenu.TestMenu, TestNumberSet.TestNumberSet)
for test in tests:
	suite.addTest(unittest.makeSuite(test))

runner = unittest.TextTestRunner(verbosity=2)
print(runner.run(suite))
