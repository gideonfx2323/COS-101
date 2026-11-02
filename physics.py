def force():
    mass = float(input("Enter mass: "))
    acceleration = float(input("Enter acceleration: "))

    f = mass * acceleration
    print("The force is", f, "N")



def heat_capacity():
    mass = float(input("Enter the mass: "))
    specific_heat_capacity = float(input("Enter the specific heat capacity of the metal: "))
    Titer_2 = float(input("Enter final temperature: "))
    Titer_1 = float(input("Enter the initial temperature: "))

    hc = mass * specific_heat_capacity * (Titer_2-Titer_1)
    print("The Heat Capacity is", hc, "KgK")

def impulse():
    force = float(input("Enter force: "))
    time = float(input("Enter time "))

    imp = force * time 
    print("The Impulse is", imp)

def speed():
    distance = float(input("Enter distance: "))
    time = float(input("Enter time: "))

    if time == 0:
        print("Time cannot be 0")
    
    s = distance/time
    print("The speed is", s, "m/s")
  
def momentum ():
    mass=float(input('Enter the mass:'))
    velocity = float(input('Enter the velocity'))
    mom = mass * velocity 
    print('The momentum is:',mom)

while True:

    print("Hey! What do you want to calculate?")
    print("1. Force")
    print("2. Speed")
    print("3. Heat Capacity")
    print("4. Impulse")
    print("5. Momentum")
    print("6. Exit")

    option = input("Select a formula (1-5) or 6 to exit.")

    if option == "1":
        force()

    elif option == "2":
        speed()

    elif option == "3":
        heat_capacity()

    elif option == "4":
        impulse()

    elif option == "5":
        momentum()

    elif option == "6":
        print("See you later!")
        break

    else:
        print("Invalid number request, pick a number from 1 to 6")
