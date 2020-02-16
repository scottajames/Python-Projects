#Let the user enter a name and get back a name and some information about them

Names = {"bill":"Bill 21 male", "john":"John 22 male", "smith":"Smith 23 male", "jeff":"Jeff 24 male", "james":"James 25 male", "joe":"Joe 26 male"}

choice = input("""
        Press 0 to - Quit
        Press 1 to - Look up
        Press 2 to - Add
        Press 3 to - Delete
        """)

if choice == "0":
        print("Bye")
        input("\nPress any key to exit")
elif choice == "1":
        look = input("Who would you like to lookup?: ")
        if look in Names: {
            print(Names.get(look))
            }
        else:
            print("Can't find what you're looking for")
elif choice == "2":
    add = input("Who would you like to add?: ")
    if add not in Names:
        description = input("How old are they and are they male or female? e.g (21 male)")
        Names[add] = description
        print("It had been added to the database")
    else:
        print("That is already in the database")
elif choice == "3":
    delete = input("Who would you like to delete?: ")
    if delete in Names:
        del Names[delete]
        print("Okay deleted")
    else:
        print("Can't find who you are looking for")
else:
    print("Invalid input")