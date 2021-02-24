import string
import random

def splitTextToTriplets(string):
    words = string.split()
    grouped_words = [' '.join(words[0: 3])]
    grouped_words += [' '.join(words[i: i + 3]) for i in range(1, len(words)-2, 1)]
    return grouped_words

with open("ascii.txt", "r") as f:
    content = f.read()

clearContent = content.translate(str.maketrans('', '', string.punctuation))
triplets = splitTextToTriplets(clearContent)


currentTriplets = ["first"]
randPosition = random.randint(0, len(triplets)-1) # Vriskw tin arxiki triada
currentTriplets.append(triplets[randPosition]) # Tin prosthetw stis triades mou
isLastTriplet = currentTriplets[0] == triplets[-1] # epistrefei true an einai h teleytaia triada
finalText = currentTriplets[-1]
words = 3 # exoume idi tis arxikes treis lekseis

while words <= 200 and not isLastTriplet:
    randPosition = random.randint(0, len(triplets)-1) # Psaxnw gia alli triada
    nextTriplet = triplets[randPosition]
    # splitarw tis lekseis kathe triadas
    currentTripletWords = currentTriplets[-1].split()
    nextTripletWords = nextTriplet.split()
    #elegxw tis lekseis kathe triadas
    if currentTripletWords[1] == nextTripletWords[0] and currentTripletWords[2] == nextTripletWords[1]:
        currentTriplets.append(nextTriplet)
        words += 1
        isLastTriplet = currentTriplets[-1] == triplets[-1]
        finalText += " " + nextTripletWords[-1]


print(finalText)
