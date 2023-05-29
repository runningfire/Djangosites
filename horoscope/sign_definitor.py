def sign_definitor(month: int, day: int) -> str:
    if month == 1:
        if day < 21:
            sign = 'capricorn'
        else:
            sign = 'aquarius'
        if (day <= 0) or (day > 31):
            sign = 'Некорректный ввод дня'
    elif month == 2:
        if day < 19:
            sign = 'aquarius'
        else:
            sign = 'pisces'
        if (day <= 0) or (day > 28):
            sign = 'Некорректный ввод дня'
    elif month == 3:
        if day < 21:
            sign = 'pisces'
        else:
            sign = 'aries'
        if (day <= 0) or (day > 31):
            sign = 'Некорректный ввод дня'
    elif month == 4:
        if day < 20:
            sign = 'aries'
        else:
            sign = 'taurus'
        if (day <= 0) or (day > 30):
            sign = 'Некорректный ввод дня'
    elif month == 5:
        if day < 21:
            sign = 'taurus'
        else:
            sign = 'gemini'
        if (day <= 0) or (day > 31):
            sign = 'Некорректный ввод дня'
    elif month == 6:
        if day < 22:
            sign = 'gemini'
        else:
            sign = 'cancer'
        if (day <= 0) or (day > 30):
            sign = 'Некорректный ввод дня'
    elif month == 7:
        if day < 23:
            sign = 'cancer'
        else:
            sign = 'leo'
        if (day <= 0) or (day > 31):
            sign = 'Некорректный ввод дня'
    elif month == 8:
        if day < 23:
            sign = 'leo'
        else:
            sign = 'virgo'
        if (day <= 0) or (day > 31):
            sign = 'Некорректный ввод дня'
    elif month == 9:
        if day < 23:
            sign = 'virgo'
        else:
            sign = 'libra'
        if (day <= 0) or (day > 30):
            sign = 'Некорректный ввод дня'
    elif month == 10:
        if day < 24:
            sign = 'libra'
        else:
            sign = 'scorpio'
        if (day <= 0) or (day > 31):
            sign = 'Некорректный ввод дня'
    elif month == 11:
        if day < 23:
            sign = 'scorpio'
        else:
            sign = 'sagittarius'
        if (day <= 0) or (day > 30):
            sign = 'Некорректный ввод дня'
    elif month == 12:
        if day < 22:
            sign = 'sagittarius'
        else:
            sign = 'capricorn'
        if (day <= 0) or (day > 31):
            sign = 'Некорректный ввод дня'
    else:
        sign = 'Некорректный ввод месяца'
    return sign
