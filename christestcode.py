def input(path):
    
    catalog = {}
    
    with open(path, "r", encoding = "utf-8") as f:
            
            for line in f:
                line = line.strip()
                split_line = line.split(",")
                name = split_line[0]
                date = split_line[1]
                date_split = date.split("/")
                month = date_split[0]
                day = date_split[1]
                year = date_split[2]
                time = split_line[2]
                hour = time[:2]
                minute = time[3:5]
                meridiem = time[-2:]
                
                
                catalog[name] = int(month), int(day), int(year), int(hour), int(minute), meridiem
                
    print(catalog)
    
input("/Library/School/INST326/CODE/CodeFiles/astrology/people.txt")