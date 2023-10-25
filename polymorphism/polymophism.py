"""
Created on 25/10/2023/10/2023 - 4:09 pm
@author: sump
"""


# Define a common interface for ShopFloor
class ShopFloor:
    def increase_points(self, num_machines):
        pass


# Define classes for different shop floors
class ShopFloor1(ShopFloor):
    def increase_points(self, num_machines):
        # Increase points based on the number of machines for Shop Floor 1
        points = num_machines * 5
        print(f"Shop Floor 1: Points increased by {points} for {num_machines} machines")


class ShopFloor2(ShopFloor):
    def increase_points(self, num_machines):
        # Increase points based on the number of machines for Shop Floor 2
        points = num_machines * 10
        print(f"Shop Floor 2: Points increased by {points} for {num_machines} machines")


class ShopFloor3(ShopFloor):
    def increase_points(self, num_machines):
        # Increase points based on the number of machines for Shop Floor 3
        points = num_machines * 15
        print(f"Shop Floor 3: Points increased by {points} for {num_machines} machines")


# Handler class
class ShopFloorHandler:
    def increase_points(self, shop_floor, num_machines):
        shop_floor.increase_points(num_machines)


# Create instances and use the handler
handler = ShopFloorHandler()


shop_floor_1 = ShopFloor1()
shop_floor_2 = ShopFloor2()

num_machines_1 = 3  # For example, 3 machines on Shop Floor 1
num_machines_2 = 4  # For example, 4 machines on Shop Floor 2

handler.increase_points(shop_floor_1, num_machines_1)
handler.increase_points(shop_floor_2, num_machines_2)
