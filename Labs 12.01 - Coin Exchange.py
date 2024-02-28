"""Labs 12.01 - Coin Exchange"""
import json
def convert_key(data):
    """JSON"""
    return {int(k): v for k, v in data.items()}

def main(money):
    """mainnn"""
    ans = {10: 0, 5: 0, 2: 0, 1: 0}
    data = convert_key(json.loads(input()))
    print("Amount: %d"%money)
    for i in data.keys():
        use_coin = min(data.get(i), money//i)
        ans[i] = use_coin
        money -= use_coin*i
    if not money:
        print("Coin exchange result:")
        for i, j in ans.items():
            print("  %d baht = %d coins"%(i, j))
        print("Number of coins: %d"%sum(ans.values()))
    else:
        print("Coins are not enough.")
main(int(input()))
