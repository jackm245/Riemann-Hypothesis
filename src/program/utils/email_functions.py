from dotenv import load_dotenv, find_dotenv
import smtplib
import os


def send_verification_email(to_addr, code):
    load_dotenv(find_dotenv())
    from_addr = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    print(from_addr, password)
    message = "Dear Sir / Ma'am\nThank you for using the Riemann " \
            f"Hypothesis Program\nYour verification code is: {code}"
    send_email(from_addr, to_addr, 'Verification', message, password)


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


send_verification_email('jack.morgan2@challoners.org',' 123456')
