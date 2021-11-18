class chinese_zodiac():
    
    def __init__(self,year):
        Best={"Monkey":{("Ox", "Rabbit")},
                "Rooster":{("Ox, Snake")},
                "Dog":{("Rabbit")},
                "Pig":{("Tiger, Rabbit, Sheep")},
                "Rat":{("Ox, Dragon, Monkey")},
                "Ox":{("Rat, Snake, Rooster")},
                "Tiger":{("Dragon, Horse, Pig")},
                "Rabbit":{("Sheep, Monkey, Dog, Pig")},
                "Dragon":{("Rooster, Rat, Monkey")},
                "Snake":{("Dragon, Rooster")},
                "Horse":{("Tiger, Sheep, Rabbit")},
                "Sheep":{("Horse, Rabbit, Pig")},
        }
        Worse={"Monkey":{("Tiger", "Pig")},
                "Rooster":{("Rat, Rabbit, Horse, Rooster, Dog")},
                "Dog":{("Dragon, Sheep, Rooster")},
                "Pig":{("Snake, Monkey")},
                "Rat":{("Tiger", "Pig")},
                "Ox":{("Tiger, Dragon, Horse, Sheep")},
                "Tiger":{("Ox, Tiger, Snake, Monkey")},
                "Rabbit":{("Snake, Rooster")},
                "Dragon":{("Ox, Sheep, Dog")},
                "Snake":{("Tiger, Rabbit, Snake, Sheep, Pig")},
                "Horse":{("Rat, Ox, Rooster, Horse")},
                "Sheep":{("Ox, Tiger, Dog")}
               }
        self.animal=self.year_to_animal(year)
        self.best_compat=str(Best[self.animal])
        self.worse_compat=str(Worse[self.animal])
    
    def __repr__(self):
        return f"{self.animal}"
    
    def year_to_animal(self,year):
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
        key= year%12
        return zodiac[key]
    
    
    def best_compatibility(self):
        a=(str(self.best_compat.replace("{","").replace("}", "")))
        a=a.replace("'", "")
        return f"Best compatibility for {self.animal}s are {(a)}"
    
    def worse_compatibility(self):
        b=(str(self.worse_compat.replace("{","").replace("}", "")))
        b=b.replace("'", "")
        return f"Worst compatibility for {self.animal}s are {(b)}"
    
    def compat(self):
        a=(str("Best with "+(self.best_compat.replace("{","").replace("}",""))))
        a=a.replace("'", "")
        b=(str("Worst with "+(self.worse_compat.replace("{","").replace("}", ""))))
        b=b.replace("'", "")
        return f"Compatibility for {self.animal}s are {a} and {b}"
    
    def is_compat(self,other):
        if isinstance(other, int):
            other= self.year_to_animal(other)
        elif any(char.isdigit() for char in other):
            other=int(other)
            other= self.year_to_animal(other)   
        if other in self.best_compat:
            return f"{self.animal} is compatible with {other}"
        else:
            return f"{self.animal} is not compatible with {other}"

        
        
