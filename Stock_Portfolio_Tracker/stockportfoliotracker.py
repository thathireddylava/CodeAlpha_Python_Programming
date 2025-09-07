stocks = {"AAPL": 180, "TSLA": 250, "AMZN": 140, "MSFT": 310, "GOOG": 125}
portfolio = {}
total_investment = 0

n = int(input("Enter number of stocks you want to add: "))

for _ in range(n):
    name = input("Enter stock symbol: ").upper()
    qty = int(input(f"Enter quantity of {name}: "))
    if name in stocks:
        portfolio[name] = qty
        total_investment += stocks[name] * qty
    else:
        print(f"{name} not found in stock list.")

print("\nYour Portfolio:")
for name, qty in portfolio.items():
    print(f"{name} - {qty} shares @ {stocks[name]} = {stocks[name]*qty}")

print("\nTotal Investment Value:", total_investment)

# Optional: Save to file
with open("portfolio.txt", "w") as f:
    f.write("Stock Portfolio Report\n")
    for name, qty in portfolio.items():
        f.write(f"{name} - {qty} shares @ {stocks[name]} = {stocks[name]*qty}\n")
    f.write(f"\nTotal Investment Value: {total_investment}")
