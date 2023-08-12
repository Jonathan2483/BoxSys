# === Imports ===
import os
from colorama import Fore
import time
import random
time.sleep(0.5)
# === Variables ===
ver = "Dev"
startdir = os.getcwd()
warn = f"{Fore.LIGHTYELLOW_EX}[WARN]{Fore.RESET}"
okay = f"{Fore.LIGHTGREEN_EX}[OKAY]{Fore.RESET}"
erro = f"{Fore.LIGHTRED_EX}[ERRO]{Fore.RESET}"
user = f"{Fore.LIGHTMAGENTA_EX}USER -> {Fore.RESET}"

# === Functions ===
def back(type):
    os.chdir(startdir)
    if type != "1":
        log(f"Directory changed to {startdir}")
def log(log):
    back("1")
    os.chdir("logs")
    ctime = time.strftime("%H:%M:%S")
    f = open(f"{clientid}.log", "w")
    f.write(f"[{ctime}] [{clientid}] {log}")
    f.close()
    back("1")
def secure():
    password = None
    cpassword = None

# === Client Startup ==
clientid = random.randint(1000, 9999)
log("Client Started.")

def login():
    None

def signup():
    None

os.system("cd..")
os.chdir("Users")
users = os.listdir()

while True:
    print("1. Login\n2. Signup")
    ls = input(user)