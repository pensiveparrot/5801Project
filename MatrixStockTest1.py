import yfinance as yfi
import os
from appJar import gui




def main():
    # stock1=input("Enter stock ticker 1")
    # stock2=input("Enter stock ticker 2")

    #history=tsla.history(period="1d")
    app = gui("Working with yfinance","640x480")
    tickers = listmaker()
    app.addLabelAutoEntry("stock1",tickers)
    def submit():
        data=app.getEntry("stock1")
        print(data)
    app.setEntrySubmitFunction("stock1",submit)

     #print(history)
    app.go()
def listmaker():
    with open('names.txt', 'r') as f:
        myNames = [line.strip() for line in f]
    return myNames
main()
