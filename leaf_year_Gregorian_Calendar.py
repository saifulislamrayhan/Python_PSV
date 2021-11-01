def is_leap(year):
    leap = False
    if (year >= 1900) & (year <= 100000):
        if (year % 100 == 0) | (year % 100 != 0):
            if (year % 4 == 0) & (year % 100 != 0):
                leap=True
                return leap
            elif (year % 4 == 0) & (year % 400 == 0):
                leap=True
                return leap
            if (year % 4 == 0) & (year % 100 == 0):
                leap=False
                return leap
            elif (year % 400 == 0) & (year % 100 == 0):
                leap=False
                return leap
            elif (year % 4 == 0) & (year % 400 == 0) & (year % 100 == 0):
                leap=True
                return leap

            else:
                leap=False
                return leap
        else:
            leap=False
            return leap
    else:
        leap=False
        return leap


year = int(input("Please Enter the Year: "))
final=is_leap(year)
print(final)