"""nullcontrol.py

Represents when an event maps to a control that should be disregarded (for
example if it is used internally to adjust button mappings, such as an 'alt'
button)

Author: Miguel Guthridge
"""

from . import ControlSurface

class NullControl(ControlSurface):
    """A control that should be disregarded outside of the controller's internal
    state.
    """
