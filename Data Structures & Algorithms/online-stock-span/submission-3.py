class StockSpanner:

    def __init__(self):
        self.prices=[]
        self.span=[]
    def next(self, price: int) -> int:
        self.prices.append(price)
        self.span.append(1)
        curr_idx=len(self.prices)-1

        while(curr_idx-self.span[curr_idx]>=0):
            itr=curr_idx
            if(self.prices[itr]>=self.prices[itr-self.span[itr]]):
                self.span[curr_idx]+=self.span[itr-self.span[itr]]
                itr=itr-self.span[itr]
            else:
                break
        return self.span[curr_idx]




        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)