def maximum_profit(prices):
    if len(prices)==0:
        return 0
    min_price = float('inf')
    max_price = 0
    for item in prices:
        min_price = min(min_price,item)
        profit = item-min_price
        max_price = max(max_price,profit)
    return max_price

n = input()
my_list = list(map(int, n.split()))  
result = maximum_profit(my_list)
print(result)