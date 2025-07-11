# Creating a profitability dashboard that shows the name of the product, price, cost and flags low margin products

print(f"\n --- Profitability Dashboard ---")

# 1. Define Product Data

products = [
    {"name": "Premium Coffee", "cost": 800, "price": 1000},
    {"name": "Deluxe Tea", "cost": 300, "price": 350},
    {"name": "Chocolate Bar", "cost": 120, "price": 200},
    {"name": "Almond Milk", "cost": 450, "price": 450},  # zero profit
]

# 2. Define functions

def calculate_profit(price, cost):
    return price - cost

def calculate_margin(price, cost):
    if cost == 0:
        return 0
    return ((price - cost)/cost) * 100


# 3. Analyze products by looping

for product in products:
    name = product["name"]
    price = product["price"]
    cost = product["cost"]
    profit = calculate_profit(price, cost)
    margin = calculate_margin(price, cost)
    print(f"\n {name}")
    print(f"Cost: {cost} | Price: {price}")
    print(f"Profit: {profit}")
    print(f"Margin: {margin:.2f}%")
    if margin < 10:
        print("Low Margin! Consider repricing")


# Full code:

print(f"\n --- Profitability Dashboard ---")

products = [
    {"name": "Premium Coffee", "cost": 800, "price": 1000},
    {"name": "Deluxe Tea", "cost": 300, "price": 350},
    {"name": "Chocolate Bar", "cost": 120, "price": 200},
    {"name": "Almond Milk", "cost": 450, "price": 450},  # zero profit
]

def calculate_profit(price, cost):
    return price - cost

def calculate_margin(price, cost):
    if cost == 0:
        return 0
    return ((price - cost)/cost) * 100

for product in products:
    name = product["name"]
    cost = product["cost"]
    price = product["price"]
    profit = calculate_profit(price, cost)
    margin = calculate_margin(price, cost)
    print(f"\n {name}")
    print(f" Cost: {cost} | Price: {price}")
    print(f" Profit: {profit}")
    print(f" Margin: {margin:.2f}%")
    if margin < 10:
        print("Low pricing! Consider repricing")







