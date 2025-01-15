def order(item, quan):
    print(f"You ordered {quan} {item}")

# passing the argument orderly 
order("apple", 15)

# passing the argument unorderly 
order(5, "apple") # item = 5, quan = "apple"

order(item="egg", quan="12")

def total_bill(price,  quantity):
    total_price = price * quantity
    print(f"The total price of your purchase is {total_price}.")

total_bill(quantity=4, price=150)