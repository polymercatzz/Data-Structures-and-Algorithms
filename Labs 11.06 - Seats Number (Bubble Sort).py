"""Labs 11.06 - Seats Number (Bubble Sort)"""
import json
def main(lst, index_, times=0):
    """Labs 11.06 - Seats Number (Bubble Sort)"""
    current = 0
    sorted_ = False
    while current <= index_ and not sorted_:
        walker = index_
        sorted_ = True
        while walker > current:
            times += 1
            if lst[walker][0] < lst[walker-1][0] or \
                (lst[walker][0] == lst[walker-1][0] and \
                 int(lst[walker][1:]) < int(lst[walker-1][1:])):
                sorted_ = False
                lst[walker], lst[walker-1] = lst[walker-1], lst[walker]
            walker -= 1
        current += 1
        print(lst)
    print("Comparison times: %d"%times)
main(json.loads(input()), int(input()))
