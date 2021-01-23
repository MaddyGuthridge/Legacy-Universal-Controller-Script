""" deviceconfig > devices.py

This file prepares device configurations to be imported during setup

Author: Miguel guthridge [hdsq@outlook.com.au]
"""

#
# Add device folder names to this list so they can be imported
# Note that folder names, cannot have spaces, punctuation or leading digits 
#
IMPORT_LIST = ["launchkeymk2"]

# Import configurations
success_count = 0
imports = []
for x in IMPORT_LIST:
    try:
        this = __import__("deviceconfig." + x)
        imports.append(getattr(this, x))
        success_count += 1
    except Exception as e:
        print("An error occured whilst importing device configuration: " + x)
        print("Ensure that the device's __init__.py configuration has been set up correctly [copied from the template] and try again")
        print("Error message:", e)
print("Successfully imported " + str(success_count) + " of " + str(len(IMPORT_LIST)) + " device configurations")

def loadSetup(identifier_str):
    """Loads the setup and runs autoinit.py for the controller specified by the identifier

    Args:
        identifier_str (str): hexadecimal identifier for the controller (from a
                                universal device inquiry)
    
    Returns: int
        1: successful import from devices
        2: successful import from default autoinit script
        0: no matches
       -1: error importing
    """
    
    # Import from proper list
    for i in imports:
        if identifier_str in i.config.SUPPORTED_DEVICE_IDS:
            try:
                i.initialise()
            except Exception as e:
                print("Error while importing device properties:", e)
                return -1
            return 1
    
    # Import from default configuration
    try:
        __import__("deviceconfig.autoinit")
        return 2
    
    # Filed to import
    except:
        return 0
    