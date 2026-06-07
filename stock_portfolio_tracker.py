# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420
}

total_investment = 0

# Number of stocks the user wants to enter
num_stocks = int(input("Enter the number of stocks: "))

for i in range(num_stocks):
    stock_name = input("\nEnter stock symbol: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print(f"Investment in {stock_name}: ${investment}")
    else:
        print("Stock not found in the price list.")

print("\nTotal Investment Value: $", total_investment)

# Save result to a text file
with open("investment_report.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_investment}")

print("Investment report saved to 'investment_report.txt'")
