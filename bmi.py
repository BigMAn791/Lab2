def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / (height ** 2)
    print("BMI = " + str(bmi))


    if bmi < 18.5:
        print("You are underweight.")
    elif bmi >= 18.5 and bmi < 25:
        print("You are normal weight.")
    elif bmi >= 25 and bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")


calculate_bmi(weight=57, height=1.73)

