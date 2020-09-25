import csv
from fuzzywuzzy import fuzz #imports fuzzy str matching module
from fuzzywuzzy import process

pairingchart = list(csv.reader(open("winepairs.csv")))#opens the csv from a spreadsheet of wine/food pairings

foodGroups = pairingchart[0][1:]
foodtypes = ""
for food in foodGroups:
        foodtypes += food + ", "

def askQuestion():
    print ("Welcome to the wine and food pairing app!")
    print ("If you enter the food you are eating, I can recommend a wine that pairs well with it!")
    print ("To make this simple, I have categorized foods into eleven basic groups:\n")
    print (foodtypes)
    
    wantedname = input("What are you eating?: ")
    pairing = findPairing(wantedname)

    
    if pairing == []:
        return False
    else:
        print("You should drink: ")
        for wine in pairing:
            print(wine)
        return True
        

def findPairing(name):
    pairinglist = []
    #search input food for wine pairing 
    names = pairingchart[0]# finds the food in the CSV file
    foundmatch = False
    for index in range(1,len(names)):#iterates over spreadsheet for matching food to input
        if matches(name,names[index]):
            foundmatch = True
            foodindex = index
            break
    if not foundmatch:
        return []
    
    firsttime = True
    for pairing in pairingchart:
        if not firsttime:#iteraters over other axis for wine pairings
            if pairing[foodindex] == "y":
                pairinglist.append(pairing[0])
        firsttime = False
    return pairinglist

def matches(food, title):
    food = food.lower()
    title = title.lower()
    accuracy =fuzz.ratio(food,title)
    if len(title) > 6 and accuracy > 80:
        return True
    elif len(title) < 7 and accuracy > 74:
        return True
    else:
        return False

finished = False
while not finished:
    finished = askQuestion()
    if not finished:
        print("\nYour entry could not be understood.\n" +
              "Please make sure it is one of the given food groups.\n")
     
    

