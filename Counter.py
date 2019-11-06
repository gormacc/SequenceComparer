def checkCounts(sequenceA, sequenceB):

    gaps = 0
    mismatches = 0
    matches = 0

    for i in range(0, len(sequenceA)):
        if(sequenceA[i] == sequenceB[i]):
            matches += 1
        else:
            mismatches += 1

    gaps = sequenceA.count("-") + sequenceB.count("-")

    print("Matches : " + str(matches))
    print("Mismatches : " + str(mismatches))
    print("Gaps : " + str(gaps))
