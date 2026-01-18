def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # Check if the year is divisible by 100
        if year % 100 == 0:
            # Check if the year is divisible by 400
            if year % 400 == 0:
                return True  # It's a leap year
            else:
                return False  # It's not a leap year
        else:
            return True  # It's a leap year
    else:
        return False  # It's not a leap year

# Test cases
print(is_leap_year(2400))  # True
print(is_leap_year(1989))  # False
