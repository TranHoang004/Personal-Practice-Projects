
name = []  # List to store input name
age = []  # List to store input age

def input_name():
    user_input = input("Enter your name: ")
    names = user_input.split()  
    name.extend(names)  

def input_age():
    while True:
        user_input = input("Enter your age: ")
        ages = user_input.split()
        try:
            ages_int = [int(a) for a in ages]
            age.extend(ages_int)
            break  
        except ValueError:
            print("Please enter valid ages (numbers only). Try again.")
    
def print_user_info():
    if name:
        print("You entered names:", name)
    else:
        print("No names entered yet.")
    if age:
        print("You entered ages:", age)
    else:
        print("No ages entered yet.")

# Call the function
def menu():

    while True:
        print("1. Input Name")
        print("2. Input Age")
        print("3. Print User Info")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            input_name()
        elif choice == '2':
            input_age()
        elif choice == '3':
            print_user_info()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

menu()  # Start the menu loop