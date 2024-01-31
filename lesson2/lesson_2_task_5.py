def month_to_season(month:int):
    if month >= 0 and month <= 2:
        print('Зима')
    elif month >= 3 and month <= 5:
        print('Весна')
    elif month >= 6 and month <= 8:
        print('Лето')
    elif month >= 9 and month <= 11:
        print('Осень')
    else:
        month == 12
        print('Зима')

month_to_season(2)