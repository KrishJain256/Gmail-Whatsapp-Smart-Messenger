import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

name = str(os.getenv("MY_NAME"))
my_email = str(os.getenv("MY_EMAIL"))
password = str(os.getenv("MY_GOOGLE_APP_PASSWORD"))

password = password[0:4] + " " + password[4:8] + " " + password[8:12] + " " + password[12:16]

def sendmessage(email, message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(my_email, password)
    msg = f'''
    From: {my_email}
    To: {email}
    Subject: Message from {name}

    {message}
    
    Regards
    {name}
    '''

    s.sendmail(my_email,email, msg)
    s.quit()



# port = 465  # For SSL
#
# def sendmessage(email,message):
#     # Create a secure SSL context
#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#         server.login("krish.jain256@gmail.com","abdk wkmy lbep eeoq")
#         server.sendmail("krish.jain256@gmail.com",email, message)

