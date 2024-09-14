# Practice 1

import yfinance as yf

def main() -> int:
    try:
        tkr = yf.Ticker('AMZN')
        dataf = tkr.history(period="5d")

        # Removing "Dividends" and "Stock Splits"
        dataf = dataf.drop("Dividends", axis=1)
        dataf = dataf.drop("Stock Splits", axis=1)

        print(dataf)
        return 0
    except:
        return 1

if __name__ == "__main__":
    print(main())