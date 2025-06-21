Prices={
    "Apples":50,
    "Mango":45,
    "Banana":10,
    "Kiwi":40,
    "Orange":30
}

cart=[]
while True:
# menu list
    print("Apples,50rs/kg")
    print("Mango,45 rs/kg")
    print("Banana,10/pc")
    print("Kiwi,40/pc")
    print("Orange,30rs/kg")

    fruit=input("Add to cart ,choose the fruit or type done : ").title()
    if fruit=="Done":
        break
    elif fruit in Prices:
        n=int (input("Enter the quantity: "))
        cart.append((fruit,n))

    else:
        print("Not available")
        # for fruit in menu.values():

print(f"Your cart {cart}")    
total_bill=0
for fruit,n in cart:
    total=Prices[fruit]*n
    print(f"{fruit} x {n} = ₹{total}")    
    total_bill+=total
print(f"Your total bill for this cart is: ₹{total_bill}")
      