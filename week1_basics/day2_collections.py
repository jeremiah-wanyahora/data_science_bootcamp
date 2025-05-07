# Create and Manipulate lists
## Lists are used for when you have dynamic data that changes like names, transactions, prices

shopping_list = ["coffee", "tea", "milk", "bread"]

print("Shopping List:", shopping_list)
print("First Item:", shopping_list[0])
print("Third item:", shopping_list[+2])

# Using append() and remove() to manipulate created lists
# In this case we are using append to add eggs and remove to subtract milk 

shopping_list.append("eggs")
shopping_list.remove("milk")
print("Updated Shopping List:", shopping_list) 

# Tuples: These are used when you are using locked in data or facts that should not change.
# Trying to change a tuple could cause an error 

store_location = (1.7689, 35.0987) # latitude, longitude
print("Store Coordinates:", store_location)
print("Latitude:", store_location[0])
print("Longitude:", store_location[1])

# Dictionaries

## It is like a row in a database or a customer profile in CRM

business_profile = {
    "name" : "Farmers Choice",
    "location" : "Ruiru",
    "open" : True,
    "employees" : 20
}

print("Business Name:", business_profile["name"])

# Update info 

business_profile["employees"] = 15
business_profile["revenue"] = 2500000

print("\n --- Business Profile ---")
for key, value in business_profile.items():
    print(f"{key.capitalize()} : {value}")

