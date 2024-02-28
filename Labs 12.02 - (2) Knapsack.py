"""Labs 12.02 - (2) Knapsack"""
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

def knapsack(amount, weight, total=0):
    """knapsack"""
    lst_item_sort = []
    for i, j in enumerate(amount):
        cost = j.get_cost()
        lst_item_sort.append([i, cost])
    lst_item_sort.sort(key=lambda x: (-x[1], x[0]))
    print("Knapsack Size: %s kg"%weight)
    print("===============================")
    for i in lst_item_sort:
        user = amount[i[0]]
        if weight-user.get_weight() >= 0:
            print("%s -> %s kg -> %d THB"%(user.get_name(), user.get_weight(), user.get_price()))
            weight -= user.get_weight()
            total += user.get_price()
        else:
            break
    print("Total: %d THB"%total)

def main():
    """mainn"""
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(
            Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(items, knapsack_capacity)
main()
