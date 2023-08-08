# https://github.com/0x-Sarthak/Zomato-Cronicle-Python.git

def main():
    print("Welcome to Zomato Chronicles: The Great Food Fiasco!")

    # Step 2: Menu Mastery
    menu = {
        1: {
            "name": "Pizza",
            "price": 12.99,
            "availability": True
        },
        2: {
            "name": "Burger",
            "price": 8.99,
            "availability": False
        },
        # Add more dishes to the menu.
    }

    print("Menu:")
    for dish_id, dish_info in menu.items():
        print(f"{dish_id}. {dish_info['name']} - ${dish_info['price']:.2f} ({'Available' if dish_info['availability'] else 'Not Available'})")

if __name__ == "__main__":
    main()
