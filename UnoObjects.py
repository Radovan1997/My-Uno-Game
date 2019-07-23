#UNO Parts

import random
import math
    
    

class card:

    def __init__(self, value, color):
        self.value = value
        self.color = color



    def __repr__(self):
        retString = ""
        retString += str(self.color)
        retString += " "
        retString += str(self.value)


        return retString


    


class pile:

    def __init__(self,deckvar):
        
        
        self.deck = deckvar
        
        self.startCard = self.deck.pickRandom()
        self.playedCards = [self.startCard]
        self.currentColor = self.startCard.color
        self.currentValue = self.startCard.value



    def __repr__(self):
        retString = ""
        retString += str(self.playedCards)
        return retString


    def addCard(self,card):

        if (card.color == self.currentColor) or (card.value == self.currentValue):
            self.playedCards += [card]
            self.currentColor = card.color
            self.currentValue = card.value
            
            return True

        else:
            print("That card cannot currently be played")
            return False
    
    
    

class deck:
    
    def __init__(self):
        
        self.colors = ["red", "yellow", "blue", "green"]
        self.values = range(10)
        self.deckStatus = []
        
        for i in range(len(self.colors)):
            for j in range(len(self.values)):
                self.deckStatus += [card(j+1, self.colors[i])]
        
    
    def __repr__(self):
        s = str(self.deckStatus)
        return s
    
    def remove(self,cardval):
        self.deckStatus.remove(cardval)
        
    
    def pickRandom(self):
        lenv = len(self.deckStatus)
        picknum = random.uniform(0,lenv) % lenv
        picknum = int(picknum)
        cardChosen = self.deckStatus[picknum]
        self.remove(cardChosen)
        return cardChosen
    
        
        
            
            
    



class handHeld:

    def __init__(self,initial_cards,pilev,deckv):
        self.deck = deckv
        self.pile = pilev
        self.Hand = []

        possibleColors = ["red", "yellow", "blue", "green"]
        possibleValues = [x for x in range(1,11)]
        
        for i in range(initial_cards):
            
            self.Hand += [self.deck.pickRandom()]
    
    
    
    def __repr__(self):
        s = str(self.Hand)
            
        

class Player:
    
    def __init__(self,startCards,pilev,deckv):
        
        self.PlayerHand = handHeld(startCards,pilev,deckv).Hand
        self.pileVar= pilev
        self.deck = deckv
    
    def __repr__(self):
        s = ""
        s += str(self.PlayerHand)
        return s
    
    
    
    def __repr__(self):
        s = str(self.PlayerHand)
        return s
    
    def play(self,cardval):
        if (self.pileVar.currentColor == cardval.color) or (self.pileVar.currentValue == cardval.value):
            self.pileVar.addCard(cardval)
            self.PlayerHand.remove(cardval)
            return True
        else:
            print("You can't add that card")
            return False
    
    def turn(self):
        isWinner = False
        print(self.PlayerHand)
        
        x = int(input("Select card to play:  "))
        
        if ((x not in range(-1,len(self.PlayerHand)))):
            
            print("")
            
            while ((x not in range(-1,len(self.PlayerHand)))):
                print("Sorry that number is invalid please try again")
                x = int(input("Select card to play:  "))
            
            
            
            
        
        if x == -1:
            self.PlayerHand += [self.deck.pickRandom()]
        
        else:
            cardToPlay = self.PlayerHand[x]
            y = self.play(cardToPlay)
            
            if y == False:
                self.turn()
        
        
        
        
        
        if self.PlayerHand == []:
            isWinner = True
        
        
        return isWinner
    
    def has_won(self):
        return (self.PlayerHand == [])
    
        
        
            


        
        

        
        


        

            























        

