class StockProfitCalculator:
    def __init__(self, prices):
        self.prices = prices  # Store the stock prices

    def max_profit(self):
        total_profit = 0
        # Iterate through the prices
        for i in range(1, len(self.prices)):
            # If the price on day i is higher than day i-1, sell
            if self.prices[i] > self.prices[i - 1]:
                total_profit += self.prices[i] - self.prices[i - 1]  # Add to profit
        return total_profit  # Return the total profit


prices = [7, 1, 5, 3, 6, 8]  # Example stock prices
calculator = StockProfitCalculator(prices)
profit = calculator.max_profit()
print(f"Maximum profit: {profit}")
