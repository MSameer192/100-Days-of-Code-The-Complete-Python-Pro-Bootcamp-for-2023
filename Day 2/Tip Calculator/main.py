# Welcome message
print("Welcome to the tip calculator!")

# Input for the total bill amount
bill_amount = float(input("Enter the total bill amount: $"))

# Input for choosing the tip percentage
chosen_tip_percentage = int(input("Select the desired tip percentage (10%, 12%, or 15%): "))

# Input for the number of people sharing the bill
num_people = int(input("Enter the number of people sharing the bill: "))

# Calculate the tip amount based on the chosen percentage
tip_percentage = chosen_tip_percentage / 100
total_tip = bill_amount * tip_percentage

# Calculate the total bill amount including the tip
total_amount = bill_amount + total_tip

# Calculate the amount each person should contribute
amount_per_person = total_amount / num_people

# Round the amount to two decimal places for clarity
rounded_amount_per_person = round(amount_per_person, 2)

# Display the amount each person should contribute
print(f"Each person should contribute: ${rounded_amount_per_person}")
