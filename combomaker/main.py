import random
import string
from colorama import init
from vardxg import Colors, Write, Center
import os

init(autoreset=True)
os.system('cls')

done = 0

logo = ("""
Random Account Gen

""")
Write.Print(Center.XCenter(logo), Colors.purple_to_blue, interval=0)

value = int(Write.Input("\n [>] Enter How Much u want >>> ", Colors.purple_to_blue, interval=0))
os.system('cls')

def generate_random_email(length=10, domain_options=None):
    if domain_options is None:
        domain_options = ['gmail.com', 'yahoo.com', 'gmx.com', 'hotmail.com']
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    domain = random.choice(domain_options)
    email = f"{username}@{domain}"
    return email

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

num_pairs = value  # Number of email-password pairs to generate

while True:
    try:
        with open('emails.txt', 'w') as f:
            for _ in range(num_pairs):
                random_password = generate_random_password()
                random_email = generate_random_email()
                email_line = "Email >>> {} | Password >>> {}\n".format(random_email, random_password)
                f.write(email_line)
                done += 1
                Write.Print("\n Generate >>> {} | Done >>> {}".format(random_email, done), Colors.purple_to_blue, interval=0)
    except:
        continue

# Made by @vardxg on Telegram!