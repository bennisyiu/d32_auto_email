import datetime as dt
import random
import smtplib

MY_EMAIL = EMAIL
MY_PASSWORD = PASSWORD

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
  with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)

    print(quote)

  with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
      from_addr=MY_EMAIL,
      to_addrs=MY_EMAIL,
      msg=f"Subject: Monday Motivation \n\n {quote}"
      )
    connection.quit()

