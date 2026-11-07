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