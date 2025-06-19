balance=1000

def check_balance():
    print(f"your acc balance is: {balance}")

def deposit(dep):
    global balance 
    balance += dep
    print("Amount deposited successfully ")
def withdraw(withdraw):

    global balance
    if withdraw > balance:
          print("Insufficient balance")
    else:
        balance -= withdraw
        print("Withdrawal successful")


while True:
    # Display menu
        print("Select operation:")
        print("1.Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        op= int(input("Enter the operation that needs to be done: "))
        if op == 4:
            print("Thanks for choosing priti atm! ")
            break

        if op==1:
             check_balance()
        elif op==2:
             amt=int(input("enter amount to be deposited-"))
             deposit(amt)
        elif op==3:
             amt=int(input("enter amount to be withdrawn-"))
             withdraw(amt)          
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

