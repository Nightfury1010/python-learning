#if statement
is_raining = True
is_sunny = False
if is_raining:
    print("Take an umbrella")
elif is_sunny:
    print("Wear sunglasses")
else:
    print("No need for an umbrella")


# price = 1000000
is_buy_good = True 
if is_buy_good:
    price = price - price * .1    
else:   
    price = price - price * .2
print(f"Price after discount: {price}")    

#logical Operators
has_good_credit = True
has_high_income = False
if has_good_credit or has_high_income:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")


#comparison operators
temp =float( input('enter temperature in celsius: '))
if temp > 30:
    print("It's a hot day")
elif temp > 20:
    print("It's a nice day")
else:
    print("It's a cold day")   

name=len( input("Enter character: "))
if name < 3:
    print("character is short")  
elif name > 30:
    print("character is long")           
else:   
    print("character is medium")         

weight = float(input("Enter your weight: "))
weight_measure = input("Enter your weight measure (kg/lb): ")
if weight_measure == "kg":
    weight = weight * 2.20462
    print(f"Your weight in pounds is: {weight}")
elif weight_measure == "lb":
    weight = weight / 2.20462
    print(f"Your weight in kilograms is: {weight}")
else:
    print("Invalid weight measure")
    