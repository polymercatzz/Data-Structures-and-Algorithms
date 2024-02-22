"""Labs 11.04 - Seats Number (Insertion Sort)"""
import json
def main(lst, index_, times=0):
    """Labs 11.04 - Seats Number (Insertion Sort)"""
    current = 1
    for _ in range(current, index_+1):
        walker = current-1
        while walker >= 0:
            if lst[walker+1][0] < lst[walker][0] or \
                (lst[walker+1][0] == lst[walker][0] and \
                int(lst[walker+1][1:]) <= int(lst[walker][1:])):
                lst[walker], lst[walker+1] = lst[walker+1], lst[walker]
                times += 1
            else:
                times += 1
                break
            walker -= 1
        print(lst)
        current += 1
    print("Comparison times: %d"%times)
main(json.loads(input()), int(input()))
