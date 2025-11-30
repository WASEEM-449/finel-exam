products = [
    {"name": "Laptop", "price": 3000},
    {"name": "Mobile", "price": 2000},
    {"name": "Headphones", "price": 500},
    {"name": "Monitor", "price": 1500},
    {"name": "Keyboard", "price": 300}
]

def show_products():
    print("\n=== Product List ===")
    for i, product in enumerate(products, 1):
        print(f"{i}- {product['name']} - Price: {product['price']} SAR")
    print("=" * 30)

def select_product():
    show_products()
    
    choice = int(input("\nSelect product number: "))
    
    if 1 <= choice <= len(products):
        return choice - 1
    else:
        print("Invalid number!")
        return None

index = select_product()
if index is not None:
    product = products[index]
    price = product['price']
    vat = price * 0.15 
    total = price + vat
    
    print(f"\n=== Product Details ===")
    print(f"Product: {product['name']}")
    print(f"Price: {price} SAR")
    print(f"VAT (15%): {vat} SAR")
    print(f"Total Price: {total} SAR")