# Credit Score Checker

print("\n --- Credit Score Checker ---")

# State input

income = float(input("Enter your income here in USD: "))
loan_amount = float(input("Enter your loan amount here in USD: "))
repayment_history = input("Has the applicant defaulted before?(yes/no): ").lower()

# Step 1: Business rule logic
# Rule 1: Income ratio

income_ratio = income/loan_amount

# Rule 2: Repayment history

has_defaulted = repayment_history == "yes"

# Decision tree logic

if has_defaulted and income_ratio < 1:
    print("High Risk: Low income and has defaulted in the past")
elif has_defaulted and income >= 1:
    print("Under Review: Income is okay but has defaulted in the past")
elif not has_defaulted and income >= 2:
    print("Approved: High income and good repayment history")
else:
    print("Under Review: Needs manual evaluation")
