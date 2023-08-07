import math

print("Choose either 'investment' or 'bond' from the menu below to proceed:")
print("investment - to calculate the amount of interest you'll earn on an investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

# Input for the type of calculation
choice = input("Enter your choice: ")

# Case 1: Investment
if choice.lower() == 'investment':
    # Input for investment values
    principal_amount = float(input("Enter the principal amount: "))
    interest_rate = float(input("Enter the rate of interest: "))
    years = int(input("Enter the number of years: "))
    interest_type = input("Enter the type of interest (compound/simple): ")

    # Calculate the investment amount based on the interest type
    if interest_type.lower() == "simple":
        investment_amount = principal_amount * (1 + interest_rate * years)
    elif interest_type.lower() == "compound":
        investment_amount = principal_amount * math.pow((1 + interest_rate), years)
    else:
        print("Invalid type of interest selected!!!")
        investment_amount = None

    if investment_amount is not None:
        print("The amount after", years, "years is", round(investment_amount, 2))

# Case 2: Bond
elif choice.lower() == 'bond':
    
    # Input for bond values
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the rate of interest: "))
    months = int(input("Enter the number of months for the bond: "))

    monthly_interest = interest_rate / 12
    bond_repayment = (monthly_interest * present_value) / (1 - (1 + monthly_interest) ** (-months))

    print("The repayment after", months, "months is", round(bond_repayment, 2))

# Invalid case
else:
    
    print("Invalid choice!!")