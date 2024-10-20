# #WAP to see if a student is applying for driving license is eligible or not
# age = int(input("Enter your age : "))
# if(age>=18):
#     print("can drive & apply for license")
# else:
#     print("sorry you are not eligible for DL")
#     print("Thank you for visiting")


# #WAP for traffic light and actions that can be taken on the basis of traffic color
# Light = input("Enter the light you see on the signal : ")  
# if(Light == "Red"):
#     print("STOP")
# elif(Light == "Orange"):
#     print("LOOK")
# elif(Light == "Green"):
#     print("GO")
# else:
#     print("Light is BROKEN")

# print("END of CODE")

# #WAP to decide grade of students of a class
# Marks = int(input("Enter your marks : "))
# if(Marks >= 90):
#     Grade = "A"
# elif(Marks >= 80 and Marks < 90):
#     Grade = "B"
# elif(Marks >= 70 and Marks < 80):
#     Grade = "C"
# else:
#     Grade = "D"
# print("The Grade of the student is ->", Grade)

#NESTING
Age = int(input("Enter you Age : "))
if(Age >= 18):
    if(Age >= 80):
        print("Cannot Drive")
    else:
        print("Can Drive")
else:
    print("Cannot Drive")    

print("Always Remember to Wear Helmets while Driving")