#a character creator program the player should be given a pool of 30 points to spend on four attributes
#Strangth, health, wisdom, dexterity
#the player should be able to take points from an attribute and put them back into the pool

attributes = ("Health", "Strength", "Wisdom", "Dexterity")
Health = 0
Strength = 0
Wisdom = 0
Dexterity = 0
Points = 30

print("-|---- Welcome! ----|- \n")
print("You have 30 points to spend in your attributes:", attributes, "\n")

while Points > 0:
    print("Points", Points)
    print("Health", Health)
    print("Strength", Strength)
    print("Wisdom", Wisdom)
    print("Dexterity",Dexterity)
    print("You have", Points, "left what skill would you like to increase?")
    print("If you want to take a point from an attribute just type - and the attribute you want to take a point from: e.g - health")
    skill = input("What attribute would you like to increase? ").lower()
    if Points == 0:
        print("Your attributes are")
        print("Health", Health)
        print("Strength", Strength)
        print("Wisdom", Wisdom)
        print("Dexterity",Dexterity)
    elif skill == "health":
        Health+=1
        Points-=1
    elif skill == "strength":
        Strength+=1
        Points-=1
    elif skill == "wisdom":
        Wisdom+=1
        Points-=1
    elif skill == "dexterity":
        Dexterity+=1
        Points-=1
    elif skill == "- health":
        Health-=1
        Points+=1
    elif skill == "- strength":
        Strength-=1
        Points+=1
    elif skill == "- wisdom":
        Wisdom-=1
        Points+=1
    elif skill == "- dexterity":
        Dexterity-=1
        Points+=1