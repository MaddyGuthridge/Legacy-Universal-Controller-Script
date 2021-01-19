"""
helpers.py

Contains helper functions for things

Author: Miguel Guthridge
"""
import internal.consts
import config

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




def getLineBreak():
    """
    Returns a series of - characters to simulate a ruled line break. Useful when printing stuff
    """
    return "————————————————————————————————————————————————————"


def getTab(string, multiplier = 1, length = internal.consts.LOG_TAB_LENGTH):
    """Returns your string plus spaces to make the string length equal to a multiple of the tab length defined in config.py

    Args:
        string (str): the string to append to
        multiplier (int, optional): the number of tabs to do (useful for alligning statements when things get long). Defaults to 1.
        length (int, optional): how far to tab across. Defaults to config.TAB_LENGTH.

    Returns:
        str: the original string with spaces appended to it to equal a tab
    """
    string += " "
    toAdd = (length * multiplier) - len(string) % (length * multiplier)

    for x in range(toAdd):
        string += " "
    return string

def getModuleName(string):
    """Returns the name of a module by replacing non-module-able characters
    
    
    DEPRECATED as of v0.4: Using sysex to identify devices
    """ 
    # Loop over string and strip bad characters
    
    
    i = 0
    found_non_digit = False
    while i < len(string):
        
        if string[i].isdigit():
            if not found_non_digit:
                string = string[ : i] + string[i + 1 : ]
                continue
        else:
            found_non_digit = True
        
        if string[i] == '-':
            string = string[ : i] + string[i + 1 : ]
            continue
        
        elif string[i] == ' ':
            string = string[ : i] + '_' + string[i + 1 : ]
        
        i += 1
    
    return string
        

def debugLog(message, level = 0):
    """Print a message for debugging, but only if the debug mode includes the debug type specified

    Args:
        message (str): what to log
        level (int, optional): the message type. Should be in the form of consts.DEBUG_SOME_MODE. Defaults to 0.
    """
    if level in config.CONSOLE_DEBUG_MODE or level == internal.consts.DEBUG.ERROR:
        print(message)