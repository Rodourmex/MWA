from os import environ
import csv
import re

from twilio.rest import Client


# Datos de autentificación
account_sid = environ['TWILIOSID']
auth_token = environ['TWILIOAUTHTOKEN']
wanbr = environ['BOTNBR'] # usar formato: whatsapp:+nmbr 

client = Client(account_sid, auth_token) # cliente para mandar mensaje

file_nm = "pnbrs.csv"

file = open(file_nm, "r", encoding="utf-8", newline="")

contacted_phn = []

text = open("sms.txt", "r", encoding="utf-8")

for row in file:
    phone = row.strip()
    digit = not re.search(r"\D",phone)
    if phone not in contacted_phn:
        contacted_phn.append(phone)
        if len(phone) == 10 and digit: # Checa que el número pueda ser de celular
            message = client.messages \
                        .create(
                            from_=wanbr, #whatsapp:+nmbr 
                            body=text,
                            to=f"whatsapp:+521{phone}"
                        )
        print(phone)