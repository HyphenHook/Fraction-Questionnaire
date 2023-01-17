#Author: Wen Bin Zhang
#Date: April 29, 2020
#Purpose: Fraction questionnaire
#============================================================
from tkinter import *
import random

#Author: Wen Bin Zhang
#Date: April 29, 2020
#Purpose: A Fraction class for use
#Date Elements:
#   numberator - integer
#   denominator - integer
#Methods:
#   init - initialize the field
#   str - returns the fractions in mixed form
#   calcGCD - calculate the gcd of 2 integers
#   reduce - reduce the fraction
#   setValue - set the value of the numerator and denominator
#   randomize - randomize the fraction
#   calcInverse - calculate the inverse of fraction
#   __eq__ - overload the equal relation
#   __add__ - overload the add operation
#   __sub__ - overload the sub operation
#   __mul__ - overload the multiply operation
#   __truediv__ - overload the divide operation
#==================================================
class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        self.intNumerator = numerator
        self.intDenominator = denominator
        self.reduce()

#   Author: Wen Bin Zhang
#   Date: April 29, 2020
#   Purpose: Handle print statements
#   Inputs/Parameters: N/A
#   Outputs/Returns: the value of fraction
#   Dependencies: N/A
#==================================================
    def __str__(self):
        if self.intNumerator % self.intDenominator == 0:
            numerator = self.intNumerator // self.intDenominator          
            answer = str(numerator)
        elif self.intNumerator < 0:
            if (self.intNumerator * -1) > self.intDenominator:
                mixed = -1 * ((self.intNumerator * -1) // self.intDenominator)
                numerator = (self.intNumerator * -1) % self.intDenominator
                answer = str(mixed) + " " + str(numerator) + "/" + str(self.intDenominator)
            else:
                answer = str(self.intNumerator) + "/" + str(self.intDenominator)
        elif self.intNumerator > 0:
            if self.intNumerator > self.intDenominator:
                mixed = self.intNumerator // self.intDenominator
                numerator = self.intNumerator % self.intDenominator
                answer = str(mixed) + " " + str(numerator) + "/" + str(self.intDenominator)
            else:
                answer = str(self.intNumerator) + "/" + str(self.intDenominator)
        return answer

#Author: Wen Bin Zhang
#Date: March 3, 2020
#Purpose: Calculating GCD
#Inputs/Parameters: numberA - first number
#                   numberB - second number
#Outputs/Returns: calculate the greatest common divisors of the two numbers in parameter.
#Dependencies: None
#==============================================================================
    def calcGCD(self, numberA, numberB):
        count = numberA % numberB
        while count != 0:
            numberA = numberB
            numberB = count
            count = numberA % numberB
        return numberB

#   Author: Wen Bin Zhang
#   Date: April 29, 2020
#   Purpose: Reduce the fraction
#   Inputs/Parameters: N/A
#   Outputs/Returns: a reduced fraction
#   Dependencies: calcGCD()
#==================================================
    def reduce(self):
        if self.intDenominator == 0:
            self.intNumerator = 0
            self.intDenominator = 1
        else:
            if self.intDenominator < 0 and self.intNumerator < 0:
                self.intDenominator *= -1
                self.intNumerator *= -1
                gcd = self.calcGCD(self.intNumerator, self.intDenominator)
                self.intNumerator //= gcd
                self.intDenominator //= gcd
            elif self.intNumerator < 0:
                self.intNumerator *= -1
                gcd = self.calcGCD(self.intNumerator, self.intDenominator)
                self.intNumerator //= gcd
                self.intNumerator *= -1
                self.intDenominator //= gcd
            elif self.intDenominator < 0:
                self.intDenominator *= -1
                gcd = self.calcGCD(self.intNumerator, self.intDenominator)
                self.intNumerator //= gcd
                self.intNumerator *= -1
                self.intDenominator //= gcd
            else:
                gcd = self.calcGCD(self.intNumerator, self.intDenominator)
                self.intNumerator //= gcd
                self.intDenominator //= gcd
                
#   Author: Wen Bin Zhang
#   Date: April 29, 2020
#   Purpose: Set the value of the fraction
#   Inputs/Parameters:
#               numerator - the numerator value
#               denominator - the denominator value
#   Outputs/Returns: the value of fraction set
#   Dependencies: reduce()
#==================================================              
    def setValue(self, numerator = 0, denominator = 1):
        self.intNumerator = numerator
        self.intDenominator = denominator
        self.reduce()

#   Author: Wen Bin Zhang
#   Date: April 29, 2020
#   Purpose: Randomize the fraction
#   Inputs/Parameters: N/A
#   Outputs/Returns: the randomized fraction
#   Dependencies: reduce()
#==================================================
    def randomize(self, maxInt = 10):
        self.intNumerator = random.randint(maxInt * -1, maxInt + 1)
        self.intDenominator = random.randint(maxInt * -1, maxInt + 1)
        self.reduce()

#   Author: Wen Bin Zhang
#   Date: April 29, 2020
#   Purpose: Calculate the inverse
#   Inputs/Parameters: N/A
#   Outputs/Returns:
#               self.intDenominator - the denominator
#               self.intNumerator - the numerator
#   Dependencies: N/A
#==================================================
    def calcInverse(self):
        return self.intDenominator, self.intNumerator

#   Author: Wen Bin Zhang
#   Date: April 29, 2020
#   Purpose: Overload equal to operator
#   Inputs/Parameters:
#                   self - the corresponding fraction
#                   secondFraction - the second fraction
#   Outputs/Returns: Boolean True or False
#   Dependencies: N/A
#==================================================
    def __eq__(self, secondFraction):
        answer = False
        if self.intNumerator == secondFraction.intNumerator and self.intDenominator == secondFraction.intDenominator:
            answer = True
        return answer

#   Author: Wen Bin Zhang
#   Date: April 29, 2020
#   Purpose: Overload add arithematic operation
#   Inputs/Parameters:
#                   self - the corresponding fraction
#                   secondFraction - the second fraction
#   Outputs/Returns:
#               numerator - the numerator answer
#               denominator - the denominator answer
#   Dependencies: N/A
#==================================================
    def __add__(self, secondFraction):
        temp = self.intNumerator
        temp2 = secondFraction.intNumerator
        if self.intDenominator != secondFraction.intDenominator:
            denominator = self.intDenominator * secondFraction.intDenominator
            self.intNumerator *= secondFraction.intDenominator
            secondFraction.intNumerator *= self.intDenominator
            numerator = self.intNumerator + secondFraction.intNumerator
        else:
            numerator = self.intNumerator + secondFraction.intNumerator
            denominator = self.intDenominator
        self.intNumerator = temp
        secondFraction.intNumerator = temp2
        return numerator, denominator

#   Author: Wen Bin Zhang
#   Date: April 29, 2020
#   Purpose: Overload subtract arithematic operation
#   Inputs/Parameters:
#                   self - the corresponding fraction
#                   secondFraction - the second fraction
#   Outputs/Returns:
#               numerator - the numerator answer
#               denominator - the denominator answer
#   Dependencies: N/A
#==================================================
    def __sub__(self, secondFraction):
        temp = self.intNumerator
        temp2 = secondFraction.intNumerator
        if self.intDenominator != secondFraction.intDenominator:
            denominator = self.intDenominator * secondFraction.intDenominator
            self.intNumerator *= secondFraction.intDenominator
            secondFraction.intNumerator *= self.intDenominator
            numerator = self.intNumerator - secondFraction.intNumerator
        else:
            numerator = self.intNumerator - secondFraction.intNumerator
            denominator = self.intDenominator
        self.intNumerator = temp
        secondFraction.intNumerator = temp2
        return numerator, denominator

#   Author: Wen Bin Zhang
#   Date: April 29, 2020
#   Purpose: Overload multiply arithematic operation
#   Inputs/Parameters:
#                   self - the corresponding fraction
#                   secondFraction - the second fraction
#   Outputs/Returns:
#               numerator - the numerator answer
#               denominator - the denominator answer
#   Dependencies: N/A
#==================================================
    def __mul__(self, secondFraction):
        numerator = self.intNumerator * secondFraction.intNumerator
        denominator = self.intDenominator * secondFraction.intDenominator
        return numerator, denominator

#   Author: Wen Bin Zhang
#   Date: April 29, 2020
#   Purpose: Overload division arithematic operation
#   Inputs/Parameters:
#                   self - the corresponding fraction
#                   secondFraction - the second fraction
#   Outputs/Returns:
#               numerator - the numerator answer
#               denominator - the denominator answer
#   Dependencies: N/A
#==================================================
    def __truediv__(self, secondFraction):
        numerator = self.intNumerator * secondFraction.intDenominator
        denominator = self.intDenominator * secondFraction.intNumerator
        return numerator, denominator

#   Author: Wen Bin Zhang
#   Date: April 29, 2020
#   Purpose: Setting up the question
#   Inputs/Parameters: N/A
#   Outputs/Returns: A question displayed
#   Dependencies: randomize(), randint(), setValue(), __str__()
#==================================================
def setup():
    #fraction1.setValue(8, 5)
    #fraction2.setValue(-6, 5)
    fraction1.randomize()
    fraction2.randomize()
    operation = random.randint(1, 4)
    if operation == 1:
        numerator, denominator = fraction1 + fraction2
        questionStr = fraction1.__str__() + " + " + fraction2.__str__()
    elif operation == 2:
        numerator, denominator = fraction1 - fraction2
        questionStr = fraction1.__str__() + " - " + fraction2.__str__()
    elif operation == 3:
        numerator, denominator = fraction1 * fraction2
        questionStr = fraction1.__str__() + " x " + fraction2.__str__()
    else:
        numerator, denominator = fraction1 / fraction2
        questionStr = fraction1.__str__() + " ÷ " + fraction2.__str__()
    fractionAnswer.setValue(numerator, denominator)
    guess = random.randint(1, 2)
    if guess == 1:
        fractionGuess.setValue(numerator, denominator)
    elif guess == 2:
        numerator, denominator = fractionAnswer.calcInverse()
        fractionGuess.setValue(numerator, denominator)
    questionStr += " = " + fractionGuess.__str__()
    question.set(questionStr)
    amountQuestion.set(amountQuestion.get() + 1)

#   Author: Wen Bin Zhang
#   Date: April 29, 2020
#   Purpose: Check if they are correct
#   Inputs/Parameters:
#                   choice - the choice of yes or no
#   Outputs/Returns: Score adding
#   Dependencies: N/A
#==================================================
def check(choice = -1):
    if choice == 0:
        if fractionGuess == fractionAnswer:
            score.set(score.get() + 1)
    if choice == 1:
        if fractionGuess != fractionAnswer:
            score.set(score.get() + 1)
    totalScore.set("Score: " + str(score.get()) + " / " + str(amountQuestion.get()))
    setup()

#Main menu
#Variable
fraction1 = Fraction()
fraction2 = Fraction()
fractionAnswer = Fraction()
fractionGuess = Fraction()

#Fraction WIndow creating
fractionWindow = Tk()
fractionWindow.title("Fraction Questionnaire")
fractionWindow.resizable(0, 0)
fractionWindow.geometry('300x150')

#GUI variable
question = StringVar()
score = IntVar()
amountQuestion = IntVar()
totalScore = StringVar()
score.set(0)
amountQuestion.set(0)


questionLabel = Label(fractionWindow, textvariable = question, font = ("Helvetica", 18), justify = CENTER, width = 20)
questionLabel.place(x = 0, y = 0)
setup()

scoreLabel = Label(fractionWindow, textvariable = totalScore, font = ("Helvetica", 14)).place(x = 95, y = 30)
rightButton = Button(fractionWindow, text = "Right", command = lambda:[check(0)], font = ("Helvetica", 16), justify = CENTER, width = 11).place(x = 3, y = 60)
wrongButton = Button(fractionWindow, text = "Wrong", command = lambda:[check(1)], font = ("Helvetica", 16), justify = CENTER, width = 11).place(x = 155, y = 60)
quitButton = Button(fractionWindow, text = "Quit", command = lambda:[fractionWindow.destroy()], font = ("Helvetica", 16), justify = CENTER, width = 24).place(x = 1, y = 105)

mainloop()

        

    
        
    
