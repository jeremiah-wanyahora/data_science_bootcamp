# Creating a business profile for stretch goal

customer_profile = {
    "name" : "Alice Mwangi",
    "location" : (1.2456, 34.6890), # tuple : fixed location
    "phone" : "+254789067544",
    "birth date" : (1995, 6, 15), # tuple :immutable DOB
    "preferences" : ["electronics", "fitness", "health"],
    "purchase_history" : {
        "2024-10-12" : ["blender", "phone"],
        "2025-02-23" : ["Treadmill", "dumbbells"]
    },
    "loyalty_tier" : "Gold"
}

print("\n --- Customer profile ---")
for key, value in customer_profile.items():
    print(f"{key.capitalize()} : {value}")