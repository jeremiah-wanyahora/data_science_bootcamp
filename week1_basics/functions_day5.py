def greet_user(name):
    print(f"Hello {name}! Welcome to Day % of your bootcamp")

greet_user("Peter")

# Functions that returns value

def calculate_profit(revenue, cost):
    profit = revenue - cost
    return profit

profit = calculate_profit(500, 1000)
print(f"Profit is: ${profit}")

def calculate_sales(price, quantity):
    sales = price * quantity
    return sales

sales = calculate_sales(12, 2000)
print(f"Total sales are: ${sales}")

# Functions with default parameters

def describe_product(name = "Laptop", price = 23000):
    print(f"The product is a {name} and it costs {price}")

describe_product("Mouse", 3000)
describe_product("Keyboard", 5000)

