'''
(The Stock class) Design a class named Stock to represent a company’s stock
that contains:
■ A private string data field named symbol for the stock’s symbol.
■ A private string data field named name for the stock’s name.
■ A private float data field named previousClosingPrice that stores the stock
price for the previous day.
■ A private float data field named currentPrice that stores the stock price for
the current time.
■ A constructor that creates a stock with the specified symbol, name, previous
price, and current price.
■ A get method for returning the stock name.
■ A get method for returning the stock symbol.
■ Get and set methods for getting/setting the stock’s previous price.
■ Get and set methods for getting/setting the stock’s current price.
■ A method named getChangePercent() that returns the percentage changed
from previousClosingPrice to currentPrice.
Draw the UML diagram for the class, and then implement the class. Write a test
program that creates a Stock object with the stock symbol INTC, the name Intel
Programming Exercises 237
Corporation, the previous closing price of 20.5, and the new current price of
20.35, and display the price-change percentage.
'''

class Stock:
    def __init__(self, symbol, name, prevPrice, curPrice):
        self.__symbol = symbol
        self.__name = name
        self.__prevPrice = prevPrice
        self.__curPrice = curPrice

    #getters
    def getSymbol(self):
        return self.__symbol

    def getName(self):
        return self.__name

    def getPrevPrice(self):
        return self.__prevPrice

    def getCurPrice(self):
        return self.__curPrice
    
    #setters
    def setSymbol(self, symbol):
        self.__symbol = symbol

    def setName(self, name):
        self.__name = name

    def setPrevPrice(self, prevPrice):
        self.__prevPrice = prevPrice

    def setCurPrice(self, curPrice):
        self.__curPrice = curPrice

    #constructor
    def getChange(self):
        return self.__curPrice - self.__prevPrice

    

    
