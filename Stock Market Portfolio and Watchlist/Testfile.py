"""
STUDENT NUMBER: 123104113
STUDENT NAME: ADVAIT MATHUR

This is a test file that uses classes and functions from Market, Watchlist, Portfolio files.

On running this file, you will see a list of stocks, and a menu stating the choices. I am giving
some sample data based on your selection from the menu for the basic idea of my program. 
To check error checking, please refer to comments for functions, classes in other files and run the test file. 


------------------- THIS IS A SAMPLE TEST RUN OF THE PROGRAM. --------------------------------------------


1: Create a new watchlist

Input 1 prompt: new
Input 2 prompt: AAPL
Input 3 prompt:

if y then:

    Input 1: META
    Input 2 prompt: n

2. View a specific watchlist

Input: new

3. View all watchlists") -> no input prompts

4. Manage Portfolio") -> Shows menu for Managing portfolio

choices and sample inputs: 

    1. Buy Stock

    Input 1: AAPL
    Input 2: 100
    Input 3: 

        if y then:
            Input 1: META
            Input 2: 120
            Input 3: n

    2. Sell Stock

    Input 1: AAPL
    Input 2: 20
    Input 3: 
        if y then: 
            Input 1: META
            Input 2: 40
            Input 3: n
            
    3. View Portfolio -> Shows your Portfolio


    4. Exit and return to main menu -> Returns to main menu


5. Exit -> Exits the program


"""




from Market import *
from Watchlist import *
from Portfolio import *

Market.generate_stocks()

print("\n ----------------------- MARKET OPEN -----------------------------------------\n")

Market.display_list()

def create_new_watchlist():

    """
    Prompts the user to enter the watchlist name. Once done, creates a Watchlist class 
    instance with argument watchlistname.

    Arguments:
    N/A

    Returns:
    watchlist -> instance of Watchlist class

    Raises:
    ValueError if user inputs incorrect/invalid value.
    """

    try:

        watchlistname = input("\nEnter the name of your new watchlist: ")
        watchlist = Watchlist(watchlistname)
        return watchlist

    except ValueError as e:
        print(e)

def add_stocks_watchlist(watchlist):

    """
    Prompts the user to enter name of a stock it wants to add in their watchlist.
    Also asks if they want to add more stocks or not.

    Arguments:
    watchlist -> The Watchlist created before.

    Returns:
    N/A

    Raises:
    ValueError if user inputs incorrect/invalid value.
    """

    try:

        Choose = input("\nEnter the name of the stock you want to add: \n").upper()

        watchlist.get_stock(Choose, Market.stocks)

        Choose2 = input("Do you want to add more stocks to this watchlist? Enter y/n: ").lower()

        if Choose2 not in ["y", "n"]:
            print("Invalid input, choose either 'n' or 'y'")
        else:
            while Choose2 != "n":
                Choose = input("\nEnter the name of the stock you want to add: \n").upper()
                watchlist.get_stock(Choose, Market.stocks)
                Choose2 = input("Do you want to add more stocks to this watchlist? Enter y/n: \n").lower()

    except ValueError as e:
        print(e)


def manage_portfolio(portfolio):

    """
    Menu for managing user portfolio.
    """

    while True:
        print("\n")
        print("1. Buy Stock")
        print("2. Sell Stock")
        print("3. View Portfolio")
        print("4. Exit and return to main menu")

        try:
            choice = int(input("Enter your choice (1/2/3/4): "))
        except ValueError:
            print("Choose only from (1/2/3/4): ")
            continue

        if choice == 1:

            try: 

                Stock_name = input("Enter Stock name: ").upper()

                volume = input("Enter the volume: ")

                portfolio.Buy(Stock_name, volume)


                buymore = input("Do you want to continue buying? Enter y/n: ").lower()

                if buymore not in ["n", "y"]:
                    print("Enter either 'n' or 'y'.")
                else:
                    while buymore != "n":
                        Stock_name = input("Enter Stock name: ").upper()
                        volume = input("Enter the volume: ")
                        portfolio.Buy(Stock_name, volume)
                        buymore = input("Do you want to continue buying? Enter y/n: ").lower()
                    

            except ValueError as e:
                print(e)
            except TypeError as e:
                print(e)
        
        elif choice == 2:

            try:

                Stock_name = input("Enter the stock name: ").upper()
                volume = input("Enter the volume: ")
                portfolio.Sell(Stock_name, volume)

                sellmore = input("Do you want to continue selling? Enter y/n: ").lower()

                if buymore not in ["n", "y"]:
                    print("Enter either 'n' or 'y'.")

                else:

                    while sellmore != "n":

                        Stock_name = input("Enter Stock name: ").upper()
                        volume = input("Enter the volume: ")
                        portfolio.Buy(Stock_name, volume)
                        sellmore = input("Do you want to continue selling? Enter y/n: ").lower()


            except ValueError as e:
                print(e)
            except TypeError as e:
                print(e)
        
        elif choice == 3: 
            portfolio.display_portfolio()
            print(f"Total Value of portfolio: ${portfolio.portfolio_value}")
            

        elif choice == 4:
            return (menu())
        
        else:
            print("Wrong Choice!! choose from (1/2/3/4)")


def menu():
    
    """
    Main Menu of the program
    """

    portfolio = Portfolio()
    while True:
        print("\n------------------- MAIN MENU-------------------------\n")
        print("1. Create a new watchlist")
        print("2. View a specific watchlist")
        print("3. View all watchlists")
        print("4. Manage Portfolio")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1/2/3/4/5): "))
        except ValueError:
            print("Invalid input, choose from (1/2/3/4/5)")
            continue

        if choice == 1:
            
            watchlist = create_new_watchlist()
            if watchlist:
                add_stocks_watchlist(watchlist)
        
        elif choice == 2:

            try: 
                watchlistname = input("\n Enter the name of the watchlist to retrieve its contents: ")
                Watchlist.particular_watchlist_contents(watchlistname)

            except ValueError as e:
                print(e)
        

        elif choice == 3:
            Watchlist.display_all_watchlists()

        elif choice == 4:
            manage_portfolio(portfolio)
        
        elif choice == 5:
            exit()
        
        else:
            print("Invalid option, choose from (1/2/3/4/5)")

menu()

