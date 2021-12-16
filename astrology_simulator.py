from datetime import date
from argparse import ArgumentParser
import sys, re
import math
import random
import time
 
"""
This program will take a list of people and user inputs and form matches
based for the user based on astrology data
""" 
    
class User:
  
  """A class to generate an user object for entering birthdays"""
  
  def __init__(self):
    
    """
    initializes a user object.
    
    Side effects:
      creates a user object with a name, age, zodiac, chinese zodiac, matches list, inbox list and
      preferred range
    
    Raises:
      ValueError: Month is not formatted correctly.
      It will raise this ValueError if the birthdate is not in the correct format.

      ValueError: Date does not exist.
      It will raise this ValueError if the birthdate does not exist.

      ValueError: Improper age range selected.
      It will raise this ValueError if the user does not select an age group within the given range.
    """
    
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
    
    user_range = input("Enter the age group you are interested in (18-25, 26-30, 31-40, 41-50 or over 50): ")
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
    
    
  def __init__(self, path):
    
    """Initializes People, takes a file path and forms a catalog with each person having their own info

    Args:
      path (str): a str containing the path of the people information file to read
      
    Side effects:
      creates a dictionary of people with names as keys and person data as a list
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
    
  """grabs month day and year from a date using regular expressions
  
  
  Args:
    date(str): date read in   

  Returns:
      tuple: int of month, day, year from date
  """
  exp = """(?xm)
  ^
  (?:(?P<month>\d\d))
  (?:\/)
  (?:(?P<day>\d\d))
  (?:\/)
  (?:(?P<year>\d\d\d\d))
  """

  match = re.search(exp, date)
  month = match.group("month")
  day = match.group("day")
  year = match.group("year")
  
  return month, day, year
        
def zodiac_convert(month, day):
  
  """Provides your zodiac sign based on your birthday.

  Args:
      month (int): month of date of birth
      day (int): day of date of birth

  Returns:
      str: zodiac sign of the person
  """

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
  
    """takes a zodiac sign and return a tuple of their compatibilities.

  Args:
      zodiacsign (str): zodiac sign of the user

  Returns:
      tuple: zodiac signs of the person's compatibility.
   """

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
  """It return a dictionary of all the people in the text file who are compatible 
  with the user based on their zodiac signs.
  
  Args:
    user (User): a User object
    dictionary (dict): a dictionary of People
  
  Returns:
    dict: a dictionary of people that matches the compatibility of the user according
    to their zodiac sign.
  """ 
  match_dictionary = {}
  zodiac = user.zodiac
  matches = compatibilities(zodiac)
  for item in matches:
    for key in dictionary.keys():
      if item == dictionary[key][1]:
        match_dictionary[key] = dictionary[key]
        
  return match_dictionary

def match_cnzodiac(user, dictionary):
  """It return a dictionary of all the people in the text file who are compatible 
  with the user based on their chinese zodiac signs.
  
  Args:
    user (User): a User object
    dictionary (dict): a dictionary of People
  
  Returns:
    dict: a dictionary of people that matches the compatibility of the user according
    to their chinese zodiac sign.
  """ 
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
      prints people with compatible zodiacs, 
      lets user send a request to them and send a message,
      asks user to type in a match based what the algorithm
      allows

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
  """
  It will grab the email from the catelog according to the person's name.

  Args:
    name (str): the person's name
    catelog (a list): a list that has the emails

  Returns:
    str: email from the catelog.
    
  Raises:
    KeyError: if the name argument is not in the catalog
  """
        
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
      prints prompt and friend request sent
  """
  
  message = input(f"Send a messsage/friend request to {name}: ")
  
  for name in catalog:
    if email == catalog[name][3]:
      catalog[name][5].append(f"New request from {user.name}: {message}") #adds a message to other person's inboc
      print (f"{name} recieved your friend request: {message}")
      
def person_response(user, name, catalog):     
  
  """
  Finds potential matches for the user and adds the match name to their
  list of overall matches. It will also reveal the user's information after the 
  match (only if the friend request they sent to their match were accepted). 
  Friend request acceptance chances are a 7/9 chance to assert high proability 
  for complete matches.

  Args:
    user (User): a User object
    name (str): the name of the person
    catelog (a list): a list that has the emails

  Side effects:
    Prints the match information on the console if user accepts
    or prints out that the user doesn't accept, and declines to 
    show user info.

  """
  
  time.sleep(3) 
  response_variable = random.randint(0,9)
  
  if response_variable > 2: 
    catalog[name][4].append(f"{user.name}") 
    print(f"{name} accepted your friend request! You have a match! Here is their info!")
    print(f"{name}: {catalog[name][0:4]}") 
    user.matches.append(name)
  else:
    print(f"{name} did not accept your friend request.") 
    
def weaker_person_response(user, name, catalog):
  
  """
  Finds potential matches for the user and adds the match name to their
  list of overall matches. It will also reveal the user's information after the 
  match (only if the friend request they sent to their match were accepted). 
  Friend request acceptance chances are a 2/9 chance to assert low proability 
  for partial matches.

  Args:
    user (User): a User object
    name (str): the name of the person
    catelog (a list): a list that has the emails

  Side effects:
    Prints the match information on the console if user accepts
    or prints out that the user doesn't accept, and declines to 
    show user info.

  """
  
  time.sleep(3)
  response_variable = random.randint(0,9)
  
  if response_variable > 7: 
    catalog[name][4].append(f"{user.name}")
    print(f"{name} accepted your friend request! You have a match! Here is their info!")
    print(f"{name}: {catalog[name][0:4]}")
    user.matches.append(name)
  else:
    print(f"{name} did not accept your friend request.")
    
def main(f):
    
    """
    Passes in a user object and catelog dictionary to the match function to
    match user to people with compatible zodiacs.

    Args:
      f (str): a str containing the path of the people information file to read
    """
    people = People(f)
    user = User()
    catalog = people.catalog
    match(user, catalog)

def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect one mandatory argument:
        - filename: a path to a CSV file that has the person's information.
  
    Args:
        arglist (list of string): The command line arguments.
    
    Returns:
        namespace: a namespace representing the parsed arguments
    """
    parser = ArgumentParser()
    parser.add_argument("filename", help="textfile containing people's information to match")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename)