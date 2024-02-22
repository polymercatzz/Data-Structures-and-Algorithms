"""Labs 11.03 - bubbleSort()"""
import json
def main(lst, index_, times=0):
    """Labs 11.03 - bubbleSort()"""
    current = 0
    sorted_ = False
    while current <= index_ and not sorted_:
        walker = index_
        sorted_ = True
        while walker > current:
            times += 1
            if lst[walker] < lst[walker-1]:
                sorted_ = False
                lst[walker], lst[walker-1] = lst[walker-1], lst[walker]
            walker -= 1
        current += 1
        print(lst)
    print("Comparison times: %d"%times)
main(json.loads(input()), int(input()))
