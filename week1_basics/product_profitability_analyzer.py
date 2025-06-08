# Create a product profitability analyzer for an ecommerce site
# The deliverables are: 
 ## 1. Calculate the profit
 ## 2. Calculate the margin
 ## 3. Flag all products with a profit margin under 20 as low-margin products

products = ["Phone", "Laptop", "Headphones", "Monitor", "Mouse"]
costs = [300, 700, 50, 200, 20]
prices = [500, 1000, 80, 250, 25]

def calculate_profit(price, cost):
    return price - cost # Simple profit calculator

def calculate_margin(profit, cost):
    return (profit/ cost) * 100 # Margin calculator

def analyze_products(products, prices, costs):
    for i in range(len(products)):
        profit = calculate_profit(prices[i], costs[i])
        margin = calculate_margin(profit, costs[i])

        print(f"\n Product: {products[i]}")
        print(f"Cost: ${costs[i]}")
        print(f"Price: ${prices[i]}")
        print(f"Profit: {profit}")
        print(f"Margin: {margin:.2f}%")

        if margin < 20:
            print(f"Warning: Low-margin product!")

analyze_products(products, prices, costs)

