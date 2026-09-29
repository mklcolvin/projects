# TODO: Import the required mixins
# from printablemixin import PrintableMixin
# from discountmixin import DiscountMixin

from printablemixin import PrintableMixin
from discountmixin import DiscountMixin

class Product(PrintableMixin, DiscountMixin):
    def __init__(self, name, price):
        # TODO: Initialize the product with name and price attributes
        # TODO: Set self.name = name
        # TODO: Set self.price = price
        self.name = name
        self.price = price 