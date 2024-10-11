def maxProfit(prices):
   

    min_price = prices[0]  # Minimum price to buy
    max_profit = 0         # Maximum profit
    buy_day = 0            # Day to buy
    sell_day = 0           # Day to sell

    for i in range(1, len(prices)):
        # If selling on day i gives better profit, update max_profit and sell_day
        if prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            sell_day = i

        # If a lower price is found, update min_price and the buy_day
        if prices[i] < min_price:
            min_price = prices[i]
            buy_day = i

    return max_profit, buy_day, sell_day

# Example usage
prices = [7, 4, 4, 5, 4, 7]
profit, buy_day, sell_day = maxProfit(prices)

if profit > 0:
    print(f"Buy on day {buy_day + 1} and sell on day {sell_day + 1} for a profit of {profit}.")
else:
    print("No profitable day to buy and sell.")
