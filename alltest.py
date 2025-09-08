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
        """where one strike followed by normal rolls and all 10 pins knocked down in the first roll"""
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
    def test_consecutive_strikes(self):
        print("\n unit test <=> consecutive Strikes")
        rolls = [10, 10, 4, 2] + [0] * 14
        expectedScore = 46  
         # 10+(10+4)=24, 10+(4+2)=16, 4+2=6 → 24+16+6=46
        for pins in rolls:
            self.game.roll(pins)
      
        actualScore = self.game.score()

        print(f" rolls <=> {rolls}")
        print(f" expected score <=> {expectedScore}")
        print(f" actual score <=> {actualScore}")
        print(" correct implementation <=> ", "✓" if actualScore == expectedScore else "✗")

        self.assertEqual(actualScore, expectedScore)
    
    def test_all_ones(self):
        #where all rolls knock down exactly one pins
        print("\n Test case where All strike ones")
        rolls = [1] * 20
        expectedScore = 20

        for pins in rolls:
            self.game.roll(pins)

        actualScore = self.game.score()

        print(f"rolls <=> {rolls}")
        print(f"expected score <=> {expectedScore}")
        print(f"actual score <=> {actualScore}")
        print("correct implementation <=> ", "✓" if actualScore == expectedScore else "✗")
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
    
    
    
    def test_spare_in_last_frame(self):
        #calculate spare in the last frame of game
        print("\n Unit test <=> Spare in Last Frame")
        rolls = [0] * 18 + [5, 5, 3]
        expectedScore = 13 
        
        for pins in rolls:
            self.game.roll(pins)
        
        actualScore = self.game.score()

        print(f" rolls <=> {rolls}")
        print(f" expected score <=> {expectedScore}")
        print(f" actual score <=> {actualScore}")
        print(" correct implementation <=>", "✓" if actualScore == expectedScore else "✗")

        self.assertEqual(actualScore, expectedScore)
    
    def test_strike_in_last_frame(self):
        #calculate spare in the last frame of game
        print("unit test <=> Strike in Last Frame")
        rolls = [0] * 18 + [10, 3, 4]
        expectedScore = 17 
        
        for pins in rolls:
            self.game.roll(pins)

        actualScore = self.game.score()
        
        print(f" rolls <=> {rolls}")
        print(f" expected score <=> {expectedScore}")
        print(f" actual score <=> {actualScore}")
        print(" correct implementation <=> ", "✓" if actualScore == expectedScore else "✗")

        self.assertEqual(actualScore, expectedScore)
    
    def test_perfect_game(self):
        #test perfect game where score 300
        print("\n unit test  <=> Perfect Game")
        rolls = [10] * 12
        expectedScore = 300  
        
        for pins in rolls:
            self.game.roll(pins)
        
        actualScore = self.game.score()
        
        print(f" rolls <=> {rolls}")
        print(f" expected score <=> {expectedScore}")
        print(f" actual score <=> {actualScore}")
        print(" correct implementation <=> ", "✓" if actualScore == expectedScore else "✗")

        self.assertEqual(actualScore, expectedScore)
    
    def test_all_spares(self):
        #check test all spares
        print("\n unit test <=> all spares")
        rolls = [5] * 21
        expectedScore = 150 
        
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
