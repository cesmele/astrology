def compatibilities(self, zodiacsign):
    self.zodiacsign = zodiacsign
    compatibility = ()
    if zodiacsign == "Aries":
        compatibility.append("Sagittarius", "Gemini", "Libra")
        print(f"You are most compatible with {compatibility[0]}, {compatibility[1]}, and {compatibility[2]}.")
    elif zodiacsign == "Taurus":
        compatibility.append("Capricon", "Virgo", "Cancer")
        print(f"You are most compatible with {compatibility[0]}, {compatibility[1]}, and {compatibility[2]}.")
    elif zodiacsign == "Gemini": 
        compatibility.append("Libra", "Sagittarius", "Aquarius")
        print(f"You are most compatible with {compatibility[0]}, {compatibility[1]}, and {compatibility[2]}.")
    elif zodiacsign == "Cancer": 
        compatibility.append("Scorpio", "Pisces", "Virgo")
        print(f"You are most compatible with {compatibility[0]}, {compatibility[1]}, and {compatibility[2]}.") 
    elif zodiacsign == "Leo":
        compatibility.append("Sagittarius", "Aquarius", "Gemini")
        print(f"You are most compatible with {compatibility[0]}, {compatibility[1]}, and {compatibility[2]}.")
    elif zodiacsign == "Virgo":
        compatibility.append("Scorpio", "Taurus", "Capricorn")
        print(f"You are most compatible with {compatibility[0]}, {compatibility[1]}, and {compatibility[2]}.")
    elif zodiacsign == "Libra":
        compatibility.append("Libra", "Aries", "Aquarius")
        print(f"You are most compatible with {compatibility[0]}, {compatibility[1]}, and {compatibility[2]}.")
    elif zodiacsign == "Scorpio":
        compatibility.append("Cancer", "Pisces", "Virgo")
        print(f"You are most compatible with {compatibility[0]}, {compatibility[1]}, and {compatibility[2]}.")
    elif zodiacsign == "Capricorn":
        compatibility.append("Virgo", "Capricorn")
        print(f"You are most compatible with {compatibility[0]} and {compatibility[1]}.")
    elif zodiacsign == "Aquarius":
        compatibility.append("Libra", "Gemini", "Aquarius")
        print(f"You are most compatible with {compatibility[0]}, {compatibility[1]}, and {compatibility[2]}.")
    elif zodiacsign == "Pisces":
        compatibility.append("Cancer", "Capricorn", "Scorpio")
        print(f"You are most compatible with {compatibility[0]}, {compatibility[1]}, and {compatibility[2]}.")