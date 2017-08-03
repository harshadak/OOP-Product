class Product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def add_tax(self, tax):
        self.price = self.price + (self.tax * self.price)
        return self
    def return_item(self, reason):
        if self.reason == "defective":
            self.status = "defective"
            self.price = 0
        elif self.reason == "unopened":
            self.status = "for sale"
        elif self.reason == "opened":
            self.status = "used"
            self.discount = 0.2
        return self
    def display(self):
        print "Price:", self.price
        print "Item name:", self.item_name
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Cost:", self.cost
        print "Status:", self.status
product1 = Product(200, "Camera", "600g", "Nikon", "$1500")
product1 = Product(600, "Tripod", "300g", "XYZ", "$500")
product1.display()
