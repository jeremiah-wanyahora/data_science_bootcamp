# Day 4: Loops Practice 

# 1. Loop through product list

products = ["Laptop", "Monitor", "Keyboard", "Mouse"]

print("\n --- Product Inventory ---")
for item in products:
    print(f"Product : {item}")

# 2. Loop through product prices using range()

print("\n --- Batch Processing ---")
for i in range(1, 8):
    print(f"Processing batch #{i}")

# 3. Loop through dictionary items

sales = {
    "Laptop" : 1200,
    "Keyboard" : 800,
    "Mouse" : 400

}

print("\n --- Product Prices ---")
for product, price in sales.items():
    print(f"{product} : ${price}")

# 4. Compute total & average prices

prices = [1200, 800, 60, 80, 150]
total = 0

for price in prices:
    total += price

average = total / len(prices)

print("\n --- Price Summary ---")
print(f"Total : ${total}")
print(f"Average : ${average:.2f}")

# 5. While loop basics

print("\n --- While Loop Example ---")
count = 0

while count < 3:
    print(f"Iteration {count + 1}")
    count += 1

# 6. [Stretch Goal] Product summary from user input

print("\n --- Product Summary ---")
prices = []

for i in range(5):
    price = float(input(f"Enter your price here{i + 1} : $"))
    prices.append(price)

total = sum(prices)
average = total / len(prices)

print("\n --- Summary ---")
print(f"Total : ${total}")
print(f"Average : ${average}")


# Stretch goal 2

products = ["Laptop", "Mouse", "Keyboard", "Laptop", "Monitor", "Mouse", "Monitor", "Keyboard"]
prices = [1200, 600, 800, 1200, 900, 600, 900, 800]

for i in range(len(products)):
    print(f"{products[i]} : ${prices[i]}")

# Calculate the total and average

total = 0
for price in prices:
    total += price

# Average 

average = total/ len(prices)

print("\n --- Prices Summary ---")
print(f"Total : ${total}")
print(f"(Average : ${average})")


