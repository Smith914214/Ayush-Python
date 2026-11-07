"""
Monthly Calendar
----------------
A simple Python program to display the calendar
for a specific month and year.
"""

import calendar

year = int(input("Enter year: "))
month = int(input("Enter month(1-12): "))

print(calendar .month(year,month))




"""
Monthly Calendar
----------------
A simple Python program to display the calendar
for a specific month and year.
"""

import calendar


def display_calendar():
    """Ask the user for a year and month, then display the calendar."""

    try:
        year = int(input("Enter year: "))
        month = int(input("Enter month (1-12): "))

        if month < 1 or month > 12:
            print("❌ Invalid month. Please enter a number between 1 and 12.")
            return

        print("\n" + calendar.month(year, month))

    except ValueError:
        print("❌ Please enter valid numbers.")


def main():
    """Run the calendar program."""

    while True:
        display_calendar()

        choice = input("Do you want to view another month? (y/n): ").lower()

        if choice != "y":
            print("Thank you for using Monthly Calendar!")
            break

        print()


if __name__ == "__main__":
    main()
    
    
    
    
    
import calendar


def main():
    while True:
        year = int(input("Enter year: "))
        month = int(input("Enter month (1-12): "))

        print("\n" + calendar.month(year, month))

        choice = input("Do you want to view another month? (y/n): ").lower()

        if choice != "y":
            print("Thank you for using Monthly Calendar!")
            break


if __name__ == "__main__":
    main()