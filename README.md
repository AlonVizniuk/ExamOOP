# ExamOOP - Order Management System

A Python-based Object-Oriented Programming (OOP) demonstration project that implements an order management system with customer types, payment methods, and gift handling.

## Overview

This project demonstrates key OOP concepts including:

- **Inheritance**: `OrderVIP` extends `Order`, `Cat/Fish/Spider` extend `Animal`
- **Abstract Classes**: `Pet` and `Giftable` as abstract base classes
- **Multiple Inheritance**: `Cat` and `Fish` inherit from both `Animal` and `Pet`
- **Polymorphism**: Different price calculations for regular vs VIP orders
- **Encapsulation**: Auto-incrementing IDs for customers, items, and orders
- **Enumerations**: `CustomerType` and `PaymentType` enums

## Project Structure

```
ExamOOP/
├── main.py           # Main entry point with test scenarios
├── customer.py       # Customer class with favorites and gift management
├── customer_type.py  # CustomerType enum (REGULAR, VIP)
├── order.py          # Base Order class
├── order_vip.py      # VIP Order with discount calculation
├── item.py           # Item class for order items
├── payment_type.py   # PaymentType enum (CREDIT_CARD, CASH, CHECK, OTHER)
├── gift.py           # Gift class implementing Giftable
├── giftable.py       # Abstract Giftable interface
├── animal.py         # Base Animal class
├── pet.py            # Abstract Pet interface
├── cat.py            # Cat class (Animal + Pet)
├── fish.py           # Fish class (Animal + Pet)
├── spider.py         # Spider class (Animal only)
└── README.md         # This file
```

## Requirements

- Python 3.12+

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/AlonVizniuk/ExamOOP.git
   cd ExamOOP
   ```

2. No additional dependencies are required as the project uses only Python standard library.

## Usage

Run the main demonstration script:

```bash
python main.py
```

### Example Output

```
--- 🛒 Starting Order Management System Comprehensive Test ---

## 1. Customer & Item Creation (Unique ID Check)
Customer IDs used: 1, 2.
Item IDs used: 1, 2, 3.

## 2. Testing Regular Order & Auto-Favorites
Order REG ID: 1.
  Price Check: 55.00 (Expected 55.0)
  REG Favorites after order (Expected 2): {'Soda', 'Large Pizza'}

## 3. Testing VIP Order (Discount & Polymorphism)
Order VIP ID: 2.
  Price Check: 44.00 (Expected 44.0)

--- ✅ All Tests Complete ---
```

## Classes

### Customer

Represents a customer with personal information, customer type, and favorites management.

```python
from customer import Customer
from customer_type import CustomerType

# Create a VIP customer with 20% discount
customer = Customer(
    "John", "Doe", "john@example.com", "123 Main St",
    CustomerType.VIP, 0.20, [], None
)

# Add items to favorites
customer.add_item_to_favorite(item)
customer.remove_item_from_favorite(item)
```

### Order & OrderVIP

Create orders for customers with automatic favorite item tracking.

```python
from order import Order
from order_vip import OrderVIP
from payment_type import PaymentType
from datetime import datetime

# Regular order
order = Order(
    "Order Name", "Delivery Address", [item1, item2],
    customer, PaymentType.CASH, datetime.now()
)

# VIP order (applies customer discount)
vip_order = OrderVIP(
    "VIP Order", "Address", [item1, item2],
    vip_customer, PaymentType.CREDIT_CARD, datetime.now()
)
```

### Item

Simple item class with auto-incrementing ID.

```python
from item import Item

item = Item("Pizza", 50.0)
print(f"Item ID: {item.id}, Name: {item.name}, Price: {item.price}")
```

### Gift System

Implements the Giftable interface for gift management.

```python
from gift import Gift

gift = Gift()
customer.take_gift(gift)
customer.open_gift()  # Prints congratulations message
```

### Animals and Pets

Demonstrates multiple inheritance with abstract classes.

```python
from cat import Cat
from fish import Fish
from spider import Spider

cat = Cat("Whiskers")    # 4 legs, is a Pet
fish = Fish()            # 0 legs, is a Pet
spider = Spider()        # 8 legs, not a Pet
```

## Key Features

- **Auto-incrementing IDs**: Customers, Items, and Orders automatically receive unique IDs
- **Favorites Management**: Orders automatically add items to customer favorites
- **VIP Discounts**: VIP customers receive percentage-based discounts
- **Gift System**: Customers can receive and open gifts
- **Type Safety**: Uses enums for customer and payment types

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is for educational purposes as part of an OOP examination.
