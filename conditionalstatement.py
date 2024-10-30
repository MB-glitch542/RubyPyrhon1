# python script that checks a number is even or odd number

num=int(input("Enter a number: "))
if num%2==0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")

# create a program that prints the largest of three numbers
num2=int(input("Enter the first number: "))
num3=int(input("Enter the second number: "))
num4=int(input("Enter the third number: "))
if num2>num3 or num2>num4:
    print(f"{num2} is the greatest number")
elif num3>num4 or num3>num2:
    print(f"{num3} is the greatest number")
elif num4>num3 or num4>num2:
    print(f"{num4} is the greatest number")
elif num2==num3 and num4==num2:
    print("they are all equal")
else:
    print("they are not equal")
