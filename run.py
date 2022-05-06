""" All imports. """

import os
import gspread
from google.oauth2.service_account import Credentials
import  datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('datasheet-python-campaign')


def title():
    # Clear terminal & Print title
    
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[1;35m")
    print("  WINTER-CAMPAIGN SUMMARY  ".center(90, "-"))
    print("\n")


title()


def welcome():
    # Welcome & explanation message

    print("\033[0;37m")
    print(" Welcome to data and insights of our last Christmas campaign!\n")
    print(" During December, every day we were sending to shops business or research tasks, e.g:")
    print(f'\033[0;34m    Business: \033[0;37m "Show the availability of FROZEN NUGGETS" ')
    print(f'\033[0;34m    Research: \033[0;37m "% of sales increase due to this promo?"')
    print("\n")
	
welcome()    
