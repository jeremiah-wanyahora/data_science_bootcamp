# Basic cleaning functions

def cleaned_whitespace(text):
    return text.strip()

def normalize_case(text):
    return text.lower()

def remove_specials(text):
    return text.replace("!", "").replace(" ", "-")

# Real World Application

raw_names = [" bOB   ", " jeNkiNs ", " peter "]

def customer_welcome(name_list):
    return[name.strip().title() for name in name_list]

print(customer_welcome(raw_names))



raw_names = [" bOB   ", " jeNkiNs ", " peter "]

def cleaned_names(name_list):
    return [name.strip().title() for name in name_list]

print(cleaned_names(raw_names))

raw_products = [" mouse   ", "  keyBoard", "   lApTop  "]

def cleaned_products(product_list):
    return[product.strip().title() for product in product_list]

print(cleaned_products(raw_products))

# Mini challenge 

def slugify(text):
    cleaned = text.strip().lower()
    cleaned = cleaned.replace(" ", "-").replace("!", "").replace("?", "")
    return cleaned

print(slugify("  PREmium? coffEe!! bEaNs!!!"))

# How data can be formatted professionally for output

name = "  jenKins  "
product = "   laPtOP  "


def customer_welcome(name, product):
    name = name.strip().title()
    product = product.strip().upper()
    print(f"Hello {name}, thank you for buying {product}!")

print(customer_welcome(name, product))

Stretch goal: Returning multiple customer_welcome messages using loops

buyers = ["  jenKins  ", "  aLex  ", "  marY  "]
products = ["   laPtOP  ", "   pHone  ", "   moNitor  "]

def customer_welcome(buyer, product):
    buyer = buyer.strip().title()
    product = product.strip().upper()
    print(f"Hello {buyer}, thank you for purchasing {product}!")



for buyer, product in zip(buyers, products):
    print(customer_welcome(buyer, product))