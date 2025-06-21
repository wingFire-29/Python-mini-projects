menu={
    "Apples":50,
    "Mango":45,
    "Banana":10,
    "kiwi":40,
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

    fruit=input("Add to cart ,choose the fruit or type done : ")
    if fruit=="done" or fruit=="Done":
        break
    elif fruit in menu:
        cart.append(fruit)
        n=int (input("Enter the quantity: "))
    else:
        print("Not available")
        # for fruit in menu.values():

print(f"Your cart {cart}")        
