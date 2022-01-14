class Oder:
    def __init__(self, price, discount=0):
        self.price = price
        self.discount = discount

    def final_price(self) -> int:
        """Calculate final price"""
        if self.discount == 0:
            return self.price
        return self.price - self.discount(self.price)
