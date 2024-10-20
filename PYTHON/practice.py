# #WAP to check if a number entered by the user is odd or even.
# n = int(input("Enter the Number : "))
# if(n%2 == 0):
#     print("The number is even")
# else:
#     print("The number is odd")

# print("END of Code")

#WAP to find greatest of 3 numbers entered by the user.
a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))
c = int(input("Enter your third number : "))

if(a >= b and a >= c):
    print("First number is largest", a)
elif(b >= c):
    print("Second number is largest", b)
else:
    print("Third number is the largest", c)


#WAP to check if a number is a multiple of 7 or not.