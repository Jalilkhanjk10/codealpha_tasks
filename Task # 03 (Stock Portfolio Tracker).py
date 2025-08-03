# Hardcoded Dictionary for Stock Prices
stock_prices = {
    "AAPL": 80,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 310
}


def starts_calculating():       # A Sub-Routine which tracks the stock portfolio
    print("Welcome to Stock Portfolio Tracker")
    total_investment = 0
    portfolio = {}
    qty = 0

    while True:
        stock = input("\nEnter Symbol for stock (or 'Done' to Exit): ").upper()     # Taking stock as input

        if stock == 'DONE':     # if user enters done after tracking, the program end and portfolio summary will be shown in the END.
            break

        if stock not in stock_prices:       # if invalid stock, continue the loop from the start.
            print("Stock not found, Try again.!")
            continue

        try:    # try and except, to handles the Quantity input.
            qty = int(input("Enter the quantity of Stock: "))
        except ValueError:
            print("Invalid Quantity, enter a number")

        value = stock_prices[stock] * qty       # Calculating the value by multiplying the quantity with stock value
        total_investment += value               # Calculating the total investment
        portfolio[stock] = portfolio.get(stock, 0) + qty    # Add each stock to the portfolio

    print("\nPortfolio Summary:")
    for stock, qty in portfolio.items():    # Printing the Stock Portfolio Summary
        print(f"{stock} - {qty} shares @ ${stock_prices[stock]} = ${stock_prices[stock] * qty}")

    print(f"Total Investment: {total_investment}")


starts_calculating()
