Height = float(input("Enter your height in centimeteres: "))
Weight = float(input("Enter your weight in kilograms: "))
h2 = Height/10000
bmi = Weight/(h2*Height)
print("your BMI is: ",bmi)
if bmi>0:
    if(bmi<=25):
        print("you are underwight")
    elif(bmi >=18,5 and bmi <=25):
        print("you are healthy")
    else:
        print("you are overweight")
else:
    print("enter valid credentials")                
