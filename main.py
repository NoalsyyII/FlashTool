import pickle
import tkinter as tk
import random as rd
from os import system, name
import time

def clear():
 
    if name == 'nt':
        _ = system('cls')
 
    else:
        _ = system('clear')

class Card():
    
    def __init__(self, question, answer) -> None:
        self.question = question
        self.answer = answer

def createNewCard() -> Card:
    
    newQ = input("Enter question >>")
    newA = input("Enter answer >>")
    newCard = Card(newQ, newA)

    
    return newCard

open("data", "wb")
cardDeck = []

while True:
    
    clear()
    mode = input("Study (s) or Create (c) mode (exit to exit)\n>> ")
    
    if mode == "s":
        
        if len(cardDeck) > 0:
            for i, c in enumerate(cardDeck):
                print(c.question)
                ansInp = input(">> ")
                if ansInp == c.answer:
                    print("Correct!")
                else:
                    print(f"Incorrect! The correct answer was {c.answer}")
                continue
        else:
            print("Card deck cannot be empty!")
        
        print("Finished card deck! Returning to main menu...")
        time.sleep(1)
        continue

    elif mode == "c":
        while True:    
            system('cls')
            cont = ""
            cont = input("Create new card? y/n >> ")
            if cont == "y":
                cardToAdd = createNewCard()
                cardDeck.append(cardToAdd)
            else:
                break
        continue
    
    else:
        print("err")
        break
        