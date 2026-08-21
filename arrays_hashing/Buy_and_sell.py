prices = [10,1,5,6,7,1]
min_price = prices[0]
max_profit = 0
for price in prices:
    min_price = min(min_price,price)
    profit = price - min_price
    max_profit = max(max_profit,profit)
print(max_profit)