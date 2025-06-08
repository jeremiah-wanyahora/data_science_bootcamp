# Put functions in a loop to create automation

revenues = [1500, 1200, 900]
costs = [1200, 900, 500]

# Create the helper function

def calculate_profit(revenues, costs):
    return revenues - costs # Simple profit calculation

# Create the main function

def calculate_all_profit(revenues, costs):
    for i in range(len(revenues)):
        profit = calculate_profit(revenues[i], costs[i])
        print(f"Transaction{i+1} profit: ${profit}")

calculate_all_profit(revenues, costs)

















