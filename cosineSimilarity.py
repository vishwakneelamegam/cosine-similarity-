#for square root
import math

#document list
listOfData = [[1,0,0,1],[0,1,0,1],[0,0,1,1]]

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
inputVector = [1,0,0,0]

for data in listOfData:
    print(cosineDistance(cosineSimilarity(inputVector,data)))
