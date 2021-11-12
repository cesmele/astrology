class chinese_zodiac():
    def __init__(self,year):
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
        key=year%12
        self.animal=(zodiac[key])
    def __repr__(self):
        return f"{self.animal}, {self.compatibility(self.animal)}"
    def compatibility(self,animal):
        compat={"Monkey":{"Best":("Ox", "Rabbit"),"Worst":("Tiger", "Pig")},
                "Rooster":{"Best":("Ox, Snake"),"Worst":("Rat, Rabbit, Horse, Rooster, Dog")},
                "Dog":{"Best":("Rabbit"),"Worst":("Dragon, Sheep, Rooster")},
                "Pig":{"Best":("Tiger, Rabbit, Sheep"),"Worst":("Snake, Monkey")},
                "Rat":{"Best":("Ox, Dragon, Monkey"),"Worst":("Tiger", "Pig")},
                "Ox":{"Best":("Rat, Snake, Rooster"),"Worst":("Tiger, Dragon, Horse, Sheep")},
                "Tiger":{"Best":("Dragon, Horse, Pig"),"Worst":("Ox, Tiger, Snake, Monkey")},
                "Rabbit":{"Best":("Sheep, Monkey, Dog, Pig"),"Worst":("Snake, Rooster")},
                "Dragon":{"Best":("Rooster, Rat, Monkey"),"Worst":("Ox, Sheep, Dog")},
                "Snake":{"Best":("Dragon, Rooster"),"Worst":("Tiger, Rabbit, Snake, Sheep, Pig")},
                "Horse":{"Best":("Tiger, Sheep, Rabbit"),"Worst":("Rat, Ox, Rooster, Horse")},
                "Sheep":{"Best":("Horse, Rabbit, Pig"),"Worst":("Ox, Tiger, Dog")}
        }
        a=(str(compat[animal]).replace("{","").replace("}", ""))
        return f"Compatibility for {animal} is {str(a)}"
    
print(chinese_zodiac(2001))
        
        
