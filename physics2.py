
# PHYSICS FORMULA CALCULATOR

# 1. Speed = Distance / Time
def calculate_speed():
    distance = float(input("Enter distance (metres): "))
    time = float(input("Enter time (seconds): "))

    if time == 0:
        print("Time cannot be zero.")
    else:
        speed = distance / time
        print("Speed =", speed, "m/s")


# 2. Force = Mass × Acceleration
def calculate_force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s²): "))

    force = mass * acceleration
    print("Force =", force, "N")


# 3. Density = Mass / Volume
def calculate_density():
    mass = float(input("Enter mass (kg): "))
    volume = float(input("Enter volume (m³): "))

    if volume == 0:
        print("Volume cannot be zero.")
    else:
        density = mass / volume
        print("Density =", density, "kg/m³")


# 4. Work Done = Force × Distance
def calculate_work():
    force = float(input("Enter force (N): "))
    distance = float(input("Enter distance (metres): "))

    work = force * distance
    print("Work Done =", work, "J")


# 5. Power = Work Done / Time
def calculate_power():
    work = float(input("Enter work done (J): "))
    time = float(input("Enter time (seconds): "))

    if time == 0:
        print("Time cannot be zero.")
    else:
        power = work / time
        print("Power =", power, "W")


# MAIN PROGRAM
while True:

    print("\n===== PHYSICS FORMULA CALCULATOR =====")
    print("1. Calculate Speed")
    print("2. Calculate Force")
    print("3. Calculate Density")
    print("4. Calculate Work Done")
    print("5. Calculate Power")

    choice = input("\nChoose a formula (1-5): ")

    if choice == "1":
        calculate_speed()

    elif choice == "2":
        calculate_force()

    elif choice == "3":
        calculate_density()

    elif choice == "4":
        calculate_work()

    elif choice == "5":
        calculate_power()

    else:
        print("\nOption does not exist!")

    # Ask whether the user wants another calculation
    while True:
        again = input(
            "\nDo you still want to calculate? (yes/no): "
        ).lower().strip()

        if again == "yes":
            break

        elif again == "no":
            print("\nThank you for using the Physics Calculator!")
            exit()

        else:
            print("Please enter yes or no.")
