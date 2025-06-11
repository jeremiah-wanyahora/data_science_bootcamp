# Stretch goal to create roi calculator

revenues = [1500, 1200, 900]
costs = [1100, 900, 500]

def calculate_roi(revenues, costs):
    for i in range(len(revenues)):
        roi = (revenues[i] - costs[i])/costs[i]
        print(f"Campaign{i+1} ROI:{roi:.2%}")

calculate_roi(revenues, costs) 



