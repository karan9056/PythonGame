"""this program about 10 pin bowling game that also calculate score 
the BowlingGame class implemented with standard scoring rules that 
calculate the strike of pins, spare bowling calculation, strike bonus points calculation
spare bonus points calculation. there are multiple functions is also created according to the 
points calculation."""
class BowlingGame:  
    """Contructor function created for initializing the class.
    there is empty list also created for storing score values according to the rolls pins knowked down in game"""  
    def __init__(self):
        self.rolls = []
    
    def roll(self, pins):
        self.rolls.append(pins)
    """this function record the number of pins knocked down in a roll of game
    Parameters:
    pins (int): it append or add the number of pins knocked down in the roll of game from 0 to 10"""
    def score(self):
        """Score method calculate and return the score value according to pins knocked 
        Returns: 
        Calculated score return according to the pins knocked in game.
        it also include bonuses value of strikes and spare
        method iterates through each frame, and check strikes, and spares"""
        totalScore = 0
        frameIndex = 0
        #for loop iterates 10 times
        for frame in range(10):
            if self.isStrike(frameIndex):
                if frameIndex + 2 < len(self.rolls):
                    totalScore += 10 + self.strikeBonus(frameIndex)
                frameIndex += 1
            # check frame do not go out of bounds for the last frame
            elif self.isSpare(frameIndex):
                if frameIndex + 2 < len(self.rolls):
                    totalScore += 10 + self.spareBonus(frameIndex)
                frameIndex += 2
            else:
            #check two rolls for this frame 
                if frameIndex + 1 < len(self.rolls):
                    totalScore += self.sumOfBallsInFrame(frameIndex)
                frameIndex += 2
        return totalScore
    
    def isStrike(self, frameIndex):
        return frameIndex < len(self.rolls) and self.rolls[frameIndex] == 10
        """Strike value calculation by above method
        Parameters: 
        frameIndex (int) : check index value in the rolls list
        Returns:
        Boolean: if roll strike 10 pins it returns true and else false"""
    def isSpare(self, frameIndex):
        """Spare method check two rolls starting value from spare index
        Parameters:
        frameIndex (int) : Starting index check
        Returns:
        bool: true if the sum of two consecutive rolls is 10 a spare else false """
        return (frameIndex + 1 < len(self.rolls) and 
                self.rolls[frameIndex] + self.rolls[frameIndex + 1] == 10)
    
    def strikeBonus(self, frameIndex):
        return self.rolls[frameIndex + 1] + self.rolls[frameIndex + 2]
    """strike bonus method calculate the strike bonus points according to strike
    parameters:
    Strike roll index value
    Returns:
    frameIndex (int) : it return the sum of two rolls after the strike pins knocked down"""
    def spareBonus(self, frameIndex):
        return self.rolls[frameIndex + 2]
    """Last spare bonus method calculate spare bonus points
    Parameters:
    frameIndex (int): index of the first roll in the spare
    returns:
    Number of pins knocked down in the next roll after the spare"""
    def sumOfBallsInFrame(self, frameIndex):
    
        return self.rolls[frameIndex] + self.rolls[frameIndex + 1]
    """Sum of two rolls in a frame with no strike or spare
    Parameters:
    frameIndex (int): index of first roll in the frame of game
    Returns:
    sum of two consecutive rolls"""
