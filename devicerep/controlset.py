"""controlset.py

Contains class definition for set of controls.

Author: Miguel Guthridge
"""

from . import ControlSurface, ControlMapping

class ControlSet:
    """Set of grouped controls
    """
    
    def __init__(self, name: str) -> None:
        self._controls = []
        self._name = name
    
    def addControl(self, set: int, control: ControlSurface):
        """Add a control to the control set and return its mapping

        Args:
            set (int): the ID of this set (for generating mapping)
            control (ControlSurface): control object
        """
        mapping = ControlMapping(set, len(self._controls))
        control.setMapping(mapping)
        self._controls.append(control)
        return mapping
