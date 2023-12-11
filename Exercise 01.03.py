"""Exercise 01.03"""
class Food:
    """Food"""
    def __init__(self, food):
        self.food = food
    def list_foods(self):
        """list"""
        print(sorted(self.food))
    def add_food_item(self, name):
        """add_food_item"""
        self.food += [name]
def main():
    """main"""
    food = Food(["Pizza", "Fried Chicken", "Hamburger", "Steak"])
    for _ in range(int(input())):
        food.add_food_item(input())
    food.list_foods()
main()
