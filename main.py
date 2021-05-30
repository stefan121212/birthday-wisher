import pandas
import datetime as dt
import random
import smtplib


EMAIL = "Your.Email@gmail.com"
PASSWORD = "Your_password"
now = dt.datetime.now()
today_tuple = (now.month, now.day)
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    name1 = birthday_dict[today_tuple]["name"]
    sending_email = birthday_dict[today_tuple].email
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r") as birthday_card:
        birthday_doc = birthday_card.read()
        finished_msg = birthday_doc.replace("[NAME]", name1)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=sending_email,
                            msg=f"Subject:Happy Birthday\n\n{finished_msg}"
        )


