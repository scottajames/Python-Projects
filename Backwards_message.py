#program that gets a message from the user then prints it out backwards


print("This program will print what you type in reverse")

message = str(input("Type a message "))[::-1]

print(message.lower())