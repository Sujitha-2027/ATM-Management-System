#twilio
from twilio.rest import Client
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_database_password",
    database="atm_project"
)
mycursor = mydb.cursor()
SID='your_twilio_sid'
token='your_twilio_token'
ct=Client(SID,token)
def send_sms (msg):
    ct.messages.create(body=msg,from_='your_twilio_number', to='user_phone_number')
history = []
acc = int(input("Enter account number: "))
#password check
password = input("Enter your password:")
if len(password) >= 8:
    if any(c.isupper() for c in password):
        if any(c.isdigit() for c in password):
            if any(not c.isalnum() for c in password):
                    print("Strong password")
            else:
                print("Password must contain at least Special char")
        else:
            print("Password must contain at least one digit")
    else:
        print("Password must contain at least one uppercase letter")
else:
    print("Password too short. Minimum 8 characters required")
    exit()
import random
otp=random.randint(1000,5000)
send_sms(f"your otp is {otp}")
user_otp=int(input("Enter your otp:"))
if user_otp == otp:
    print("Your otp is correct")
else:
    print("Your otp is incorrect")
mycursor.execute("SELECT balance FROM users WHERE account_no=%s",(acc,))
data = mycursor.fetchone()
balance = data[0]
#pin check
attempt=0
while attempt < 5:
    pin=int(input("enter your pin:"))
    if pin==2027:
        print("access granted")
        break
    else:
        print("wrong pin")
        attempt=attempt+1
if attempt==5:
    print("card blocked")
    exit()
while True:
    print("1.balance")
    print("2.credit")
    print("3.debit")
    choice=int(input("enter your choice:"))
    if choice==1:
        print("balance:",balance)
        send_sms(f"Your balance is {balance}")
    if choice==2:
        credit=int(input("enter your credit:"))
        balance+=credit
        mycursor.execute(
            "UPDATE users SET balance=%s WHERE account_no=%s",
            (balance, acc)
        )
        mydb.commit()
        print("updated balance:",balance)
        history.append(f"credit {balance}")
        send_sms(f"Credited {credit} Rs.Balance  {balance}")
    elif choice==3:
        debit=int(input("enter your debit:"))
        if(2000<debit):
            print("2000 above not debit")
        if(debit>balance):
            print("insufficient balance")
        if(debit<=0):
            print("invalid amount")
        else:
            balance -= debit
            mycursor.execute(
                "UPDATE users SET balance=%s WHERE account_no=%s",
                (balance, acc)
            )
            mydb.commit()
            print("remaining balance:",balance)
            print("amount debited successfully")
            send_sms(f"Debited {debit} Rs.Balance  {balance} ")
            history.append(f"debit {balance}")
    elif(choice==4):
        for i in history:
            print(i)
        send_sms(f"last transaction is {history[-1]}")
    if(choice==5):
        import pyttsx3
        #voice
        text_speech = pyttsx3.init()
        text_speech.say("Thank you! visit again")
        text_speech.runAndWait()
        print("Thank you! visit again")
        break
else:
    print("invalid choice")
