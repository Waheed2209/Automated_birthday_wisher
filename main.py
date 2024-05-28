import pandas
import datetime as dt
import smtplib


GMAIL = "mohdwaheed071@gmail.com"
PASSWORD = "gnsz qcsw clim xstl"


with open("letter_templates/letter_1.txt") as file:
    letter = file.read()

today = dt.datetime.now()

birthday_data = pandas.read_csv("birthdays.csv",index_col=False)
dic = birthday_data.to_dict(orient="records")
for num in dic:

    if num["month"] == today.month and num["day"] == today.day:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=GMAIL, password=PASSWORD)
            connection.sendmail(from_addr=GMAIL, to_addrs=num["email"],
                                    msg=f"Subject:Happy Birthday \n\n{letter.replace("[NAME]",num["name"])}")










