import pickle
import tkinter as tk
import random as rd
from os import system, name
import time

class Card():
    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer

class Window():
    def __init__(self, root, mode:str):
        self.root = root
        self.root.geometry("500x500")
        self.root.title = "FlashTool"
        
        self.mode = mode
        self.currentCardIndex = 0
        self.CardDeck = [Card("cat", "dog"), Card("lol", "lmao")]

        if self.mode == "create":
            self.studyMode()
        elif self.mode == "study":
            self.studyMode()
        

    def studyMode(self):
        self.mode = "study"
        self.root.label = tk.Label(text="Study Mode")
        self.root.label.pack()
        
        self.root.questionLabel = tk.Label(text=self.CardDeck[self.currentCardIndex].question)
        self.root.questionLabel.pack()

        self.root.answerLabel = tk.Label(text=self.CardDeck[self.currentCardIndex].answer)
        self.root.answerLabel.pack()
        
        self.root.answerBox = tk.Entry()
        self.root.answerBox.pack()
        
        self.root.checkAnsButt = tk.Button(text="Check Answer", command=self.checkAns)
        self.root.checkAnsButt.pack()
        
        self.root.nextButt = tk.Button(text="Next Card", command=self.nextCard)
        self.root.nextButt.pack()

        self.currentCardIndex += 1
        
    def checkAns(self):
        inp = self.root.answerBox.get()
        if inp == self.CardDeck[self.currentCardIndex].answer:
            self.root.outcomeLabel = tk.Label(text="Correct!")
            self.root.outcomeLabel.pack()

    def nextCard(self):
        if self.currentCardIndex > len(self.CardDeck):
            self.currentCardIndex = 0
        self.root.label.destroy()
        self.root.questionLabel.destroy()
        self.root.answerLabel.destroy()
        self.root.answerBox.destroy()
        self.root.checkAnsButt.destroy()
        self.root.nextButt.destroy()
        try:
            self.root.outcomeLabel.destroy()
        except AttributeError:
            self.studyMode()
        self.studyMode()

    def createMode(self):
        self.root.label = tk.Label(text="Create Mode")
        self.root.label.pack()



root = tk.Tk()
app = Window(root, "study")
root.mainloop()