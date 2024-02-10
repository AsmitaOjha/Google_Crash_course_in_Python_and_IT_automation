def get_valid_name():
    name = ""
    while len(name) < 3:
        name = input("Enter your name: ")
        if len(name) < 3:
            print("Invalid! The name should be at least 3 characters long.")
    print("Valid name! Your name is:", name)

# Call the function to get a valid name
get_valid_name()
