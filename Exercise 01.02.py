"""Exercise 01.02"""
class Food:
    """Food"""
    def __init__(self, food):
        self.food = food
    def random_foods(self):
        """radom"""
        pass
    def list_foods(self):
        """list"""
        print(sorted(self.food))
def main():
    """main"""
    food = Food(["Pizza", "Fried Chicken", "Hamburger", "Steak"])
    food.list_foods()
main()