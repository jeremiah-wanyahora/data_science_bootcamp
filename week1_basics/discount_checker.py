# Discount checker

price = int(input("Enter product price: 1200"))
discount = 0

if price > 1000:
    discount = 0.1
    print("You get a 10% discount!")

elif price > 500:
    discount = 0.05
    print("You get a 5% discount!")

else:
    discount = 0 
    print("No discount available")

final_price = price * (1 - discount)
print(f"Final price after discount : {final_price}")