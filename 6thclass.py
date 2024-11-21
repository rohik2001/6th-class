'''mark=int(input('Enter your mark: ')) 
attendance=int(input('Enter your attendance: ')) 
if mark>=80 and mark<=100:
    print("your grade is A+")
    grade='A+'
elif mark>=70 and mark<=79:
    print("your grade is A")
    grade='A'
elif mark>=60 and mark<=69:
    print("your grade is B")
    grade='B'
elif mark>=50 and mark<=59:
    print("your grade is C")
    grade='C'
elif mark>=40 and mark<=49:
    print("your grade is D")
    grade='D'
elif mark>=33 and mark<=39:
    print("your grade is D")
    grade='D'
else:
    print('Your grade is F')
    grade='F'
#check if student  can  participant or not
grade_list=['C','B','A','A+'] #list
if grade in grade_list and attendance>=70:
    print(f'Grade: {grade}, Attendence: {attendance}% - You are eligible to participate for the Exam')
else:
    print(f'Grade: {grade}, Attendence: {attendance}% - You are not eligible to participate for the Exam')'''
'''



height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
BMI= weight/(height*height)
print("Your BMI is", BMI)
if BMI <= 16:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
elif BMI <= 34.9:
    print("You are severely over weight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")'''



age=int(input("Age: "))
gender=input("enter your gender (male/female)").strip().capitalize()
weight=float(input("Enter your weight in kilogram: "))
height=float(input("Enter your height in meter: "))
BMI=weight/(height**2)
if BMI <18.5:
    category="Underweight"
elif BMI>-18.5 and BMI <-24.9:
    category="Healthy"
elif BMI>-25 and BMI <=29.9:
    category="Overweight"
elif BMI>-30 and BMI <=34:
    category="Obese"
else:
    category="Extreme Obese"
if gender=="Male":
    if age<18:
         message="As a young male, ensure you have a balanced diet and stay active"
    elif age>=18 and age<=40:
        message=" As a adult male, maintaining healthy lifestyle is crucial "
    else:
        message=" As a mature male, regular checkup and balanced diet is essential"
elif gender=="Female":
    if age<18:
         message="As a young male, ensure you have a balanced diet and stay active"
    elif age>=18 and age<=40:
        message=" As a adult male, maintaining healthy lifestyle is crucial "
    else:
        message=" As a mature male, regular checkup and balanced diet is essential"

else:
    message='Please enter a valid gender'


print (f"your BMI is {BMI} and you are {category}")
print (message)
