"""Labs 12.02 - (1) Item Class"""
class Item():
    """ITEM"""
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def get_name(self):
        """get name"""
        return self.name

    def get_price(self):
        """get price"""
        return self.price

    def get_weight(self):
        """get weight"""
        return self.weight

    def get_cost(self):
        """get weight"""
        return self.price/self.weight

def main():
    """mainn"""
    import json
    item_in = json.loads(input())
    item = Item(item_in["name"], item_in["price"], item_in["weight"])
    print(item.get_name(), item.get_price(), item.get_weight(), sep='\n')

main()
