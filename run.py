""" All imports. """

import os
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    """
    Clear terminal & Print title
    """

    os.system("cls" if os.name == "nt" else "clear")
    print("\033[1;36m")
    print("  WINTER-CAMPAIGN SUMMARY  ".center(90, "-"))
        

title()

# Names & numbers of reports plus global variables
REPORT1 = "Number of participants every day"
REPORT2 = "Time of answering questions during the day"
REPORT3 = "Answer by region to different type of questions"

def welcome():
    """
    Welcome & explanation message
    """

    print("\033[0;37m")
    print(" Welcome to data and insights of our last Christmas campaign!\n\n".center(90,))
    print(" During December, every day we were sending to shops business"
          " or research tasks, e.g:")
    print("\033[0;34m    Business: \033[0;37m 'Show the availability of FROZEN NUGGETS'")
    print("\033[0;34m    Research: \033[0;37m '% of sales increase due to this promo?'\n")
    
    print("\033[0;37m And we were observing their \033[4;37mAnswering"
          " Behavior\033[0;37m ")
    print("\n")
    print("\033[0;36m    Please, select the report for the analysis:\n")

    print(f"\033[0;36m    # 1 :\033[0;37m  {REPORT1}")
    print(f"\033[0;36m    # 2 :\033[0;37m  {REPORT2}")
    print(f"\033[0;36m    # 3 :\033[0;37m  {REPORT3}\n")

    print("\033[0;36m    And any period between 1st and 31st of the month"
          " : \033[0;37m  Dates for analysis\n")
    print("-".center(90, "-"))
    print("\n\n")

welcome()

def collect_input_data():
    """
    Get report & time selection input from the user.
    """
    user_input = SHEET.worksheet('data-input')

    # Input, check the report number and update google sheet
    report_number = int(input("Enter the report number here (1 to 3): "))
    while report_number < 1 or report_number > 3: 
        report_number = int(input(
            "\n\033[1;31mInvalid input, Please type a number between \033[0;37m1 & 3: \n"
        ))

    user_input.update("A2", report_number)
    
    # Input, check the period dates & update the google sheet
    start_date = int(input("\nEnter the NUMBER of start-day (1 to 31): "))
    while start_date < 1 or start_date > 31:
        start_date = int(input(
            "\n\033[1;31mInvalid input, Please type a number between \033[0;37m1 & 31:\n"
        ))

    user_input.update("B2", start_date)

    end_date = int(input(f"\nEnter the NUMBER of end-day ({start_date} to 31): "))
    while (end_date < 1 or end_date > 31) or (start_date > end_date):
        end_date = int(input(
            f"\n\033[1;31mInvalid input, Please type a number between \033[0;37m{start_date} and 31:\n"
        ))

    user_input.update("C2", end_date)

    # Print the user selected options
    if report_number == 1:
        print("\n\n\033[0;37mYou selected:\n")
        print(f"\033[0;36m '{REPORT1}' \033[0;37mfrom {start_date} to {end_date} of December\n")
    elif report_number == 2:
        print("\n\n\033[0;37mYou selected:\n")
        print(f"\033[0;36m '{REPORT2}' \033[0;37mfrom {start_date} to {end_date} of December\n")
    else:
        print("\n\n\033[0;37mYou selected:\n")
        print(f"\033[0;36m '{REPORT3}' \033[0;37mfrom {start_date} to {end_date} of December\n")

collect_input_data()

def make_reports():
    data_sheet = SHEET.worksheet("win-campaign")
    input_sheet = SHEET.worksheet("data-input")
    data = data_sheet.get("A1:E17")

    report_no = int(input_sheet.get("A2")[0][0])
    start_day = int(input_sheet.get("B2")[0][0])
    end_day = int(input_sheet.get("C2")[0][0])

    def create_report1():
        """
        REPORT1 calculation & presentation
        """
        report1 = {}
        for n in range(start_day, end_day+1, 1):
            report1[n] = 0

        for d in range(1, len(data), 1):
            date = data[d][4]
            time = datetime.strptime(date, "%d.%m.%Y %H:%M:%S")
            days = int(time.day)
            if days >= start_day and days <= end_day:
                report1[days] += 1
                            
        for key, value in report1.items():
            print('\033[0;36m       December', key, ':\033[0;37m', value,
                  ' participants')

        report1_values = sorted(report1.items(), key=lambda y: y[1],
                                reverse=True)
        print('\n \033[0;36m Most active days were \033[0;37mDecember',
                report1_values[0][0], 'with', report1_values[0][1],
                '\033[0;36mand \033[0;37mDecember', report1_values[1][0],
                'with', report1_values[1][1], '\033[0;36mparticipants\n\n')
    
    def create_report2():
        """
        REPORT2 calculation & presentation
        """
        report2 = {}
        for n in range(1, 25, 1):
            report2[n] = 0

        for d in range(1, len(data), 1):
            date = data[d][4]
            time = datetime.strptime(date, "%d.%m.%Y %H:%M:%S")
            days = int(time.day)
            hour = int(time.hour)
            if days >= start_day and days <= end_day:
                report2[hour+1] += 1
        print("      \033[4;37mBetween\033[0;37m (hours:)\n")
        for key, value in report2.items():
            print('\033[0;36m            ', key-1, '-', key,
                  ':00 :\033[0;37m', value, ' participants')

        report2_values = sorted(report2.items(), key=lambda y: y[1],
                                reverse=True)
        print('\n\033[0;36m Recommendation: \033[0;37mSend your tasks around\033[4;37m',
            report2_values[0][0]-2, "o'clock\033[0;37m - \033[1;37m2 hours\033[0;37m before the most active time from @\033[0;37m",
            report2_values[0][0]-1, ':00\n\n')

    if report_no == 1:
        create_report1()
    elif report_no ==2:
        create_report2()
    else:
        create_report3()

make_reports()
