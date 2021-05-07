import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card_game = CardGame()
        self.card1 = Card("heart", 1)
        self.card2 = Card("spade", 7)
        self.cards = [self.card1, self.card2]

    def test_check_for_ace_returns_true(self):
        # Arrange
        expected = True
        # Act
        actual = self.card_game.check_for_ace(self.card1)
        # Assert
        self.assertEqual(expected, actual)

    def test__highest_card_returns_highest_card(self):
        # Arrange
        expected = self.card2
        # Act
        actual = self.card_game.highest_card(self.card1, self.card2)
        # Assert
        self.assertEqual(expected, actual)

    
