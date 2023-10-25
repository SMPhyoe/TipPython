"""
Created on 25/10/2023/10/2023 - 2:19 pm
@author: sump
"""


class ShopFloor:
    def increase_points(self, shop_floor, num_machines):
        point_multipliers = {
            "Shop Floor 1": 5,
            "Shop Floor 2": 10,
            "Shop Floor 3": 15
        }
        if shop_floor in point_multipliers:
            points = point_multipliers[shop_floor] * num_machines
            print(f"{shop_floor}: Points increased by {points} for {num_machines} machines")
        else:
            print("Invalid shop floor.")


# Create an instance and use the handler
handler = ShopFloor()

shop_floor_name_1 = "Shop Floor 1"
shop_floor_name_2 = "Shop Floor 2"

num_machines_1 = 3  # For example, 3 machines on Shop Floor 1
num_machines_2 = 4  # For example, 4 machines on Shop Floor 2

handler.increase_points(shop_floor_name_1, num_machines_1)
handler.increase_points(shop_floor_name_2, num_machines_2)
