import random

def zodiac_sign(month=str(input("Enter birth month: ")),  day=int(input("Enter birth day: "))):
    if month.lower() == "January":
        if day <= 19:
            result = "Capricorn"
        else:
            result = "Aquarius"
    elif month.lower() == "February":
        if day <= 18:
            result = "Aquarius"
        else:
            result = "Pisces"
    elif month.lower() == "March":
        if day <= 20:
            result = "Pisces"
        else:
            result = "Aries"
    elif month.lower() == "April":
        if day <= 19:
            result = "Aries"
        else:
            result = "Taurus"
    elif month.lower == "May":
        if day <= 20:
            result = "Taurus"
        else:
            result = "Gemini"
    elif month.lower() == "June":
        if day <= 20:
            result = "Gemini"
        else:
            result = "Cancer"
    elif month.lower == "July":
        if day <= 22:
            result = "Cancer"
        else:
            result = "Leo"
    elif month.lower == "August":
        if day <= 22:
            result = "Leo"
        else:
            result = "Virgo"
    elif month.lower == "September":
        if day <= 22:
            result = "Virgo"
        else:
            result = "Libra"
    elif month.lower() == "October":
        if day <= 22:
            result = "Libra"
        else:
            result = "Scorpio"
    elif month.lower == "November":
        if day <= 21:
            result = "Scorpio"
        else:
            result = "Sagittarius"
    elif month.lower == "December":
        if day <= 21:
            result = "Sagittarius"
        else:
            result = "Capricorn"



