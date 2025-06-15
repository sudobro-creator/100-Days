import time

# Users (username: password)
users = {
    "admin": "1234"
}

# Products in store
products = {
    "apple": 100,
    "banana": 50,
    "milk": 200,
    "bread": 150
}

# Discount codes
discounts = {
    "SAVE10": 10,
    "SAVE20": 20
}

cart = {}
current_user = None

def signup():
    username = input("Choose a username: ")
    if username in users:
        print("❌ Username already exists.")
    else:
        password = input("Choose a password: ")
        users[username] = password
        print("✅ Sign-up successful. You can now log in.")

def login():
    global current_user
    username = input("Username: ")
    password = input("Password: ")
    if users.get(username) == password:
        current_user = username
        print(f"✅ Welcome back, {username}!")
        return True
    else:
        print("❌ Invalid credentials.")
        return False

def show_products():
    print("\n🛍️ Available Products:")
    for item, price in products.items():
        print(f"{item.title()} - ₦{price}")
    print()

def add_to_cart(item, quantity):
    if item in products:
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
        print(f"✅ {quantity} x {item.title()} added to cart.")
    else:
        print("❌ Product not found.")

def show_cart():
    if not cart:
        print("🛒 Your cart is empty.")
        return
    print("\n🛒 Your Cart:")
    total = 0
    for item, quantity in cart.items():
        price = products[item] * quantity
        total += price
        print(f"{item.title()} x {quantity} = ₦{price}")
    print(f"Total (before discount): ₦{total}\n")

def checkout():
    if not cart:
        print("🛒 Cart is empty. Nothing to checkout.")
        return
    show_cart()
    total = sum(products[item] * qty for item, qty in cart.items())

    code = input("Enter discount code (or press Enter to skip): ").strip().upper()
    if code in discounts:
        discount = discounts[code]
        discount_amount = total * (discount / 100)
        total -= discount_amount
        print(f"🎉 Discount applied: {discount}% off (₦{int(discount_amount)} saved)")
    elif code == "":
        print("No discount code applied.")
    else:
        print("❌ Invalid or no discount code applied.")

    print(f"💳 Final Total: ₦{int(total)}")

    # Save receipt to file
    with open(f"receipt_{current_user}.txt", "w") as file:
        file.write(f"Receipt for {current_user} - {time.ctime()}\n")
        for item, qty in cart.items():
            file.write(f"{item} x {qty} = ₦{products[item]*qty}\n")
        file.write(f"\nTotal Paid: ₦{int(total)}\n")
        if code in discounts:
            file.write(f"Discount Code: {code} ({discounts[code]}%)\n")
        file.write("Thank you for shopping!\n")
    
    print("🧾 Receipt saved. Thank you for shopping!\n")
    cart.clear()

# -------- Program Entry Point --------
print("=== Welcome to the Shopping Cart System ===")

while True:
    print("\n1. Login")
    print("2. Sign Up")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        if login():
            break
    elif choice == "2":
        signup()
    elif choice == "3":
        exit("Goodbye!")
    else:
        print("❌ Invalid choice.")

# --- Main Menu After Login ---
while True:
    print("\n--- Main Menu ---")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Logout")
    
    action = input("Choose an option: ")

    if action == "1":
        show_products()
    elif action == "2":
        item = input("Enter product name: ").lower()
        qty = input("Enter quantity: ")
        if qty.isdigit():
            add_to_cart(item, int(qty))
        else:
            print("❌ Quantity must be a number.")
    elif action == "3":
        show_cart()
    elif action == "4":
        checkout()
    elif action == "5":
        print("🔒 Logged out.")
        break
    else:
        print("❌ Invalid option.")
1