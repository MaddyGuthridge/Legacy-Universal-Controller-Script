

def getLineBreak():
    return "################################"

def getNumSuffix(number):
    if 10 < number % 100 < 20:
        return str(number) + "th"
    elif number % 10 == 1:
        return str(number) + "st"
    elif number % 10 == 2:
        return str(number) + "nd"
    elif number % 10 == 3:
        return str(number) + "rd"
    else:
        return str(number) + "th"
