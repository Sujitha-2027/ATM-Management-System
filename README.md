# ATM Management System using Python, MySQL and Twilio

## Project Overview

This is a simple ATM Management System developed using Python, MySQL, and Twilio. The project simulates basic ATM operations such as balance enquiry, credit, debit, PIN verification, OTP authentication, transaction history, and SMS notifications.

## Features

* Account Number Verification
* Password Strength Validation
* OTP Authentication using Twilio
* PIN Verification
* Balance Enquiry
* Credit Amount
* Debit Amount
* Transaction History
* SMS Alerts for Transactions
* Voice-Based Exit Message using pyttsx3
* MySQL Database Integration

## Technologies Used

* Python
* MySQL
* Twilio API
* pyttsx3

## Required Modules

Install the required modules using:

pip install mysql-connector-python twilio pyttsx3

## Database Setup

Create a database named:

atm_project

Create a table named:

users

Columns:

* account_no
* balance

## How to Run

1. Configure MySQL database connection.
2. Update Twilio SID, Auth Token, and phone numbers.
3. Run the Python script.
4. Enter account number and password.
5. Verify OTP.
6. Enter PIN.
7. Perform ATM transactions.

## Project Workflow

1. User enters account number.
2. Password strength is validated.
3. OTP is sent to the registered mobile number.
4. User verifies OTP.
5. PIN authentication is performed.
6. User can:

   * Check Balance
   * Credit Amount
   * Debit Amount
   * View Transaction History
7. SMS notifications are sent after transactions.
8. Voice message is played when exiting the application.

## Note

This project is developed for educational and learning purposes. Sensitive credentials such as database passwords, Twilio SID, and Auth Tokens should not be uploaded to public repositories.

## Author

Sujitha A

