import math
import re

def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_valid_money(value):
    # Regular expression to match money values (positive or negative)
    money_pattern = r'^-?\d+(\.\d{1,2})?$'
    return re.match(money_pattern, value) is not None

def calculate_investment(amount, interest_rate, years, interest_type):
    r = interest_rate / 100
    if interest_type == "simple":
        future_value = amount * (1 + r * years)
    elif interest_type == "compound":
        future_value = amount * math.pow((1 + r), years)
    return future_value

def calculate_bond_repayment(present_value, annual_interest_rate, months):
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    repayment = (monthly_interest_rate * present_value) / (1 - math.pow(1 + monthly_interest_rate, -months))
    return repayment

def main():
    while True:
        print("===========Welcome to THEE BEST Finance Calculator!==========")
        print("Choose either 'investment' or 'bond' from the menu below to proceed:")
        print("1. Investment")
        print("2. Bond")
        print("3. Exit")

        choice = input("Enter your choice: ").strip().lower().replace(" ", "")

        if choice == "investment" or choice == "1":
            while True:
                amount = input("Enter the amount of money you are depositing: R").replace(" ", "")
                if not is_numeric(amount) or not is_valid_money(amount) or float(amount) <= 0:
                    print("Invalid input for amount. Please enter a valid positive numeric value.")
                else:
                    break


            while True:
                interest_rate = input("Enter the interest rate (as a percentage): ")
                if not is_numeric(interest_rate) or float(interest_rate) <= 0 or float(interest_rate) >= 100:
                    print("Invalid input for interest rate. Please enter a valid percentage value.")
                else:
                    break


            while True:
                years = input("Enter the number of years you plan on investing for: ").replace(" ", "")
                if not is_numeric(years) or int(years) <= 0 or int(years) >= 10:
                    print(
                        "Invalid,Please enter a valid value or come to renew your investment after 10yrs.")
                else:
                    break

            while True:
                interest_type = input("Enter 'simple' or 'compound' interest: ").strip().lower()
                if interest_type not in ["simple", "compound"]:
                    print("Invalid interest type. Please enter 'simple' or 'compound'.")
                else:
                    break

            amount = float(amount)
            interest_rate = float(interest_rate)
            years = int(years)

            future_value = calculate_investment(amount, interest_rate, years, interest_type)
            print(f"The future value is: {future_value:.2f}")

        elif choice == "bond" or choice == "2":
            while True:
                present_value = input("Enter the present value of the house: R").replace(" ", "")
                if not is_numeric(present_value) or not is_valid_money(present_value) or float(present_value) <= 0:
                    print("Invalid input for present value. Please enter a valid positive numeric value.")
                else:
                    break

            while True:
                annual_interest_rate = input("Enter the annual interest rate: ").replace(" ", "")
                if not is_numeric(annual_interest_rate) or float(annual_interest_rate) <= 0 or float(
                        annual_interest_rate) >= 100:
                    print("Invalid input for interest rate. Please enter a valid percentage value.")
                else:
                    break

            while True:
                months = input("Enter the number of months for bond repayment: ").replace(" ", "")
                if not is_numeric(months) or int(months) <= 0:
                    print("Invalid input for months. Please enter a valid positive numeric value.")
                else:
                    break

            present_value = float(present_value)
            annual_interest_rate = float(annual_interest_rate)
            months = int(months)

            bond_repayment = calculate_bond_repayment(present_value, annual_interest_rate, months)
            print(f"The monthly bond repayment is: {bond_repayment:.2f}")

        elif choice == "quit" or choice == "3":
            print("Thank you for using our calculator.")
            break

        else:
            print("Invalid choice. Please select 'investment', 'bond', or 'quit'.")

if __name__ == "__main__":
    main()


