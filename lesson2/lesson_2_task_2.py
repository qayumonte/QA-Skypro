def is_year_leap(year: int):
    if year % 4 == 0:
        print('год', str(year) + ':', True)
    else:
        print('год', str(year) + ':', False)

is_year_leap(2024)


