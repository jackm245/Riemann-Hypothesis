from dotenv import load_dotenv, find_dotenv
import smtplib
import os
from .user import User


def send_verification_email(code):
    load_dotenv(find_dotenv())
    from_addr = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    message = f"Dear {User.GetUsername()}\nThank you for using the Riemann " \
            f"Hypothesis Program\nYour verification code is: {code}\n" \
            "If this was not you, please make sure that your account is secured"
    send_email(from_addr, User.GetEmail(), 'Verification', message, password)


def send_email(from_addr, to_addr, subject, message, password,
              smtpserver='smtp.gmail.com:587'):
    header = f'Subject: {subject}\n'
    header += f'To: {to_addr}\n'
    message = header + message
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(from_addr,password)
    problems = server.sendmail(from_addr, to_addr, message)
    server.quit()
