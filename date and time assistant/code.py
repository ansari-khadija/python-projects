import datetime
import calendar
import time


def show_datetime():
    now = datetime.datetime.now()

    print("\n--- Current Date & Time ---")
    print("Date:", now.strftime("%d-%m-%Y"))
    print("Time:", now.strftime("%I:%M:%S %p"))
    print("Day:", now.strftime("%A"))


def show_calendar():
    try:
        year = int(input("Enter year: "))
        month = int(input("Enter month (1-12): "))

        if month < 1 or month > 12:
            print("Please enter a month between 1 and 12.")
            return

        print("\n", calendar.month(year, month))

    except ValueError:
        print("Please enter valid numbers.")


def calculate_date_difference():
    try:
        date1 = input("Enter first date (DD-MM-YYYY): ")
        date2 = input("Enter second date (DD-MM-YYYY): ")

        first = datetime.datetime.strptime(
            date1, "%d-%m-%Y"
        ).date()

        second = datetime.datetime.strptime(
            date2, "%d-%m-%Y"
        ).date()

        difference = abs((second - first).days)

        print("Difference:", difference, "days")

    except ValueError:
        print("Invalid date! Please use DD-MM-YYYY.")


def show_countdown():
    try:
        seconds = int(input("Enter countdown seconds: "))

        if seconds < 0:
            print("Seconds cannot be negative.")
            return

        print("\nCountdown started!")

        for remaining in range(seconds, 0, -1):
            print(f"\rTime remaining: {remaining} seconds ", end="", flush=True)
            time.sleep(1)

        print("\rTime is up!                 ")

    except ValueError:
        print("Please enter a valid whole number.")


def main():
    while True:
        print("\n" + "=" * 35)
        print("      DATE & TIME ASSISTANT")
        print("=" * 35)
        print("1. Current Date & Time")
        print("2. Show Calendar")
        print("3. Calculate Date Difference")
        print("4. Countdown Timer")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_datetime()
        elif choice == "2":
            show_calendar()
        elif choice == "3":
            calculate_date_difference()
        elif choice == "4":
            show_countdown()
        elif choice == "5":
            print("Thank you for using Date & Time Assistant!")
            break
        else:
            print("Invalid choice! Please select 1-5.")


if __name__ == "__main__":
    main()