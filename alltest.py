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
    def test_one_strike(self):
        """where one strike followed by normal rolls"""
        print("\n unit test <=> One Strike")
        rolls = [10, 3, 4] + [0] * 16
        expectedScore = 24  
        # frame 1 contain strike 10 and 2nd frame rolls 3 and 4 and remaining rolls zeros
        for pins in rolls:
            self.game.roll(pins)

        actualScore = self.game.score()

        print(f" rolls <=> {rolls}")
        print(f" expected score <=> {expectedScore}")
        print(f" actual score <=> {actualScore}")
        print(" correct implementation <=> ", "✓" if actualScore == expectedScore else "✗")
        self.assertEqual(actualScore, expectedScore)
    def test_one_spare(self):
        # test a game with one spare value that is followed by a normal roll
        print("\n unit test <=> One Spare")
        rolls = [5, 5, 3] + [0] * 17
        expectedScore = 16 
        #1st frame 5+5, 2nd frame first roll 3 pins, zero for remaining
        for pins in rolls:
            self.game.roll(pins)

        actualScore = self.game.score()

        print(f" rolls <=> {rolls}")
        print(f" expected score <=> {expectedScore}")
        print(f" actual score <=> {actualScore}")
        print(" correct implementation <=> ", "✓" if actualScore == expectedScore else "✗")

        self.assertEqual(actualScore, expectedScore)
   

if __name__ == '__main__':
    unittest.main()
