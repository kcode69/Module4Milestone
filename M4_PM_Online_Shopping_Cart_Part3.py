class ItemsToPurchase:
    def __init__(self, item_name, item_price, item_quantity):
        self.item_name = str(item_name)
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)

    def print_item_cost(self):
        print( self.item_name, self.item_quantity,'@ $',f'{self.item_price:.2f}', '= $', f'{self.item_quantity*self.item_price:.2f}', '\n')


#initiate total_items to 0  and sum_total_items to 0      
total_items = 0
sum_total_items = 0

# get the total number of items to set total_items
print('How many different items do you have today?')
total_items = int(input())

#if total items are 0
if total_items == 0:
    print('Sorry you didnot find what you were looking for')

print("Total number of items is", total_items)

#for loop for incrementing through items, price, quantity and summing
for i in range (0,total_items):
    print('\nWhat is item', i + 1)
    it_name = str(input())
    print('\nWhat is the price of item', i + 1)
    it_price = float(input())
    print('\nWhat is the quantity of item', i + 1) 
    it_quantity = int(input())
    it_name = ItemsToPurchase(it_name, it_price, it_quantity)
    it_name.print_item_cost()
    sum_total_items = sum_total_items + it_price*it_quantity

print('The total for today is: $', f'{sum_total_items:.2f}')