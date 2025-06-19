def calculator():
  while True:
     # Display menu
        print("\nSimple Calculator")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        operation=input("enter the operation(1/2/3/4/5)")

        if operation=="5":
          print("Exiting the calculator,Bye")
          break
        if operation in ['1', '2', '3', '4']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if operation == '1':
                print(f"{num1} + {num2} = {num1 + num2}")
            elif operation == '2':
                print(f"{num1} - {num2} = {num1 - num2}")
            elif operation == '3':
                print(f"{num1} * {num2} = {num1 * num2}")
            elif operation == '4':
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Invalid input, please choose a valid operation.")
calculator()


