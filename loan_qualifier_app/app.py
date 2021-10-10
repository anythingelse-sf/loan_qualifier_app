# # -*- coding: utf-8 -*-
# """Loan Qualifier Application.

# This is a command line application to match applicants with qualifying loans.

# # Example:
#     $ python app.py
# """
import sys
import fire
import questionary
from pathlib import Path
import csv
import pandas
from questionary.question import Question

from qualifier.utils.fileio import load_csv

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value

#Print the Relative Path

#Print the Absolute Path

def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """

    csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)


def get_applicant_info():
    """Prompt dialog to get the applicant's financial information.

    Returns:
        Returns the applicant's financial information.
    """

    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text("What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

    return credit_score, debt, income, loan_amount, home_value


def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

    """

    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    print(f"Found {len(bank_data_filtered)} qualifying loans")

    return bank_data_filtered




# """The main function for running the script."""

    # Load the latest Bank data
bank_data = load_bank_data()

    # Get the applicant's information
credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

print(qualifying_loans) 
 
 
 #Ask the user if they would like to save the loan list to a CSV file
        ## Use Questionary to ask if you would like to save the file
        ## Offer Yes or NO

header= ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]

def export_loan_data():
    output_csvwriter = questionary.select("Would you like to save this loan data to a CSV file?", choices=["Yes", "No"],).ask()
   

    if  output_csvwriter == "Yes":
        def directory():
            file_path = questionary.text("What directory would you like your loan list saved to?")
            # file_path = Path(file_path)
            with open('data/bank_filtered_data.csv', 'w', newline='') as csvfile:
                create_output_csvwriter = csv.writer(csvfile, delimiter=',')
                create_output_csvwriter.writerow(header)
                for lines in range(len(qualifying_loans)):
                    create_output_csvwriter.writerow(qualifying_loans[lines])
            # if not file_path.exists():
            #     for i =1:3:
            #         try
            #             def directory():
            #             print("This is an incorrect file path")
            #         except
            #                 None
            #         else:
            #             break
            #     else:
            #         print("I'm sorry you have failed three attempts. Try running the program again")

            print("Your loan data had been saved to the 'data' folder. Thank you for using Dylan's loan qualifier app!")        
    elif  output_csvwriter == "No": 
        print("Thank you for using Dylan's loan qualifier! Good luck in your home buying adventure!")
  
    

    
    # Use the csv library and `csv.writer` to write the header row
    # and each row of `loan.values()` from the `inexpensive_loans` list.
            


if __name__ == "__main__":
    fire.Fire(export_loan_data)
