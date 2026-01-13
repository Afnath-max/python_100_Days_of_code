print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much would you like to tip? $"))
split = int(input("How many people to split the bill? $"))
payment = (bill + tip ) / split
print(f"Each person should p ay: ${payment:.2f}")