from DirectionEnum import DirectionEnum as de
from Counter import checkCounts

class NeedlemanWunsch:
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

    def solve(self, sequenceA, sequenceB):
        #remove white spaces
        sequenceA = sequenceA.replace(" ", "")
        sequenceB = sequenceB.replace(" ", "")
        #initialization
        rows = len(sequenceA) + 1
        columns = len(sequenceB) + 1
        scoreMatrix = [ [ 0 for i in range(columns) ] for j in range(rows) ]
        directionMatrix = [ [ de.none for i in range(columns) ] for j in range(rows) ]
        #filling matrices with default values
        for i in range(rows):
            scoreMatrix[i][0] = self.gapScore * i
            directionMatrix[i][0] = de.up
        for i in range(columns):
            scoreMatrix[0][i] = self.gapScore * i
            directionMatrix[0][i] = de.left
        directionMatrix[0][0] = de.none
        #filling matrices with scores and directions
        for i in range(1, rows):
            for j in range(1, columns):
                #calculate values of each operation
                match = scoreMatrix[i-1][j-1] + self.matchFunction(sequenceA[i-1], sequenceB[j-1])
                delete = scoreMatrix[i-1][j] + self.matchFunction(sequenceA[i-1], "-")
                insert = scoreMatrix[i][j-1] + self.matchFunction("-", sequenceB[j-1])
                maxValue = max(match, delete, insert)
                #choose best operation and write score to matrices
                if(maxValue == match):
                    scoreMatrix[i][j] = match
                    directionMatrix[i][j] = de.diag
                elif(maxValue == delete):
                    scoreMatrix[i][j] = delete
                    directionMatrix[i][j] = de.up
                else:
                    scoreMatrix[i][j] = insert
                    directionMatrix[i][j] = de.left
        #initialization of aligned sequences
        newSequenceA = ""
        newSequenceB = ""
        i = rows - 1
        j = columns - 1
        #reconstructiong aligned sequences using matrices
        while(directionMatrix[i][j] != de.none):
            if(directionMatrix[i][j] == de.diag):
                i = i - 1
                j = j - 1
                newSequenceA = sequenceA[i] + newSequenceA
                newSequenceB = sequenceB[j] + newSequenceB
            elif(directionMatrix[i][j] == de.left):
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