# STUDENT NUMBER: 123104113
# STUDENT NAME: ADVAIT MATHUR

import random
class Market:

    """
    Market class to represent the Stock Market

    This class contains 3 functions and 2 class methods. It is responsible for maintaining a list
    of stocks and their details such as current price, previous price, change in price as a percentage.

    It is responsible for generating the Market as well as displaying it. The individual description
    of each function is included in the definition of the functions.
    """

    stocks = []


    def __init__(self, name, currentprice, previousprice):

        """
        Initializes Market by passing: name of stock (str), current price (int), previous price (int).
        These are assigned to protect instance variables _name, _currentprice, _previousprice respectively.

        Change in price value initialized as _change is calculated by calling calcChange function defined below.

        Arguments:
        Name of Stock (_name) -> Name of stock as string
        Current Price (_currentprice) -> Current price of stock as integer
        Previous Price (_previousprice) -> Previous price of stock as integer

        Returns:
        N/A

        Raises:
        N/A
        """

        self._name = name
        self._currentprice = currentprice
        self._previousprice = previousprice
        self._change = self.calcChange()
        Market.stocks.append(self)

    def calcChange(self):

        """
        Calculates change in price of stock as a percentage and returns it.

        Arguments:
        N/A

        Returns:
        Float representing the percentage change in price of stock from previous price to current price.
        """
        return ((self._currentprice - self._previousprice) / self._previousprice) * 100

    
    def display(self):
        """
        Displays the Stock name, current price, previous price and change in price along with a '+' or '-' symbol
        based on whether the change is positive or negative (stock has risen or fallen).

        Arguments:
        N/A

        Returns:
        Stock name, current price, previous price and change as a string.

        Raises:
        N/A
        """
        
        if self._change >= 0:
            symbol = "+"
        else:
            symbol = "-"
        change_display = f"{symbol}{abs(round(self._change,2))}%"
        return f"Stock Name: {self._name}\nCurrent Price: ${self._currentprice} Previous Price ${self._previousprice} Change: {change_display}"
    
    @classmethod
    def generate_stocks(cls):

        """
        Creates multiple instances of stocks. Random module is used for manipulating stock price in a given range.
        Modifies currentprice, previousprice as random integers generated using random.randint.

        Arguments:
        N/A

        Returns:
        N/A

        Raises:
        N/A
        """

        stock_price = {"AAPL": (210, 250),
                        "NVDA": (120, 160),
                        "MFST": (410, 470),
                        "GOOGL":(120, 200),
                        "AMZN":(150, 240),
                        "META": (550, 700),
                        "ADOBE": (480, 530),
                        "AIRBNB": (120, 180),
                        "NETFLIX": (770, 850),
                        "TESLA": (210, 260)}
        for name, price in stock_price.items():
            previousprice = random.randint(price[0], price[1])
            currentprice = random.randint(price[0], price[1])
            cls(name, currentprice, previousprice)
    

    @classmethod
    
    def display_list(cls):

        """
        Displays the list of stocks.

        Arguments:
        N/A

        Returns:
        N/A

        Raises:
        N/A
        """

        for stock in cls.stocks:
            print(stock.display())   
