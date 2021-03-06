class Checkout:
    """Represents a shopping cart."""

    class discount:
        def __init__(self, nbrItems, price):
            self.nbrItems = nbrItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def addDiscount(self, item, nbrOfItems, price):
        discount = self.discount(nbrOfItems, price)
        self.discounts[item] = discount

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.prices:
            raise Exception("Bad Item")

        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def canCalculateItemDiscountedTotal(self, item, cnt, discount):
        total = 0
        nbrOfdiscounts = cnt/discount.nbrItems
        total += nbrOfdiscounts * discount.price
        remaining = cnt % discount.nbrItems
        total += remaining * self.prices[item]
        return total

    def canCalculateItemTotal(self, item, cnt):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.nbrItems:
                total += self.canCalculateItemDiscountedTotal(
                    item, cnt, discount)
            else:
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt
        return total

    def calculateTotal(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.canCalculateItemTotal(item, cnt)
        return total

    def readPricesFile(self, filename):
        with open(filename) as inFile:
            for line in inFile:
                tokens = line.split()
                self.addItemPrice(tokens[0], int(tokens[1]))
