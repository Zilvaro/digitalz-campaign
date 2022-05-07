""" All imports. """

import os
import gspread
from google.oauth2.service_account import Credentials
import datetime

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
    print("\033[1;36m")
    print("  WINTER-CAMPAIGN SUMMARY  ".center(90, "-"))
        

title()


# Names & numbers of reports plus global variables
report1 = "Number of participants every day by region"
report2 = "Time of answering questions during the day"
report3 = "Answer by region to different type of questions"


def welcome():
    # Welcome & explanation message

    print("\033[0;37m")
    print(" Welcome to data and insights of our last Christmas campaign!\n\n".center(90,))
    print(" During December, every day we were sending to shops business"
        " or research tasks, e.g:")
    print(f"\033[0;34m    Business: \033[0;37m 'Show the availability of FROZEN NUGGETS'")
    print(f"\033[0;34m    Research: \033[0;37m '% of sales increase due to this promo?'")
    print("\n")
    print("\033[0;37m  And we were observing their answering Behavior ")
    print("\033[0;36m  Please, select the report and dates for the analysis:\n")

    print("\033[0;36m    # 1 :\033[0;37m  {report1}")
    print("\033[0;36m    # 2 :\033[0;37m  Time of answering questions during the day")
    print("\033[0;36m    # 3 :\033[0;37m  Answer by region to different type of questions\n")

    print("\033[0;36m    Any period between 1st and 31st of the month : \033[0;37m  Dates for analysis\n")
    print("-".center(90, "-"))
    print("\n\n")
     

welcome()


def get_input_data():
    """
    Get report & time selection input from the user.
    """
    user_input = SHEET.worksheet('data-input')

    # Input & check the report number
    report_number = int(input("Enter the report number here (1 to 3): "))
    while report_number < 1 or report_number > 3: 
        report_number = int(input(
            "\n\033[1;31mInvalid input, Please type a number between \033[0;37m1 & 3: \n"
        ))
    report_value = user_input.update ("A2", report_number)
    
    # Input & check the period dates
    start_date = int(input("\nEnter the NUMBER of start-day (1 to 31): "))
    while start_date < 1 or start_date > 31:
        start_date = int(input(
            "\n\033[1;31mInvalid input, Please type a number between \033[0;37m1 & 31:\n"
        ))

    start_value = user_input.update ("B2", start_date)

    end_date = int(input("\nEnter the NUMBER of end-day (1 to 31): "))
    while (end_date <1 or end_date >31) or (start_date > end_date):
        end_date = int(input(
            f"\n\033[1;31mInvalid input, Please type a number between \033[0;37m{start_date} and 31:\n"
        ))

    end_value = user_input.update ("C2", end_date)

    # Print the user selected options 
    if report_number == 1:
        print("\n\n\033[0;37mYou selected:\n")
        print(f"\n\033[1;36m '{report1}' \033[1;37mfrom {start_date} to {end_date} of December")
    elif report_number == 2:
        print("\n\n\033[0;37mYou selected:\n")
        print(f"\n\033[1;36m '{report2}' \033[1;37mfrom {start_date} to {end_date} of December")
    else:
        print("\n\n\033[0;37mYou selected:\n")
        print(f"\n\033[1;36m '{report3}' \033[1;37mfrom {start_date} to {end_date} of December")


get_input_data()

"""
def run_file:

report_value = user_input.cell(2,1)
    start_value = user_input.cell(2,2)
    end_value = user_input.cell(2,3)
    
"""