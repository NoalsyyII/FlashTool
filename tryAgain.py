import pickle
import tkinter as tk
import random as rd
from os import system, name
import time

class Card():
    def __init__(self, question: str, answer: str, reqAnswer=True):
        self.question = question
        self.answer = answer
        self.reqAnswer = reqAnswer

class Window():
    def __init__(self, root, mode:str):
        self.root = root
        self.root.geometry("500x500")
        self.root.title = "FlashTool"
        
        self.mode = mode
        self.currentCardIndex = 0
        self.CardDeck = [Card("cat", "dog"), Card("lol", "lmao")]
        self.InvalidNames = ["", " ", "\n"]

        if self.mode == "create":
            self.createMode()
        elif self.mode == "study":
            self.studyMode()
        
        self.markedcorrect = False

        

    def studyMode(self):
        self.mode = "study"
        self.label = tk.Label(text="Study Mode")
        self.label.pack()
        
        self.answerLabel = tk.Label(text=f"Question {self.currentCardIndex + 1} of {len(self.CardDeck)}")
        self.answerLabel.pack()

        self.questionLabel = tk.Label(text=self.CardDeck[self.currentCardIndex].question)
        self.questionLabel.pack()
        
        self.answerBox = tk.Entry()
        self.answerBox.pack()
        
        self.checkAnsButt = tk.Button(text="Check Answer", command=self.checkAns)
        self.checkAnsButt.pack()
        
        self.nextButt = tk.Button(text="Next Card", command=self.nextCard)
        self.nextButt.pack()

        self.switchButt = tk.Button(text="Create Mode", command=self.switchMode("create"))
        self.switchButt.pack()
        
    def checkAns(self):
        if not self.markedcorrect:
            inp = self.answerBox.get()
            if inp == self.CardDeck[self.currentCardIndex].answer:
                self.outcomeLabel = tk.Label(text="Correct!")
                self.outcomeLabel.pack()
                self.markedcorrect = True
            

    def nextCard(self):
        self.currentCardIndex += 1
        self.markedcorrect = False
        if self.currentCardIndex >= len(self.CardDeck):
            self.currentCardIndex = 0
        
        self.label.destroy()
        self.questionLabel.destroy()
        self.answerLabel.destroy()
        self.answerBox.destroy()
        self.checkAnsButt.destroy()
        self.nextButt.destroy()
        
        try:
            self.outcomeLabel.destroy()
        except AttributeError:
            self.studyMode()
        self.studyMode()

    def createMode(self):
        self.label = tk.Label(text="Create Mode")
        self.label.pack()
        
        self.entryPrompt = tk.Label(text="New question/prompt:")
        self.entryPrompt.pack()
        self.newQuestionBox = tk.Entry(textvariable="New question/prompt")
        self.newQuestionBox.pack()

        self.ansPrompt = tk.Label(text="Associated Answer:")
        self.ansPrompt.pack()
        self.newAnswerBox = tk.Entry()
        self.newAnswerBox.pack()

        self.saveCardButt = tk.Button(text="Check Answer", command=self.saveCard)
        self.saveCardButt.pack()
    
    def saveCard(self):
        newQ = self.newQuestionBox.get()
        newA = self.newAnswerBox.get()
        
        if newQ not in self.InvalidNames and newA not in self.InvalidNames:
            self.CardDeck.append(Card(newQ, newA))
            print(self.CardDeck)
        else:
            print("ERROR: Invalid card content")
    
    def switchMode(self, newMode):
        if newMode == "study":
            self.label.destroy()
            self.entryPrompt.destroy()
            self.newQuestionBox.destroy()
            self.newAnswerBox.destroy()
            self.ansPrompt.destroy()
            self.saveCardButt.destroy()
            self.studyMode()
        elif newMode == "create":
            self.label.destroy()
            self.questionLabel.destroy()
            self.answerLabel.destroy()
            self.answerBox.destroy()
            self.checkAnsButt.destroy()
            self.nextButt.destroy()
            try:
                self.outcomeLabel.destroy()
            except AttributeError:
                self.createMode()
            self.createMode()





        



root = tk.Tk()
app = Window(root, "study")
root.mainloop()