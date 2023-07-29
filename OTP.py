#Task-2 OTP Verification

import random
import smtplib

#Generating a random 6 digit number as OTP

OTP=random.randint(100000,999999)

#setting up server

server=smtplib.SMTP("smtp.gmail.com",587) #server code of gmail is 587
server.starttls() #for security

name=input("Enter your name:")
global receiver_email
receiver_email=input("Enter your Email ID:")

def email_verification(receiver_email):
    email_check1=["gmail","hotmail","yahoo","outlook"]
    email_check2=[".com",".in",".org",".edu",".co.in"]

    count=0
    
    for domain in email_check1:
        if domain in receiver_email:
            count+=1
    for site in email_check2:
        if site in receiver_email:
            count+=1
    
    if "@" not in receiver_email or count!=2:
        print("Invalid Email ID!")
        new_receiver_email=input("Enter correct Email ID:")
        email_verification(new_receiver_email)
        return new_receiver_email
    return receiver_email

valid_receiver_email=email_verification(receiver_email) #checking if the email is valid or not

password= "diyveevdnbxjvwhj" #password to get into the sender's gmail account
server.login("shwetapal0768@gmail.com",password) #logging into the sender's gmail account

body="Dear "+name+","+"\n"+"\n"+"Your One Time Password (OTP) is "+str(OTP)+"." #generating a message
subject="One Time Password (OTP) for verification"
message=f'Subject:{subject}\n\n{body}'

server.sendmail("shwetapal0768@gmail.com",valid_receiver_email,message)

def sending_otp(receiver_email):
    New_OTP=random.randint(100000,999999)

    body="Dear "+name+","+"\n"+"\n"+"Your One Time Password (OTP) is "+str(New_OTP)+"." #generating a message with new OTP
    subject="One Time Password (OTP) for verification"
    message=f'Subject:{subject}\n\n{body}'

    server.sendmail("shwetapal0768@gmail.com",receiver_email,message)
    print("OTP has been sent to "+receiver_email)
    received_OTP=int(input("Enter OTP:"))

    if received_OTP==New_OTP: #verifying the entered OTP
        print("OTP Verified!")
    else:
        print("Invalid OTP!")
        print("Resending OTP...")
        sending_otp(receiver_email)

print("OTP has been sent to "+valid_receiver_email)
received_OTP=int(input("Enter OTP:"))

if received_OTP==OTP: #verifying the entered OTP
    print("OTP Verified!")
else:
    print("Invalid OTP!")
    answer=input("Enter Yes to resend OTP to the same Email ID and No to enter a new Email ID:")
    YES=["YES","yes","Yes"]
    NO=["NO","no","No"]
    if answer in YES:
        sending_otp(valid_receiver_email)
    elif answer in NO:
        new_receiver_email=input("Enter new Email ID:")
        email_verification(new_receiver_email)
        sending_otp(new_receiver_email)
    else:
        print("Invalid Input!")

server.quit()