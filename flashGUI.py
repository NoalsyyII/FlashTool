import pickle
import tkinter as tk
import random as rd
from os import system, name
import time

class Card():
    
    def __init__(self, question: str, answer: str) -> None:
        self.question = question
        self.answer = answer

def createNewCard() -> Card:
    
    newQ = input("Enter question >>")
    newA = input("Enter answer >>")
    newCard = Card(newQ, newA)

    return newCard

def checkAnswer():
    ans = answerBox.get()
    if ans == createNewCard():
        pass

# inpfile = open("data", "rb")
# cardDeck = pickle.load(inpfile)
# inpfile.close()

cardDeck = []
cardDeck.append(Card("Question", "Answer"))
cardDeck.append(Card("Qestion1", "Answ"))


mainWin = tk.Tk()


def studyMode(*args, **kwargs):
    mainWin.destroy()
    studyWin = tk.Tk()
    studyWin.geometry("500x500")
    for i, c in enumerate(cardDeck):
        studyWin.title(f"Question {i} of {len(cardDeck)}")
        questionLabel = tk.Label(text=c.question)
        answerLabel = tk.Label(text=c.answer)
        global answerBox 
        answerBox = tk.Entry()
        checkAnsButt = tk.Button(text="Check Answer")
        questionLabel.pack()
        answerLabel.pack()
        checkAnsButt.pack()
        answerBox.pack()
        

    
    studyWin.mainloop()


def createMode():
    createWin = tk.Tk()
    createWin.mainloop()

def mainMenu():
    mainWin.geometry("500x500")
    mainWin.title("Main Menu")
    welcome = tk.Label(text="Welcome to FlashTool")
    createButt = tk.Button(text="Manage Cards")
    createButt.bind("<Button-1>", createMode)
    studyButt = tk.Button(text="Study Cards")
    studyButt.bind("<Button-1>", studyMode)

    welcome.pack()
    createButt.pack()
    studyButt.pack()
    
    mainWin.mainloop()

mainMenu()