def bmi_calculator():
    wgt=float(input("enter weight in kgs-"))
    ht=float(input("enter height in cm-"))

    hgt=pow((ht/100),2)#height in metres
    bmi=wgt/hgt
    print(f" Your bmi is {bmi}")
            
    if bmi < 18.5:
                print("Category: Underweight")
    elif 18.5 <= bmi < 24.9:
        print("Category: Normal weight")
    elif 25 <= bmi < 29.9:
        print("Category: Overweight")
    else:
        print("Category: Obese")
bmi_calculator()