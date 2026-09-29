# Project Statement: Day Finder – Weekday Calculator

## 1. Problem Statement

Finding out which day of the week a particular date falls on (for example, a birthday, a deadline, an exam date, or a historical event) is a common need, yet most people rely on a physical calendar or an online tool, and mental calculation is error-prone because of the irregular length of months and the presence of leap years.

This project solves the problem by building a program that takes **any date in any year** (day, month, year) as input and, **without using Python's built-in `datetime` or `calendar` libraries**, computes and displays the correct day of the week. The calculation is done from first principles: the program counts forwards or backwards from a known anchor date (1 January 2026, a Thursday) using month-length tables and leap-year rules, so past and future years are handled in exactly the same way. This demonstrates core programming concepts: lists, functions, loops, conditionals, and modular arithmetic.

## 2. Scope of the Project

### In Scope
- Accepting a date as three integer inputs: day, month, and year.
- Correctly handling leap years using the Gregorian rule (divisible by 4, except century years not divisible by 400).
- Calculating the number of days elapsed from the start of the year to the entered date using separate month-length tables for normal and leap years.
- Calculating the weekday for **any year** (from year 1 onwards, past or future) by counting the weekday shift between the entered year and the 2026 anchor year.
- Validating user input (valid month range, valid day range for the given month/year, year of at least 1, numeric-only input) and displaying clear error messages.
- Displaying the resulting weekday name (Monday to Sunday).
- Modular code organisation (input handling, validation, calculation logic, output display) with unit tests covering leap years, century years, boundary dates, and past/future dates.

### Out of Scope
- Historical calendar systems: the Gregorian rules are applied to every year (the proleptic Gregorian calendar), so the Julian calendar used before 1582 and other calendars (Hijri, Hebrew, etc.) are not modelled.
- Time-of-day, time zones, and daylight-saving handling.
- A graphical or web-based user interface (the project is a command-line application).
- Storing user data or maintaining user accounts.

## 3. Target Users

- **Students** learning programming, who can study how date arithmetic works without relying on library functions.
- **General users** who want to quickly find the weekday of a birthday, anniversary, or upcoming event.
- **Educators** who need a simple, readable example for teaching functions, lists, loops, and modular arithmetic in Python.
- **Beginner developers** who want a clean example of input validation and modular program design.

## 4. High-Level Features

1. **Date Input & Validation Module** – Reads the day, month, and year from the user and rejects invalid entries (e.g., 31 April, 30 February, month 13, non-numeric input) with helpful messages.
2. **Leap Year Detection Module** – Determines whether a given year is a leap year using the full Gregorian rule.
3. **Weekday Calculation Engine** – Computes the weekday by combining:
   - the number of days elapsed within the year (using normal- and leap-year month tables), and
   - the weekday shift between the entered year and the 2026 reference year, accounting for every leap year in between (works for both past and future years).
4. **Result Display Module** – Prints the weekday name in a clear, readable format.
5. **Error Handling** – Graceful handling of invalid or unexpected input so the program never crashes.
6. **Testing** – A suite of unit tests verifying the calculation against known dates (e.g., leap days, century years such as 1900 and 2000, year boundaries, and extreme years such as 1 and 9999).
