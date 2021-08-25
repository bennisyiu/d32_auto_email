from datetime import datetime as dt
import random
import smtplib
import pandas as pd
from dotenv import load_dotenv
import os

## notes: task 1
# weekday = now.weekday()

# if weekday == 0:
#   with open("quotes.txt") as quote_file:
#     all_quotes = quote_file.readlines()
#     quote = random.choice(all_quotes)

#     print(quote)

#   with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(MY_EMAIL, MY_PASSWORD)
#     connection.sendmail(
#       from_addr=MY_EMAIL,
#       to_addrs=MY_EMAIL,
#       msg=f"Subject: Monday Motivation \n\n {quote}"
#       )
#     connection.quit()
load_dotenv('.env')
MY_EMAIL = os.getenv('EMAIL')
MY_PASSWORD = os.getenv('PASSWORD')

today = dt.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")
bday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows() }
if today_tuple in bday_dict:
  bday_person = bday_dict[today_tuple]
  file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

  with open(file_path) as letter:
    contents = letter.read()
    contents = contents.replace("[NAME]", bday_person["name"])

  with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=bday_person["email"], msg=f"Subjet: Happy Birthday! \n\n {contents}")
    connection.quit()
