# STUDENT NUMBER: 123104113
# STUDENT NAME: ADVAIT MATHUR

from Market import *

class Portfolio(Market):

    """
    Class Portfolio is responsible for maintaining a portfolio of the user's stock purchasing
    and selling. It inherits from the Market class, uses encapsulation for the portfolio (_portfolio).


    It includes 4 functions: __init__, Buy, Sell, display_portfolio and a property: portfolio_value. Using these, a portfolio
    is generated for the user which can be used for buying and selling stocks available in the 
    Market (Market class). The user can also see their portfolio and its total value.

    The individual description of each function is included in the definition of the functions.
    """

    def __init__(self):

        """
        Initializes portfolio as a dictionary. The dictionary is protected in _portfolio

        Arguments:
        N/A

        Returns:
        N/A

        Raises:
        N/A
        """
        self._portfolio = {}
    
    def Buy(self, name, volume):

        """
        Inserts stocks bought by user as a dictionary to self._portfolio and displays the stock name,
        volume and buy price(current price inherited from Market class).

        If the stock name exists in the portfolio, it adds the volume to the existing volume.

        Arguments:
        name -> Name of stock to be bought by the user as string
        volume -> Number of stocks to be purchased as string. After error checking, if everything goes well, casts it as integer.

        Returns: 
        N/A

        Raises: 
        ValueError:-
            1. If the stock name is not Alphabetic.
        TypeError:-
            1. If the volume is negative.
            2. If the volume is not an integer
        """

        stock_found = False

        if type(volume) is not int and not volume.isnumeric():
            raise TypeError("Volume should be a positive integer!!")
        
        volume = int(volume) # Since input by default takes a string, if everything goes well cast to integer.
       
        
        if not name.isalpha():
            raise ValueError("Stock name should be Alphabetic!")

        for stock in Market.stocks:
                if stock._name == name:
                    stock_found = True
                    if stock._name not in self._portfolio:

                        self._portfolio[name] = {"volume": volume, "buy_price": stock._currentprice} # The stock is stored as a dictionary inside a dictionary. Looks like - {"AAPL":{"volume": 100, "buy_price": 210}}
                    else:
                        self._portfolio[name]["volume"] += volume
                    
                    print(f"Stock {name} bought at ${stock._currentprice}. Total cost = ${stock._currentprice * volume}")
                    break

        if not stock_found: 
            print("Mentioned stock not found in market")



    def Sell(self, name,vol_to_remove):

        """
        Removes stocks bought by user. If volume of stocks to be sold is less than existing
        volume, it only updates the volume, if it is same then deletes stock from portfolio
        since volume is zero. You can't sell more stocks than you own.

        Arguments:
        name -> Name of stock to be sold by the user as string
        vol_to_remove -> Number of stocks to be sold as string. After error checking, if everything goes well, casts it as integer.

        Returns: 
        N/A

        Raises:
        ValueError:-
            1. If the stock name is not Alphabetic.
        TypeError:-
            1. If the volume is negative.
            2. If the volume is not an integer

        """

        if type(vol_to_remove) is not int and not vol_to_remove.isnumeric():
            raise TypeError("Volume should be a positive integer!!")
        
        
        vol_to_remove = int(vol_to_remove) # Since input by default takes a string, if everything goes well cast to integer.


        
        if not name.isalpha():
            raise ValueError("Stock name should be Alphabetic!")



        if name not in self._portfolio:
            print("You can't sell stocks which you don't own")
            return
            

        stock_found = False

        for stock in Market.stocks:

            if stock._name == name:
                stock_found = True

                current_volume = self._portfolio[name]["volume"]

                if current_volume < vol_to_remove:
                    print("You can't sell more stocks than you own!!")
                else:
                    self._portfolio[name]["volume"] -= vol_to_remove
                    total_value = vol_to_remove * stock._currentprice
                    print(f"Stock {name} sold at ${stock._currentprice}. Total Value = ${total_value}")


                    if self._portfolio[name]["volume"] == 0:
                        del self._portfolio[name]
                break


        if not stock_found: 
            print("Mentioned stock not found in market")

    def display_portfolio(self):

        """
        Displays the stocks in portfolio as string.

        Arguments:
        N/A

        Returns:
        N/A

        Raises:
        N/A
        """


        print("Your Portfolio: ")
        for name, data in self._portfolio.items():
            print(f"Stock: {name}, Volume: {data["volume"]}, Buy Price: ${data["buy_price"]}")

    @property
    def portfolio_value(self):
        """
        Getter Property for calculating total value of the portfolio

        Arguments:
        N/A

        Returns:
        total_value: Total value of the portfolio, based on currentprice

        Raises:
        N/A
        """
        total_value = 0
        for stock_name, data in self._portfolio.items():
            for stock in Market.stocks:
                if stock_name == stock._name:
                    total_value += data["volume"] * stock._currentprice
                    break
        return total_value
