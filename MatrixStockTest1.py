import yfinance as yfi
import os
def main():
    tsla=yfi.Ticker("TSLA")
    history=tsla.history(period="1d")
    print(history)
    os.system("pause")
main()
