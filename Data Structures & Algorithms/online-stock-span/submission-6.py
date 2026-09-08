class StockSpanner:

    def __init__(self):
        self.prices=[]
        self.span=[]

    def next(self, price: int) -> int:
        span=1
        while(self.prices and self.prices[-1]<=price):
            span+=self.span[-1]
            self.prices.pop()
            self.span.pop()
        self.prices.append(price)
        self.span.append(span)
        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)