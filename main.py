import random
import smtplib
import pandas as pd
import datetime as dt

now = dt.datetime.now()
actual_day = (now.month, now.day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if actual_day in birthdays_dict:
    birthday_person = birthdays_dict[actual_day]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])


email = "xxxxxxxxx"
password = "xxxxxxxxx"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(from_addr=email,
                        to_addrs=f"{birthday_person['email']}",
                        msg=f"Subject: Feliz Aniversario!!!\n\n{contents}"
        )



