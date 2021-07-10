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
- Allow the user to create a deposit account with a minimum balance of ¢50
- Allow the user to create a current account with a minimum balance of ¢25
- ? Allow multiple accounts per PPSN?

## Deposit money
The system shall…
- ? Allow the user to deposit money into their account from the minimum of ¢5 to the maximum of ¢2,000 at once?
- ? only allow lodgements in multiples of ¢5?
- ? Allow the customer to lodge money up to ¢5,000, and the limit of the lodgement shall be reset as soon as the customer logs out?
- Print new balance after completing the deposit

## Withdraw money
The system shall…
- ? Allow the customer to withdraw money up to ¢500, and the limit of withdrawal shall be reset as soon as the customer logs out.
- ? Allow the customer to withdraw money from the minimum of ¢5 to the maximum of ¢200 at once.
- ? Only allow withdrawals in multiples of ¢5.
- Allow the customer to select predefined values: 20, 40, 60, and 100 when withdrawing. It shall also allow the customer to enter a custom amount which must be in multiples of ¢5? 
- Print new balance after completing the withdrawal


## Reflect Interest Rate
The system shall... 
- Set the interest rate of the account to 5% if the balance is greater than €10,000
- Set the interest rate of the account to 2% if the balance is less than €10,000
- Set the interest rate of the account to ?% if the overdraft facility is used?


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
- ?Allow a user to transfer funds the minimum of ? to the maximum of ? from one account to another?
	
## Close the program
The system shall…
- Exit and close the program safely
