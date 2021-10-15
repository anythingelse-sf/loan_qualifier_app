 """Loan Qualifier Application."""
# This is a command line application to match applicants with qualifying loans.

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

#Import the financial filter scripts
from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value

## Import Questionary prompts around the CSV file



"""The main function for running the script."""

    # Load the latest Bank data
bank_data = load_bank_data()

    # Get the applicant's information
credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

print(qualifying_loans) 
 

if __name__ == "__main__":
    fire.Fire(export_loan_data)
