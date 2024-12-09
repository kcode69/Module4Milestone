class ItemsToPurchase:
    def __init__(self, item_name, item_price, item_quantity):
        self.item_name= str(item_name)
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
    def print_item_cost(self):
        print( self.item_name, self.item_quantity,'@ $',self.item_price, '= $', self.item_quantity*self.item_price)
        
itemname = ItemsToPurchase("none", 0, 0)
water = ItemsToPurchase("Bottled Water", 3.59, 6)

water.print_item_cost()
