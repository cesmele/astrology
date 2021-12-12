from datetime import date
from argparse import ArgumentParser
import sys, re
import math
import random
import time
    
class User:
  def __init__(self):
    
    self.name = input("Type in your name: ") #inputs a user's name
    
    birthday = input("Enter your birthday in the following format MM/DD/YYYY: ") #inputs birthday and checks format
    if len(birthday) != 10:
      raise ValueError("Date not formatted correctly.")
    if birthday[2] != "/" and birthday[5] != "/":
      raise ValueError("Date not formatted correctly.")
    if birthday[0:2].isdigit() == False:
      raise ValueError("Month is not formatted correctly.")
    if birthday[3:5].isdigit() == False:
      raise ValueError("Day is not formatted correctly.")
    if birthday[6:].isdigit() == False:
      raise ValueError("Day is not formatted correctly.")
    
    month = int(birthday[0:2])
    day = int(birthday[3:5])
    year = birthday[6:]
    
    if int(birthday[0:2]) < 0 or int(birthday[0:2]) > 12: #check if it's an actual date
      raise ValueError("Date does not exist.")
    if  day < 1 or day > 31:
      raise ValueError("Date does not exist")
    if month == 2 and day > 29 and int(birthday[6:]) % 4 == 0:
      raise ValueError("Date does not exist")
    if month == 2 and day > 28 and int(birthday[6:]) % 4 != 0:
      raise ValueError("Date does not exist")
    if month == 4 and day > 30: 
      raise ValueError("Date does not exist")
    if month == 6 and day > 30: 
      raise ValueError("Date does not exist")
    if month == 9 and day > 30: 
      raise ValueError("Date does not exist")
    if month == 11 and day > 30: 
      raise ValueError("Date does not exist")
    else:
      self.age = age_convert(int(year), month, day) #creates age
      self.zodiac = zodiac_convert(month, day) #forms zodiac
      self.chinese_zodiac = chinese_zodiac_convert(year) #forms chinese zodiac
      self.matches = [] # a place to hold matches
      self.inbox = [] #a place to hold messages  
    
    user_range = input("Enter the age group you are interested in (18-25, 26-30, 31-40, 41-50 or over 50): ") #assigns age range to user
    if user_range == "18-25": 
      self.range = user_range
    elif user_range == "26-30":
      self.range = user_range
    elif user_range == "31-40":
      self.range = user_range
    elif user_range == "41-50":
      self.range = user_range
    elif user_range == "over 50":
      self.range = user_range
    else:
      raise ValueError("Improper age range selected.")
      
class People:
  """Creates People
  
  Attributes:
    catalog(dict):  A dictionary of names and their respective age, zodiac, chinese_zodiac, email, matches, inbox
  """
    
    #takes a file path and forms a catalog with each person having their own info
  def __init__(self, path):
    """Initializes People

    Args:
      path (str): a str containing the path of the people information file to read
    """
        
    self.catalog = {}
    with open(path, "r", encoding = "utf-8") as f:
      for line in f:
          line = line.strip()
          split_line = line.split(",")
          name = split_line[0]
          birthday = split_line[1]
          email = split_line[2]
          birth_data_file = date_iterator(birthday)
          month = int(birth_data_file[0])
          day = int(birth_data_file[1])
          year = int(birth_data_file[2])
          zodiac = zodiac_convert(month, day)
          chinese_zodiac = chinese_zodiac_convert(year)
          age = age_convert(year, month, day) #creates age
          matches = [] # a place to hold matches
          inbox = [] #a place to hold messages  
          self.catalog[name] = [age, zodiac, chinese_zodiac, email, matches, inbox]
          
def age_convert(year, month, day):
  """creates age based on birthday

  Args:
      year (int): year of date of birth
      month (int): month of date of birth
      day (int): day of date of birth

  Returns:
      int: age of the person
  """
  
  today = date.today()
  birthday = date(year, month, day)
  age = today - birthday
  age = math.floor(age.days/365)
  return age
          
def date_iterator(date):
    
  """grabs month day and year from a date
  Args:
    date(str): date read in   

  Returns:
      tuple: int of month, day, year from date
  """
  date.split("/")
  date_split = date.split("/")
  month = date_split[0]
  day = date_split[1]
  year = date_split[2]
              
  return month, day, year
        
def zodiac_convert(month, day):

  if month == 1:
    if day <= 19:
      return "Capricorn"
    else:
      return "Aquarius"
  elif month == 2:
    if day <= 18:
      return "Aquarius"
    else:
      return "Pisces"
  elif month == 3:
    if day <= 20:
      return "Pisces"
    else:
      return "Aries"
  elif month == 4:
    if day <= 19:
      return "Aries"
    else:
      return "Taurus"
  elif month == 5:
    if day <= 20:
      return "Taurus"
    else:
      return "Gemini"
  elif month == 6:
    if day <= 20:
      return "Gemini"
    else:
      return "Cancer"
  elif month == 7:
    if day <= 22:
      return "Cancer"
    else:
      return "Leo"
  elif month == 8:
    if day <= 22:
      return "Leo"
    else:
      return "Virgo"
  elif month == 9:
    if day <= 22:
      return "Virgo"
    else:
      return "Libra"
  elif month == 10:
    if day <= 22:
      return "Libra"
    else:
      return "Scorpio"
  elif month == 11:
    if day <= 21:
      return "Scorpio"
    else:
      return "Sagittarius"
  elif month == 12:
    if day <= 21:
      return "Sagittarius"
    else:
      return "Capricorn"
   
def compatibilities(zodiacsign):

    if zodiacsign == "Aries":
        return "Sagittarius", "Gemini", "Libra"
    elif zodiacsign == "Taurus":
        return "Capricon", "Virgo", "Cancer"
    elif zodiacsign == "Gemini": 
        return "Libra", "Sagittarius", "Aquarius"
    elif zodiacsign == "Cancer": 
        return "Scorpio", "Pisces", "Virgo"
    elif zodiacsign == "Leo":
        return "Sagittarius", "Aquarius", "Gemini"
    elif zodiacsign == "Virgo":
        return "Scorpio", "Taurus", "Capricorn"
    elif zodiacsign == "Libra":
        return "Libra", "Aries", "Aquarius"
    elif zodiacsign == "Scorpio":
        return "Cancer", "Pisces", "Virgo"
    elif zodiacsign == "Capricorn":
        return "Virgo", "Capricorn"
    elif zodiacsign == "Aquarius":
        return "Libra", "Gemini", "Aquarius"
    elif zodiacsign == "Pisces":
        return "Cancer", "Capricorn", "Scorpio"
    elif zodiacsign == "Sagittarius":
        return "Aries", "Leo"   
             
def chinese_zodiac_convert(year):
  """Matches birth year to respective animal

  Args:
      year (str or int): birth year of a person

  Returns:
      str: animal matching the birth year
  """
  zodiac={0:"Monkey",
          1:"Rooster",
          2:"Dog",
          3:"Pig",
          4:"Rat",
          5:"Ox",
          6:"Tiger",
          7:"Rabbit",
          8:"Dragon",
          9:"Snake",
          10:"Horse",
          11:"Sheep"
          }
  key= int(year)%12
  return zodiac[key]
        
def chinese_zodiac_compatibilities(chinese_zodiac_sign):
  """Gives the best compatible chinese zodiac for the respective animal

  Args:
      chinese_zodiac_sign (str): zodiac animal of the person

  Returns:
     tuple: collection of strings containing the compatible animals
  """
    
  CZ_best={"Monkey":("Ox", "Rabbit"),
              "Rooster":("Ox", "Snake"),
              "Dog":("Rabbit"),
              "Pig":("Tiger", "Rabbit", "Sheep"),
              "Rat":("Ox", "Dragon", "Monkey"),
              "Ox":("Rat", "Snake", "Rooster"),
              "Tiger":("Dragon", "Horse", "Pig"),
              "Rabbit":("Sheep", "Monkey", "Dog", "Pig"),
              "Dragon":("Rooster", "Rat", "Monkey"),
              "Snake":("Dragon", "Rooster"),
              "Horse":("Tiger", "Sheep", "Rabbit"),
              "Sheep":("Horse", "Rabbit", "Pig"),
      }
  
  
  return CZ_best[chinese_zodiac_sign]
  
def match_range(user, dictionary):
  """gets a dictionary of people that are in the wanted age range
  
  Args:
    user(User): a User object
    dictionary(dict): a dictionary of People
  
  Returns:
    dict: a dictionary of people that matches the wanted age range
  """  

  matched_ranges = {}
  if user.range == "18-25":
    for key in dictionary.keys():
      age = dictionary[key][0]
      if age < 26 and age > 17:
        matched_ranges[key] = dictionary[key]
  if user.range == "26-30":
    for key in dictionary.keys():
      age = dictionary[key][0]
      if age > 25 and age < 31:
        matched_ranges[key] = dictionary[key]
  if user.range == "31-40":
    for key in dictionary.keys():
      age = dictionary[key][0]
      if age >= 31 and age <= 40:
        matched_ranges[key] = dictionary[key]
  if user.range == "41-50":
    for key in dictionary.keys():
      age = dictionary[key][0]
      if age >= 41 and age <= 50:
        matched_ranges[key] = dictionary[key]
  if user.range == "over 50":
    for key in dictionary.keys():
      age = dictionary[key][0]
      if age > 50:
        matched_ranges[key] = dictionary[key]
  
  return matched_ranges

def match_zodiac(user, dictionary):
  match_dictionary = {}
  zodiac = user.zodiac
  matches = compatibilities(zodiac)
  for item in matches:
    for key in dictionary.keys():
      if item == dictionary[key][1]:
        match_dictionary[key] = dictionary[key]
        
  return match_dictionary

def match_cnzodiac(user, dictionary):
  match_dictionary = {}
  zodiac = user.chinese_zodiac
  matches = chinese_zodiac_compatibilities(zodiac)
  for item in matches:
    for key in dictionary.keys():
      if item == dictionary[key][2]:
        match_dictionary[key] = dictionary[key]
        
  return match_dictionary

def show_matches(zodiac, chinese_zodiac):
  """show compatible zodiacs

  Args:
      zodiac (str): western zodiac
      chinese_zodiac (str): chinese zodiac
  
  Side effects
    prints user's two zodiacs and their compatible zodiacs
  """
  zodiac_compatibility = compatibilities(zodiac)
  cn_compatability = chinese_zodiac_compatibilities(chinese_zodiac)
  print(f"Your signs: {zodiac}, {chinese_zodiac}")
  print(f"Your zodiac matches are: {zodiac_compatibility}")
  print(f"Your chinese zodiac matches are: {cn_compatability}")
  
def match(user, dictionary):
  """match user to people with compatible zodiacs

  Args:
      user (User): a User object
      dictionary (dict): dictionary of potential matches
  
  Side effects:
      prints people with compatible zodiacs, and lets user send a request to them.

  """
  show_matches(user.zodiac, user.chinese_zodiac)
  range_match = match_range(user, dictionary)
  zodiac_match = match_zodiac(user, range_match)
  cn_match = match_cnzodiac(user, range_match)
  full_match = match_cnzodiac(user, zodiac_match)
  
  compatibles = cn_match|zodiac_match
  
  time.sleep(1)
  print()
  
  print("Your zodiac compatibles are:")
  for key in zodiac_match.keys():
    print(f"{key}: {zodiac_match[key][0]}, {zodiac_match[key][1]}")
  
  time.sleep(1)
  print()
  
  print("Your chinese zodiac compatibles are:")
  for key in cn_match.keys():
    print(f"{key}: {cn_match[key][0]}, {cn_match[key][2]}")
  
  time.sleep(1)
  print()
  
  print("Your potential matches are:")
  for key in full_match.keys():
    print(f"{key}: {full_match[key][0]}, {full_match[key][1]}, {full_match[key][2]}")
  
  time.sleep(1)
  print()
  
  if len(full_match) == 0:
    print("No complete matches found")
    print()
    name = input("Since no complete matches were found, type in a full name of one of your chinese zodiac/zodiac compatables: ")
    email = get_email(name, compatibles)
    send_message(user, name, email, compatibles)
    weaker_person_response(user, name, compatibles)
    
  else:
    name = input("Enter a full name of one of your potential matches to send a request: ")
    email = get_email(name, full_match)
    send_message(user, name, email, full_match)
    person_response(user, name, dictionary)
          
def get_email(name, catalog):
  
  #grabs email from catalog
        
  if name in catalog:
    return catalog[name][3]
  else:
    raise KeyError("Name not found")

def send_message(user, name, email, catalog):
  """sends a message to a person in the catalog and add it to their inbox

  Args:
      user (User): a user object
      name (str): message recipient
      email (str): email of message recipient
      catalog (dict): dictionary of people
  
  Side effects:
      prints prompt and send friend request
  """
  
  
  
  message = input(f"Send a messsage/friend request to {name}: ")
  
  for name in catalog:
    if email == catalog[name][3]:
      catalog[name][5].append(f"New request from {user.name}: {message}") #adds a message to other person's inboc
      print (f"{name} recieved your friend request: {message}")
      
def person_response(user, name, catalog):
  
  time.sleep(3) #simulates time waiting for a reply
  response_variable = random.randint(0,9)
  
  if response_variable > 2: #offers a high chance to return a match
    catalog[name][4].append(f"{user.name}") #adds user's name into this person's list of matches
    print(f"{name} accepted your friend request! You have a match! Here is their info!")
    print(f"{name}: {catalog[name][0:4]}") #this reveals user info after the match
    user.matches.append(name)
  else:
    print(f"{name} did not accept your friend request.") #outputs whether or not they were accepted
    
def weaker_person_response(user, name, catalog):
  
  time.sleep(3)
  response_variable = random.randint(0,9)
  
  if response_variable > 7: #offers a low chance to return a match
    catalog[name][4].append(f"{user.name}")
    print(f"{name} accepted your friend request! You have a match! Here is their info!")
    print(f"{name}: {catalog[name][0:4]}")
    user.matches.append(name)
  else:
    print(f"{name} did not accept your friend request.")
    
def main(f):
  
    people = People(f)
    user = User()
    catalog = people.catalog
    match(user, catalog)

def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("filename", help="textfile containing people's information to match")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename)