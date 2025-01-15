
def total_bill(price,  quantity):
    total_price = price * quantity # total_price = 150 * 4 = 600
    return total_price

total = total_bill(quantity=4, price=150) # total = 600
print(f"The total price of your purchase is {total}.")