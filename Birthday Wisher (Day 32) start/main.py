# import smtplib
#
# my_email = "sharmakrishnaroyalacademy@gmail.com"
# password = "xepzaxywpigeehqy"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="krishna.sharma21b@iiitg.ac.in", msg="Subject:Yo\n\nKaam Kar Launde")
# import datetime as dt
# now = dt.datetime.now()
#

import datetime as dt
import smtplib
import random

now = dt.datetime.now()
if now.weekday() == 2:

    with open("quotes.txt") as file:
        data = file.readlines()
        my_email = "sharmakrishnaroyalacademy@gmail.com"
        password = "xepzaxywpigeehqy"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        quote = random.choice(data)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: Tuesday Motivation\n\n{quote}")

#
#
#
#
