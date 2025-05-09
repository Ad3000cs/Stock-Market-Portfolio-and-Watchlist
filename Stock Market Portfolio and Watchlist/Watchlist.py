# STUDENT NUMBER: 123104113
# STUDENT NAME: ADVAIT MATHUR

from Market import *

class Watchlist(Market):

    """
    Watchlist class to represent a watchlist of stocks to be monitored by the user.

    This class has 3 functions and 2 static methods responsible for maintaining a watchlist
    of stocks available in the market (Market class) for the user. The class Inherits from the 
    Market class. The user can create more than one watchlist.


    The individual description of each function is included in the definition of the functions.
    """

    allwatchlists = {}

    def __init__(self,watchlistname):

        """
        Initializes watchlist - a list of stocks. The watchlist name is stored in allwatchlists defined above.

        Arguments: 
        watchlistname - Name of the watchlist provided bu user

        Returns:
        N/A

        Raises:
        ValueError if watchlistname is not alphabetic  
        """
        
        if watchlistname in Watchlist.allwatchlists:
            print(f"Watchlist {watchlistname} already exists")
            exit()

        if not watchlistname.isalpha():
            raise (ValueError("The Watchlist name should be alphabetic!"))

        self._watchlistname = watchlistname
        self._watchlist = []
        Watchlist.allwatchlists[watchlistname] = self


    
    def get_stock(self, stock_name, stocks):

        """
        Gets stocks from User and adds details from Market class to watchlist.

        Arguments:
        stock_name -> Stock name given by user
        stocks -> list of stocks from Market class

        Returns:
        N/A

        Raises:
        ValueError if stock_name is not alphabetic
        """

        for stock in stocks:
            if stock._name == stock_name:                
                self._watchlist.append([stock._name, stock._currentprice, stock._previousprice])
                return
                
            if not stock_name.isalpha():
                raise (ValueError("The stock name should be alphabetic!"))
        
        if stock._name != stock_name and stock_name != "": 
            print("Mentioned stock not found in market")

        
    
    def displayWatchlist(self):

        """
        Displays all stocks from watchlist

        Arguments:
        N/A

        Returns:
        N/A

        Raises:
        N/A
        """

        print(f"Watchlist: {self._watchlistname}")

        if not self._watchlist:
            print("The Watchlist is empty")

        else:
            for stock in self._watchlist:
                print(stock)
    
    @staticmethod
    def display_all_watchlists():

        """
        Displays all watchlist names

        Arguments:
        N/A

        Returns:
        N/A

        Raises:
        N/A
        """

        print("All Watchlists: ")
        if not Watchlist.allwatchlists:
            print("No watchlists found")
        else:
            for name in Watchlist.allwatchlists.keys():
                print(name)
    
    @staticmethod
    def particular_watchlist_contents(watchlistname):

        """
        Displays content of a particular watchlist. Takes watchlist name as argument and uses displaywatchlist() function.

        Arguments:
        watchlistname - Name of the watchlist for which content has to be shown, provided by user

        Returns:
        N/A

        Raises:
        ValueError if watchlistname is not alphabetic.
        """

        if not watchlistname.isalpha():
            raise (ValueError("The Watchlist name should be alphabetic!"))

        if watchlistname in Watchlist.allwatchlists:
            Watchlist.allwatchlists[watchlistname].displayWatchlist()
        else:
            print(f"Watchlist does not exist")  