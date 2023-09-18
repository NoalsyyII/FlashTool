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

inpfile = open("savedCards.simp", "wb")
newcard = Card("test", "setup")
pickle.dump(None, inpfile)
inpfile.close()

newfile = open("savedCards.simp", "rb")
newdata = pickle.load(newfile)
newfile.close()
print(newdata)
