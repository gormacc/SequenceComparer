from DirectionEnum import DirectionEnum as de
from Counter import checkCounts

class SmithWaterman:
    #initializing scores
    def __init__(self, matchScore, mismatchScore, gapScore):
        self.matchScore = matchScore
        self.mismatchScore = mismatchScore
        self.gapScore = gapScore
    #match function
    def matchFunction(self, letterLeft, letterRight):
        if(letterLeft == "-" or letterRight == "-"):
            return self.gapScore
        elif(letterLeft == letterRight): 
            return self.matchScore
        else:
            return self.mismatchScore
    #function returning next move, finding maximum value direction
    def nextMove(self, scoreMatrix, i, j):
        if i == 0:
            return de.left
        if j == 0:
            return de.up
        diag = scoreMatrix[i - 1][j - 1]
        up   = scoreMatrix[i - 1][j]
        left = scoreMatrix[i][j - 1]
        if diag >= up and diag >= left:    
            return de.diag
        elif up > diag and up >= left:      
            return de.up      
        elif left > diag and left > up:
            return de.left

    def solve(self, sequenceA, sequenceB):
        #remove white spaces
        sequenceA = sequenceA.replace(" ", "")
        sequenceB = sequenceB.replace(" ", "")
        #initialization
        rows = len(sequenceA) + 1
        columns = len(sequenceB) + 1
        scoreMatrix = [ [ 0 for i in range(columns) ] for j in range(rows) ]
        #filling matrices with scores
        for i in range(1, rows):
            for j in range(1, columns):
                match = scoreMatrix[i-1][j-1] + self.matchFunction(sequenceA[i-1], sequenceB[j-1])
                delete = scoreMatrix[i-1][j] + self.matchFunction(sequenceA[i-1], "-")
                insert = scoreMatrix[i][j-1] + self.matchFunction("-", sequenceB[j-1])
                scoreMatrix[i][j] = max(match, delete, insert, 0)
        #initialization of aligned sequences        
        newSequenceA = ""
        newSequenceB = ""
        i = rows - 1
        j = columns - 1
        #reconstructiong aligned sequences using matrices
        while(i > 0 or j > 0):
            nextMove = self.nextMove(scoreMatrix, i, j)
            if(nextMove == de.diag):
                i = i - 1
                j = j - 1
                newSequenceA = sequenceA[i] + newSequenceA
                newSequenceB = sequenceB[j] + newSequenceB
            elif(nextMove == de.left):
                j = j - 1
                newSequenceA = "-" + newSequenceA
                newSequenceB = sequenceB[j] + newSequenceB
            else:
                i = i - 1
                newSequenceA = sequenceA[i] + newSequenceA
                newSequenceB = "-" + newSequenceB
        #print results
        print("score : " + str(scoreMatrix[rows - 1][columns - 1]))
        checkCounts(newSequenceA, newSequenceB)

      