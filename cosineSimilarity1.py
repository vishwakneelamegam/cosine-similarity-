#for square root
import math

#testList
testList = ["apple","mango","grape","pineapple"]
ip1 = ["apple","mango"]

#document list
listOfData = [[1,1,0,0],[1,0,0,1],[0,1,1,0],[0,1,0,1]]


def cleanInput(inputList):
    try:
        testList1 = testList.copy()
        for pos in range(len(testList1)):
            if testList1[pos] in inputList:
                testList1[pos] = 1
            else:
                testList1[pos] = 0
        return testList1
    except:
        return False
    
#cosine similarity function
def cosineSimilarity(vec1,vec2):
    try:
        count = 0
        for i in range(len(vec1)):
            count += vec1[i] * vec2[i]
        return count / float(math.sqrt(sum(vec1)) * math.sqrt(sum(vec2)))
    except:
        return False

#cosine distance
def cosineDistance(value):
    try:
        return float(1 - value)
    except:
        return False
#process

for data in listOfData:
    print(cosineSimilarity(cleanInput(ip1),data))
