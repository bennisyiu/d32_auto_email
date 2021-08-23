# import smtplib

# my_email = "prefacedemo1@gmail.com"
# password = "prefacecode"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#   connection.starttls()
#   connection.login(user=my_email, password=password)
#   connection.sendmail(
#     from_addr=my_email,
#     to_addrs="prefacedemo2@gmail.com",
#     msg="Subject: This is a testing email \n\n This is the body of my email!"
#     )

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_the_week = now.weekday()

# print(day_of_the_week)

import datetime as dt
import random
import smtplib

MY_EMAIL = "prefacedemo1@gmail.com"
MY_PASSWORD = "prefacecode"

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



