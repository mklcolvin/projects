# TODO: Import the required classes
# from product import Product

from product import Product

class DigitalProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price)

    def apply_discount(self, percent):
        # TODO: Override the apply_discount method with a special fixed 10% discount
        # TODO: Return self.price * 0.9 (10% off, regardless of the percent parameter)
        # TODO: This special discount ignores the percent parameter and always applies 10%
        return self.price * 0.9