"""button.py

Button control type

Author: Miguel Guthridge
"""

from devicerep import ControlValue
from .status_data1_control_surface import StatusData1ControlSurface

# Constants
BUTTON_PRESS = 0x7F
BUTTON_RELEASE = 0

class Button(StatusData1ControlSurface):
    """Button control surface
    """
    def recognise(self, event) -> 'ControlValue':
        ret = super().recognise(event)
        if ret._value != BUTTON_RELEASE:
            ret._value = BUTTON_PRESS
        return ret
        
    