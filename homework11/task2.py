class Oder:
    def __init__(self, price, discount=None):
        self.price = price
        self.discount = discount

    def final_price(self) -> int:
        """Calculate final price"""
        if self.discount:
            return self.price - self.discount(self)
        return self.price
