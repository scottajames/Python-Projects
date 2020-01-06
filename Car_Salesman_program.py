#Write a car salesman program where the user enters the base price of a car.
#the program should add on a bunch of extra fees such as tax, license,
#dealer prep, and destination charge. make tax and license a percent of
#the base price. the other fees should be set values display the actual
#price of the car once all the extras are applied

car = int(input("Car Price \n £"))
tax = car*10//100
license = car*5//100
prep = 100
destination = 100
print ("Tax £", tax)
print("License £", license)
print("Dealer prep £", prep)
print("Destination charge £", destination)
print("Total Cost £", car + tax + license + prep + destination)
