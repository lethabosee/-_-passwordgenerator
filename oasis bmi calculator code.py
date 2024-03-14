import math   #import calculator from built in funtions in order to determine the numbers 

def getWeight():   #variable weight,allocated/defined by a string 
    weight =float(input("please enter your weight in kgs :"))
    return weight     #results/print the following when calculaton is done

def getHeight():     #define height ,as a variable
    height =float(input("please enter your height in meters :"))
    return height

def calculateBMI(weight, height):    # Bmi formula 

    BMI = weight / (height * height)
    return BMI



if __name__== "__main__":
    print("welcome to the BMI calculator:)")

weight = getWeight()
height = getHeight()

bmi = calculateBMI(weight, height)
print(f"your final bmi is: {round(bmi, 2)}")

if (bmi<18.5):

        print("underweight")
        if (bmi>= 18.5 and bmi < 24.9):
            
            print("you are healthy")
        if (bmi>=24.9 and bmi <30 ):
            print("you are overweight" )

        if (bmi >=30):
            print("you are obese")
