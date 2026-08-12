#Iub Grading Policy

number = int(input("Enter number: "))

if 0<= number <=44:
    print (f"The student number is {number} and grade is F and the grade point is 0.0")

elif 45<= number <=49:
    print (f"The student number is {number} and grade is D and the grade point is 1.0")

elif 50<= number <=54:
    print (f"The student number is {number} and grade is D+ and the grade point is 1.3")

elif 55<= number <=59:
    print (f"The student number is {number} and grade is C- and the grade point is 1.7")

elif 60<= number <=64:
    print (f"The student number is {number} and grade is C and the grade point is 2.0")

elif 65<= number <=69:
    print (f"The student number is {number} and grade is C+ and the grade point is 2.3")

elif 70<= number <=74:
    print (f"The student number is {number} and grade is B- and the grade point is 2.7")

elif 75<= number <=79:
    print (f"The student number is {number} and grade is B and the grade point is 3.0")

elif 80<= number <=84:
    print (f"The student number is {number} and grade is B+ and the grade point is 3.3")

elif 85<= number <=89:
    print (f"The student number is {number} and grade is A- and the grade point is 3.7")

elif 90<= number <=100:
    print (f"The student number is {number} and grade is A and the grade point is 4.0")

else:
    print("Invalid Number! Please enter a number between 0-100")

