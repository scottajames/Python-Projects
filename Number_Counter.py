#Write a program that counts for the user
#let the user enter the starting number, ending number and the amount by which to count

print("This program will count for you")
print("Enter the first and second number and which amount to count it by")

number_1 = int(input("First Number "))
number_2 = int(input("Second Number "))
multiply = int(input("Amount by which to count "))

for i in range (number_1, number_2, multiply):
    print(i, end=" ")