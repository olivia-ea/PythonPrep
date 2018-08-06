#StockTest

from Stock import Stock
def main():
    newstock = Stock("INTC", "Intel Corporation", 20.5, 20.35)

    print("Stock information: \n", "Company Name:", newstock.getName(),
          "\nCompany Symbol:", newstock.getSymbol(),
          "\nPrevious Closing Price:", newstock.getPrevPrice(),
          "\nCurrent Price:", newstock.getCurPrice(),
          "\nPrice Difference:", newstock.getChange())
main()
