# Created by Su Myat Phyoe at 11:20 am 22/10/2023 using PyCharm

class ShopFloor:
    def __init__(self, name, location):
        self.name = name
        self.location = location


class ShopFloorRegistry:
    def __init__(self):
        self.shop_floors = []

    def register_shop_floor(self, shop_floor):
        self.shop_floors.append(shop_floor)

    def display_registered_shop_floors(self):
        for shop_floor in self.shop_floors:
            print(f"Name: {shop_floor.name}, Location: {shop_floor.location}")


def main():
    registry = ShopFloorRegistry()

    while True:
        print("\nMachine Shop Floor Registration System")
        print("1. Register a New Shop Floor")
        print("2. Display Registered Shop Floors")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            name = input("Enter the name of the new shop floor: ")
            location = input("Enter the location of the shop floor: ")
            new_shop_floor = ShopFloor(name, location)
            registry.register_shop_floor(new_shop_floor)
            print(f"Shop floor '{name}' registered successfully!")
        elif choice == "2":
            registry.display_registered_shop_floors()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3).")


if __name__ == "__main__":
    main()
