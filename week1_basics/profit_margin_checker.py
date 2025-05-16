cost = int(input("Enter cost here: "))
revenue = int(input("Enter revenue here: "))
margin = revenue - cost

if margin > 0 and margin < 100:
    print("Low profit margin")
elif margin >= 100:
    print("High profit margin")
else:
    print("Loss detected")
profit_margin = 1 * margin
print(f"Final profit margin : {profit_margin}")