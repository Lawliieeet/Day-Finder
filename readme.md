# Day Finder Using Mathematical Logic

## About the Project

This project is a Python program that determines the day corresponding
to a given date, month, and year.

The program was developed using mathematical reasoning and modular
arithmetic rather than relying on built-in date or calendar functions.
The calculation is based on the number of days in years and months and
the way those days shift the day of the week.

The program can calculate the corresponding day for any year, including
leap years.

## How It Works

The main idea behind the calculation is based on the fact that a week
contains 7 days.

-   A normal year contains 365 days.
-   365 % 7 = 1, so a normal year shifts the day by 1.
-   A leap year contains 366 days.
-   366 % 7 = 2, so a leap year shifts the day by 2.
-   The program calculates the accumulated shift between the given year
    and a reference year.
-   It then calculates the number of days that have passed within the
    given year.
-   Modular arithmetic is used to obtain the final day.

Leap years are identified using the conditions for divisibility by 4,
100, and 400.

## Requirements

-   Python 3
-   No external libraries are required.

## How to Run

### 1. Run the program

```bash
python main.py
```
### 2. Enter the date

```text
The program will ask for the date, month, and year.
```
Enter each value when prompted.

## Example

```text
Input

Enter the date: 29
Enter the month: 9
Enter the year: 2026

Output

Tuesday
```
## Features

-   Determines the day for a given date, month, and year.
-   Handles leap years.
-   Calculates dates both before and after the reference year.
-   Uses mathematical logic and modular arithmetic.
-   Runs directly through the command line.
-   Requires no external Python libraries.


