import unittest
#unittest library import to test the bowling pins game
from bowling_game import BowlingGame
#class contain 9 unit test
class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()
        """
        SetUP method runs before every unit test
        """

    def test_gutter_game(self):
        """first test where all rolls knock down zero pins
        It's total score is zero"""
        print("\n unit Test Gutter Game")
        rolls = [0] * 20
        expectedScore = 0
        #simulate all rolls
        for pins in rolls:
            self.game.roll(pins)

        actualScore = self.game.score()

        print(f"rolls <=> {rolls}")
        print(f"expected score <=> {expectedScore}")
        print(f"actual score <=> {actualScore}")
        print("correct implementation <=> ", "✓" if actualScore == expectedScore else "✗")

        self.assertEqual(actualScore, expectedScore)
if __name__ == '__main__':
    unittest.main()
