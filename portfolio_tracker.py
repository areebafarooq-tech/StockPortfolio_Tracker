import csv

# hardcoded stock prices dictionary
stock_prices = {
    "AAPL": 180,   # Apple
    "TSLA": 250,   # Tesla
    "MSFT": 320,   # Microsoft
    "GOOG": 140,   # Google
    "AMZN": 130,   # Amazon
    "NFLX": 420,   # Netflix
    "NVDA": 450,   # Nvidia
    "META": 300,   # Meta (Facebook)
    "INTC": 35,    # Intel
    "AMD": 110,    # Advanced Micro Devices
    "BA": 220,     # Boeing
    "DIS": 90,     # Disney
    "PYPL": 65,    # PayPal
    "ORCL": 105,   # Oracle
    "IBM": 150     # IBM
}


portfolio = {}

def display_available_stocks():
    print("\n Available Stocks:")
    print("-" * 30)
    print("Symbol".ljust(8) + "Price ($)".rjust(10))
    print("-" * 30)
    for stock, price in stock_prices.items():
        print(stock.ljust(8) + str(price).rjust(10))
    print("-" * 30)


def add_stock():
    display_available_stocks()
    stock = input("Enter stock symbol to add: ").upper()
    if stock not in stock_prices:
        print("INVALID STOCK SYMBOL!")
        return
    try:
        quantity = int(input("Enter quantity for " + stock + ": "))
        if quantity <= 0:
            print("QUANTITY MUST BE POSITIVE!")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER!")
        return

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    print("✅ Added " + str(quantity) + " shares of " + stock + " to your portfolio.")

def remove_stock():
    if not portfolio:
        print("Portfolio is empty.")
        return
    stock = input("Enter stock symbol to remove: ").upper()
    if stock in portfolio:
        del portfolio[stock]
        print("✅ Removed " + stock + " from portfolio.")
    else:
        print("Stock not found in portfolio.")

def view_portfolio():
    if not portfolio:
        print("Portfolio is empty.")
        return
    print("\nYOUR PORTFOLIO:")
    print("-" * 50)
    print("Stock".ljust(8) + "Quantity".rjust(10) + "Price ($)".rjust(12) + "Value ($)".rjust(12))
    print("-" * 50)
    total_value = 0
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        total_value += value
        print(stock.ljust(8) + str(quantity).rjust(10) + str(price).rjust(12) + str(value).rjust(12))
    print("-" * 50)
    print("Total Investment:".ljust(30) + str(total_value).rjust(12))
    print("-" * 50)


def save_portfolio():
    if not portfolio:
        print("PORTFOLIO IS EMPTY, NOTHING TO SAVE.")
        return
    filename = "portfolio.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        total_value = 0
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            total_value += value
            writer.writerow([stock, quantity, price, value])
        writer.writerow(["Total", "", "", total_value])
    print("✅ Portfolio saved to " + filename)

# main menu
while True:
    print("\n===== STOCK PORTFOLIO TRACKER =====")
    print("1. View available stocks")
    print("2. Add stock to portfolio")
    print("3. Remove stock from portfolio")
    print("4. View portfolio")
    print("5. Save portfolio to file")
    print("6. Exit")
    
    choice = input("Choose an option (1-6): ")
    
    if choice == "1":
        display_available_stocks()
        input("\nPress Enter to continue...")
    elif choice == "2":
        add_stock()
        input("\nPress Enter to continue...")
    elif choice == "3":
        remove_stock()
        input("\nPress Enter to continue...")
    elif choice == "4":
        view_portfolio()
        input("\nPress Enter to continue...")
    elif choice == "5":
        save_portfolio()
        input("\nPress Enter to continue...")
    elif choice == "6":
        print("👋 Exiting. Goodbye!")
        break
    else:
        print("❌ INVALID CHOICE! PLEASE TRY AGAIN.")
        input("\nPress Enter to continue...")
