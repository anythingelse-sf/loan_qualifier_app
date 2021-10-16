
# This is a command line application to match applicants with qualifying loans.
"""Loan Qualifier Application."""

# Import the necessary python libraries
import sys
import fire
import questionary
from pathlib import Path
import csv
import pandas

# Import the util scripts
from qualifier.utils.fileio import load_csv
from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

# Import the financial filter scripts
from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value

# Import user inputs from the questionary financial prompts
from qualifier.utils.financial_prompts import get_applicant_info

# Import the FILEIO scripts
from qualifier.utils.fileio import load_csv    
# from qualifier.utils.fileio import export_csv

## Run the Questionary prompts around the CSV file
def load_bank_data():
    
    csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)

"""
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

# Determine which loans the user qualifies for. Loan qualification criteria is based on:
        # - Credit Score
        # - Loan Size
        # - Debit to Income ratio (calculated)
        # - Loan to Value ratio (calculated)

# Load the latest Bank data from the CSV in the data folder
bank_data = load_bank_data()


 
# The main function for running the script.
def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    
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

# Get the applicant's information
credit_score, debt, income, loan_amount, home_value = get_applicant_info()

# Find qualifying loans
qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )
for loans in qualifying_loans:
    if len(qualifying_loans) ==0:
        print("No loans are available at this time.")
    break

print(f'Here is the list of qualifying loans: {qualifying_loans}') 
        # Ask the user if they would like to to save the data
def export_loan_data():
   
    output_csvwriter = questionary.select("Would you like to save this loan data to a CSV file?", choices=["Yes", "No"],).ask()
    if  output_csvwriter == "Yes":
            filepath= questionary.text("Enter the filepath for where you would you like your loan list saved to:").ask()
            filepath=str(filepath)
            new_csv = "/exported_loan_data.CSV"
            filepath = filepath+new_csv
            with open (Path(filepath), 'w', newline='') as csvfile:
                #Prepare the header for CSV export
                header= ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]
                create_output_csvwriter = csv.writer(csvfile, delimiter=',')
                create_output_csvwriter.writerow(header)
                for lines in range(len(qualifying_loans)):
                    create_output_csvwriter.writerow(qualifying_loans[lines])
            print("Your loan data had been saved to the 'data' folder. Thank you for using Dylan's loan qualifier app!")   
    elif  output_csvwriter == "No": 
                print("You have elected not to save your data. Thank you for using this loan qualifier!")

if __name__ == "__main__":
    fire.Fire(export_loan_data)
