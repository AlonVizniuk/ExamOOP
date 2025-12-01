from datetime import datetime
from customer import Customer
from customer_type import CustomerType
from item import Item
from order import Order
from order_vip import OrderVIP
from payment_type import PaymentType
from gift import Gift
from giftable import Giftable

# Almost all the test cases within this system were initially written with the assistance of an AI tool.
# However, they have been thoroughly reviewed and manually validated by me
# to ensure full compliance with all conditions and requirements outlined in the exam specification.

# --- Helper Function for Property Dump ---
def print_properties(obj, title: str):
    """Prints all attributes and their values for an object."""
    print(f"\n--- {title} PROPERTIES ---")
    for attr, value in obj.__dict__.items():
        # Handle enums and complex objects gracefully for printing
        if isinstance(value, list) and all(isinstance(i, Item) for i in value):
            item_names = [i.name for i in value]
            print(f"  {attr:<20}: {len(item_names)} items ({item_names})")
        elif hasattr(value, 'name') and isinstance(value, (CustomerType, PaymentType)):
            print(f"  {attr:<20}: {value.name} ({value.value})")
        elif isinstance(value, Customer):
            print(f"  {attr:<20}: Customer (ID {value.id})")
        elif isinstance(value, Giftable):
            print(f"  {attr:<20}: {value.__class__.__name__}")
        else:
            print(f"  {attr:<20}: {value}")
    print("----------------------------")


def main():
    print("--- 🛒 Starting Order Management System Comprehensive Test ---")

    # 1. SETUP: Create Customers and Items
    print("\n## 1. Customer & Item Creation (Unique ID Check)")

    customer_vip = Customer(
        "Vicky", "Peterson", "vicky@corp.com", "123 Main St",
        CustomerType.VIP, 0.20, [], None
    )
    customer_reg = Customer(
        "Reginald", "Smith", "reg@home.com", "456 Side Rd",
        CustomerType.REGULAR, None, [], None
    )

    item_pizza = Item("Large Pizza", 50.0)  # ID 1
    item_soda = Item("Soda", 5.0)  # ID 2
    item_extra_soda = Item("Soda", 5.0)  # ID 3 (Same name, different ID)
    item_fries = Item("Fries", 15.0)  # ID 4 (For manual update test)

    order_items_1 = [item_pizza, item_soda]  # Base price: 55.0
    order_items_2 = [item_pizza, item_extra_soda]  # Base price: 55.0

    print(f"Customer IDs used: {customer_vip.id}, {customer_reg.id}.")
    print(f"Item IDs used: {item_pizza.id}, {item_soda.id}, {item_extra_soda.id}.")

    # Print properties of VIP Customer
    print_properties(customer_vip, "VIP Customer Properties")

    # ----------------------------------------------------------------------

    # 2. TEST: Regular Order (Base Pricing & Auto-Favorites)
    print("\n## 2. Testing Regular Order & Auto-Favorites")

    order_reg = Order(
        "Reg Order 1", customer_reg.delivery_address, order_items_1,
        customer_reg, PaymentType.CASH, datetime.now()
    )
    print(f"Order REG ID: {order_reg.order_id}.")
    print(f"  Price Check: {order_reg.total_price:.2f} (Expected 55.0)")

    # Check Auto-Favorites (Pizza and Soda added)
    print(f"  REG Favorites after order (Expected 2): {customer_reg.get_items_names()}")

    # Print properties of Regular Order
    print_properties(order_reg, "Regular Order Properties")

    # ----------------------------------------------------------------------

    # 3. TEST: VIP Order (Discounted Pricing)
    print("\n## 3. Testing VIP Order (Discount & Polymorphism)")

    order_vip = OrderVIP(
        "VIP Order 1", customer_vip.delivery_address, order_items_2,
        customer_vip, PaymentType.CREDIT_CARD, datetime.now()
    )
    # Base Price: 55.0. Discount: 20% (11.0). Final Price: 44.0
    print(f"Order VIP ID: {order_vip.order_id}.")
    print(f"  Price Check: {order_vip.total_price:.2f} (Expected 44.0)")

    # Check Auto-Favorites (Should not add duplicates, size should remain 2)
    print(f"  VIP Favorites after order (Expected 2): {customer_vip.get_items_names()}")

    # Print properties of VIP Order
    print_properties(order_vip, "VIP Order Properties")

    # ----------------------------------------------------------------------

    # 4. TEST: Customer Favorites Manual Update (Add/Remove)
    print("\n## 4. Testing Manual Favorite Item Updates")

    # 4a. Add
    print(f"  VIP Favorites BEFORE manual ADD (Expected 2): {len(customer_vip.favorite_items)}")
    customer_vip.add_item_to_favorite(item_fries)
    print(f"  VIP Favorites AFTER ADD (Expected 3): {customer_vip.get_items_names()}")

    # 4b. Remove
    customer_vip.remove_item_from_favorite(item_pizza)
    print(f"  VIP Favorites AFTER REMOVE Pizza (Expected 2): {customer_vip.get_items_names()}")

    # ----------------------------------------------------------------------

    # 5. TEST: Gift Management (take_gift / open_gift)
    print("\n## 5. Testing Gift Management (take_gift / open_gift)")

    new_gift = Gift()

    # --- Before giving gift ---
    print(f"  VIP Customer Gift BEFORE take_gift: {customer_vip.gift}")

    customer_vip.take_gift(new_gift)

    # --- After giving gift ---
    print(f"  VIP Customer Gift AFTER take_gift: {customer_vip.gift.__class__.__name__}")
    print("  Attempting to open gift:")
    customer_vip.open_gift()

    # --- Testing open_gift failure if no gift exists ---
    print("  Attempting to open gift when no gift exists:")
    customer_reg.open_gift()

    # ----------------------------------------------------------------------

    # 6. TEST: VIP Check Constraint (Error Handling)
    print("\n## 6. Testing VIP Check Constraint (Negative Test)")

    try:
        # This call is expected to fail and raise the exception
        OrderVIP(
            "Fake VIP Order", customer_reg.delivery_address, order_items_1,
            customer_reg, PaymentType.CASH, datetime.now()
        )
        print("  FAILURE: Exception was NOT raised! (Test Failed)")

    except Exception as e:
        if "VIP order with customer type 'Regular'" in str(e):
            print(f"  SUCCESS: Caught expected error: {e}")
        else:
            print(f"  FAILURE: Caught unexpected error: {e}")

    print("\n--- ✅ All Tests Complete ---")


# Run the main function
if __name__ == "__main__":
    main()