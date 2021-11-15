import random

def zodiac_sign(month, day):
  if month == "January":
    if day <= 19:
      return "Capricorn"
    else:
      return "Aquarius"
  elif month == "February":
    if day <= 18:
      return "Aquarius"
    else:
      return "Pisces"
  elif month == "March":
    if day <= 20:
      return "Pisces"
    else:
      return "Aries"
  elif month == "April":
    if day <= 19:
      return "Aries"
    else:
      return "Taurus"
  elif month == "May":
    if day <= 20:
      return "Taurus"
    else:
      return "Gemini"
  elif month == "June":
    if day <= 20:
      return "Gemini"
    else:
      return "Cancer"
  elif month == "July":
    if day <= 22:
      return "Cancer"
    else:
      return "Leo"
  elif month == "August":
    if day <= 22:
      return "Leo"
    else:
      return "Virgo"
  elif month == "September":
    if day <= 22:
      return "Virgo"
    else:
      return "Libra"
  elif month == "October":
    if day <= 22:
      return "Libra"
    else:
      return "Scorpio"
  elif month == "November":
    if day <= 21:
      return "Scorpio"
    else:
      return "Sagittarius"
  elif month == "December":
    if day <= 21:
      return "Sagittarius"
    else:
      return "Capricorn"



