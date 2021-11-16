class Moon:
    """
    Attributes:
        path(string): a string containing the path to the csv file where the moons
        data is held.
    
    """
    
    def __init__(self,path):
        """
        Will open the path to the full_moon.csv file
        Args:
            path: path to full_
        """
        self.catalog = {}
        with open(path,"r") as f:
           for lines in f :
               lines = lines.strip()
               lines = lines.split(",")
               self.catalog[lines[0]] = (lines[1], float(lines[2]), float(lines[3])) #Day, Date, Month, Year
        
    def get_date(self, date):
        """
        will find the date of the full moon in the csv file. 
        
        Args:
            date: days of full a
            
        """
        if date not in self.catalog:
            print("This date matches that of a date of a full moon.")
        else:
            print("No full moon on this date!")