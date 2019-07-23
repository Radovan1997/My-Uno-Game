#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:36:08 2019

@author: radovanvitek
"""

# UNO Game

import UnoObjects


def play_game(numPlayers,initCards):
    
    GameDeck = UnoObjects.deck()
    GamePile = UnoObjects.pile(GameDeck)
    
    playerList = []
    
    winner = -1
    
    for i in range(numPlayers):
        playerList += [UnoObjects.Player(initCards,GamePile, GameDeck)]
    
    
    #print(playerList)
    
    print("Starting hands:")
    for x in range(len(playerList)):
        print(playerList[x])
    
    print("Game Starting:")
    print("")
    
    roundcounter = 0
    
    
    while (True):
        
        #print("len list = ", len(playerList))
        
        for x in range(len(playerList)):
            print("")
            print("Card on top is: ")
            print (GamePile.currentColor,GamePile.currentValue)
            playerList[x].turn()
            
            if playerList[x].has_won() == True:
                print("")
                print("The winner is Player:", (x%len(playerList) + 1))
                break
            
                
            
        
        
        
        
        roundcounter += 1
            
    
        
    
    

    
    