from abc import ABC, abstractmethod


class Discount(ABC):
    @staticmethod
    @abstractmethod
    def count_discount():
        pass


class MorningDiscount(Discount):
    @staticmethod
    def count_discount():
        return 0.25


class ElderDiscount(Discount):
    @staticmethod
    def count_discount():
        return 0.8


class Oder:
    def __init__(self, price, discount=0):
        self.price = price
        self.discount = discount

    def final_price(self) -> int:
        """Calculate final price"""
        if self.discount == 0:
            return self.price
        return self.price - self.price * self.discount.count_discount()
