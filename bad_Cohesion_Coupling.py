shop_floors = []


def register_shop_floor():
    name = input("Enter the name of the new shop floor: ")
    location = input("Enter the location of the shop floor: ")
    shop_floors.append({"Name": name, "Location": location})


def display_registered_shop_floors():
    for shop_floor in shop_floors:
        print(f"Name: {shop_floor['Name']}, Location: {shop_floor['Location']}")


while True:
    print("\nMachine Shop Floor Registration System")
    print("1. Register a New Shop Floor")
    print("2. Display Registered Shop Floors")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        register_shop_floor()
    elif choice == "2":
        display_registered_shop_floors()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3).")