"""deviceidentifier.py

Contains code for identifying a device based on its response to a universal
device enquiry message, and creating an instance of said device

Author: Miguel Guthridge
"""

from devicerep import DeviceObject

# Dictionary of responses and their mappings
# Format:
#   key:    list of valid responses (to allow one object to work with multiple
#           devices of the same family).
#   value:  string containing name of submodule to import and create an instance
#           from.
DEVICE_IDENTIFIERS = {
    
}

def recogniseDeviceSysex(sysex: bytes) -> DeviceObject:
    """Create and return a DeviceObject representing the device of the detected
    controller.

    Args:
        sysex (bytes): SYSEX message response to universal device enquiry

    Returns:
        DeviceObject: device matched by Sysex message (None if not recognised)
    """
    for key, value in DEVICE_IDENTIFIERS.items():
        if sysex in key:
            # Import, create and return
            module = __import__(value, level=1)
            return module.Controller(sysex)
    
    # Device not recognised
    return None
