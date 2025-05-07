# User interactive dictionaries

print("\n --- Build your Business profile ---")

name = input("Business Name: ")
location = input("Enter Business Location: ")
open_status = input("Is it open now?(yes/no): ")
employees = input("Number of employees: ")

profile = {
    "name" : name,
    "location" : location,
    "open" : open_status,
    "employees" : employees
}

print("\n --- Your Business Profile ---")
for key, value in profile.items():
    print(f"{key.capitalize()} : {value}")