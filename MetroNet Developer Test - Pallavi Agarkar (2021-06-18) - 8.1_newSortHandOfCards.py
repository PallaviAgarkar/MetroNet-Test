## Function to sort the hand of cards in ascending order

def findSortedCard(cardList):
    newCardList = []
    ## sepatate the card value and suit 
    for card in cardList:
        card = card.split(" ")
        newCardList.append(card[0]) 
        newCardList.append(card[1])

    for i in range(0, len(newCardList), 2):
        for j in range(i+2, len(newCardList), 2):

            # check if card face value at i'th position is higher than j'th position, if yes then swap(sort) it.
            if value(newCardList[i]) > value(newCardList[j]):
                newCardList[i], newCardList[j] = swap(newCardList[i], newCardList[j])
                newCardList[i+1], newCardList[j+1] = swap(newCardList[i+1], newCardList[j+1])

            # if card face value at i'th position and j'th position is same, then check for suit value and swap(sort) it accodingly.
            #  
            elif value(newCardList[i]) == value(newCardList[j]):
                if suit(newCardList[i+1]) > suit(newCardList[j+1]):
                    newCardList[i+1], newCardList[j+1] = swap(newCardList[i+1], newCardList[j+1])
                else:
                    pass
    
    # return the list of cards in ascending order by combining the elements in "value of suit" format
    ascList = []
    for i in range(0, len(newCardList), 2):
        ascList.append(newCardList[i] + " of " + newCardList[i+1])
    return ascList

## function to find the face value of card
def value(r):

    if r == "2":
        return 2
    if r == "3":
        return 3
    if r == "4":
        return 4
    if r == "5":
        return 5
    if r == "6":
        return 6
    if r == "7":
        return 7
    if r == "8":
        return 8
    if r == "9":
        return 9
    if r == "10":
        return 10
    if r == "J":
        return 11
    if r == "Q":
        return 12
    if r == "K":
        return 13
    if r == "A":
        return 14
    return -1

##Function to find the value of shape of card
def suit(s):
    if s == "Hearts":
        return 1
    if s == "Diamonds":
        return 2
    if s == "Clubs":
        return 3
    if s == "Spades":
        return 4
    return -1

## Function to swap the values
def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

## Function to find the Decsending order of cards
def findDecOrder(cardList):
    decList = []
    for i in range(len(cardList)-1, -1, -1):
        decList.append(cardList[i])
    return decList

"""
## Function to find the Ascending order of cards. 
## Implemented this part in "findSortedCard" function to return ascending order of cards.

def findAscOrder(cardList):
    ascList = []
    for i in range(0, len(cardList), 2):
        #print(cardList[i] + " of " +cardList[i+1])
        ascList.append(cardList[i] + " of " +cardList[i+1])
    return ascList
"""

## Function to print the order of cards on separate line
def printOrder(cardList):
    for i in range(0, len(cardList)):
        print(cardList[i])


## Driver code
if __name__ == "__main__":
    ## Input array of cards
    #cardLi = ["7 Hearts", "A Spades", "3 Clubs", "A Hearts"]

    cardLi = ["A Hearts", "6 Spades", "2 Clubs", "Q Hearts", "9 Diamonds", "6 Clubs"]

    ## Find the list of cards in sorted(ascending) order
    cardList = findSortedCard(cardLi)
    print("Sorted list of cards in ascending order: \n", cardList)

    """
    ## Bonus flag to print sorted card in Ascending or Decsending order as per users request
    """
    print("Please enter 1 for Ascending order or 2 for Descending order")
    orderDetail = int(input())

    if orderDetail == 1:
        print("Sorted list of cards in ascending order: ")
        printOrder(cardList)
    elif orderDetail == 2:
        print ("Sorted list of cards in descending order: ")
        printOrder(findDecOrder(cardList))
    else:
        print("Invalid order")
    
    """

    Output:
    sortCardList in Ascending order
    #cardLi = ["7 Hearts", "A Spades", "3 Clubs", "A Hearts"]
    1.	3 of Clubs
    2.	7 of Hearts
    3.	Ace of Hearts
    4.	Ace of Spades

    #################################################

    sortCardList in Descending order
    cardLi = ["A Hearts", "6 Spades", "2 Clubs", "Q Hearts", "9 Diamonds", "6 Clubs"]
    A of Hearts
    Q of Hearts
    9 of Diamonds
    6 of Spades
    6 of Clubs
    2 of Clubs
    
    """