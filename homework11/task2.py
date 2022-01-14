from typing import Optional


class Oder:
    def __init__(self, price: float, discount: Optional = None):
        self.price = price
        self.discount = discount

    def final_price(self) -> float:
        """Calculate final price"""
        if self.discount:
            return self.price - self.discount(self)
        return self.price
