# Code #69: Create a Class to Manage a Shopping Cart
"""
    🧠 Why This Matters?
    Used in:
    - 🛍️ E-commerce platforms
    - 🛒 POS systems and digital storefronts
    - 🧾 Order staging & inventory tracking
    - 💻 Multi-user session handlin
"""
# Tier: Intermediate
# Goal: Track how many shopping cars have been created using a class variable, and manage items Inside each cart

# Python Code
class ShoppingCart:
    cart_count = 0 # Class variable to track carts created

    def __init__(self):
        self.items = [] # Each cart has its own item list

        ShoppingCart.cart_count += 1
    
    def add_item(self, item):
        self.items.append(item)
        print(f"Added '{item}' to cart.")

    def view_cart(self):
        return f"Items in cart: {self.items}"
    
    @classmethod
    def total_carts(cls):
        return cls.cart_count
    
# Sample Usage
cart1 = ShoppingCart()
cart1.add_item("Laptop")
cart1.add_item("Mouse")
print(cart1.view_cart())

cart2 = ShoppingCart()
cart2.add_item("Keyboard")
print(cart2.view_cart())

print("Total carts creaed:", ShoppingCart.total_carts())

# Sample Output
"""
    Added 'Laptop' to cart.
    Added 'Mouse' to cart.
    Items in cart: ['Laptop', 'Mouse']
    Added 'Keyboard' to cart.
    Items in cart: ['Keyboard']
    Total carts created: 2
"""

# Concept Breakdown
"""
    Concept         Description
    ----------------------------
    cart_count      Tracks how many carts have been created
    items           List of products per cart
    add_item()      Adds product to specific cart
    @classmethod    Access class-level data (cart count)
"""