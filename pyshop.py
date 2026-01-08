try:
    birth_year = int(input("Enter your birth year: "))
    age = 2019 - birth_year
    print(f"You are {age} years old.")
except ValueError:
    print("Please enter a valid year.")
