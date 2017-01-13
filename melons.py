"""This file should have our order classes in it."""

import random
# import datetime
# now = datetime.datetime.now()
# now.weekday() >>> will give day of the week in number; Mon-Friday (0-4)
# now.hour() >>> this will give 24hour time



class AbstractMelonOrder(object):
    """ Parent class calcuates total price and shipping status"""

    def __init__(self, species, qty, tax, order_type):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = tax
        self.order_type = order_type

    def get_base_price(self):
        """Generates random price between 5 to 9 inclusive."""

        base_price = random.randint(5, 9)
        return base_price

    def get_total(self):
        """Calculate price."""

        if self.species == "Christmas melon":
            base_price = 1.5 * self.get_base_price()
        else:
            base_price = self.get_base_price()

        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(DomesticMelonOrder, self).__init__(species, qty, 0.08, "domestic")


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty, 0.17, "international")
        self.country_code = country_code

    def get_total(self):
        """Calculate price and add fee for low melon sales."""

        total = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            return total + 3
        else:
            return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A domestic Government melon order"""

    def __init__(self, species, qty):
        """ Initializes melon order attributes"""

        super(GovernmentMelonOrder, self).__init__(species, qty, 0, "domestic")
        self.passed_inspection = False

    def mark_inspection(self, passed=True):
        """Set passed_inspection to user input, default to true"""

        self.passed_inspection = passed
