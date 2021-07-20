# Banking-Account-Management-System
A console-based Banking Account Management application using the OOP paradigm.

# Functional Objectives

## Create a new account
The system shall…
- Allow the user to create a new customer account including:
    - first name
    - last name
    - PPSN
    - account number (generated)
    - account type (deposit/current)
    - overdraft (Y/N)
- Allow the user to create a deposit account with a balance of ¢50.
- Allow the user to create a current account with a balance of ¢25.
- Allow multiple accounts per PPSN.


## Lodge money
The system shall…
- Allow the user to lodge money into the selected account from the minimum of ¢5 to the maximum of ¢20,000 at once.
- Allow the user to deposit irregular amounts, including cents.
- Print new balance after completing the lodgement

There’s no limit to the number of deposits to an account in a day/session.


## Withdraw money
The system shall…
- Allow the user to withdraw money from the minimum of ¢5 to the maximum of ¢20,000 at once from Current account.
- Allow the user to withdraw irregular amounts, including cents.
- Print new balance after completing the withdrawal.
- Not allow withdrawing from a deposit account.

There’s no limit to the number of withdrawals to an account in a day/session.


## Reflect Interest Rate
The system shall... 
- Set the interest rate of the account to 5% if the balance is greater than €10,000
- Set the interest rate of the account to 2% if the balance is less than €10,000
- Keep the interest rate of the account to 2% even when the overdraft facility is being used.


## View accounts
The system shall…
- Allow a user to display a list of all accounts that have been created, include:
    - first name
    - last name
    - account number
    - balance
    - interest rate
- Allow a user to view account information for a specific PPSN, include:
    - first name
    - last name
    - PPSN
    - Account number
    - Account type
    - Overdraft (Y/N)
    - Interest rate

## Transfer funds
The system shall…
- Allow a user to transfer funds the minimum of  ¢5  to the maximum of ¢250,000 from one account to another.
- Allow the user to transfer irregular amounts, including cents.

	
## Close the program
The system shall…
- Exit and close the program safely
- Save customer data and account data in csv files.

