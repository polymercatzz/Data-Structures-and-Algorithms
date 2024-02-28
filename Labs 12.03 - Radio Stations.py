"""Labs 12.03 - Radio Stations"""
import json
def main(want, all_station):
    """main"""
    ans = []
    want_sta = []
    for i in all_station:
        want_sta.append([i.get("Name"), set(i["Cities"]) & want])
    while want:
        want_sta.sort(key=lambda x: len(x[1] & want), reverse=True)
        if want_sta[0][1] & want:
            want -= want_sta[0][1]
            ans.append(want_sta[0][0])
        else:
            break
        want_sta.pop(0)
    print(sorted(ans))
main(set(json.loads(input())), [json.loads(input()) for _ in range(int(input()))])
