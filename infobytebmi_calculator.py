import math #built in function 

height = float(input("enter height in meters:"))    #create variable == input string , use float for accurate values , applies to weight variable aswell
weight = float(input("enter weight in kgs:"))

def BMI(height , weight):   #define BMI formula to carry out calculations 
    bmi= weight/(height**2)

    if (bmi<16):                  # standard bmi measurements used worldwide to determine different categories 
        return "severely underweight" ,bmi      #if number falls within mentioned category , broadcast "category"

    elif(bmi>=16 and bmi<18.5):
        return "underweight" ,bmi

    elif(bmi>=18.5 and bmi<24.9):
        return "healthy" ,bmi

    elif(bmi>=24.9 and bmi<30):
        return "overweight" ,bmi

    elif(bmi>=30):
        return "obese" ,bmi


quote, bmi=BMI(height,weight)
print("your bmi is: {} and you are: {}" .format(bmi,quote))   # answer will be relayed according to following strings
