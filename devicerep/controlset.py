"""controlset.py

Contains class definition for set of controls.

Author: Miguel Guthridge
"""

from . import ControlSurface, ControlMapping, ControlValue

class ControlSet:
    """Set of grouped controls
    """
    
    def __init__(self, name: str) -> None:
        self._controls = []
        self._name = name
    
    def addControl(self, set: int, control: ControlSurface) -> None:
        """Add a control to the control set and return its mapping

        Args:
            set (int): the ID of this set (for generating mapping)
            control (ControlSurface): control object
        """
        mapping = ControlMapping(set, len(self._controls))
        control.setMapping(mapping)
        self._controls.append(control)
        return mapping

    def recognise(self, event) -> 'ControlValue':
        """Recognise an event and return its ControlValue. If no matches are
        found, None is returned.
        
        Args:
            event (FlEvent): event to check
        """
        for control in self._controls:
            res = control.recognise(event)
            if res is not None:
                return res

    def getControl(self, mapping: ControlMapping) -> ControlSurface:
        """Return a reference to the ControlSurface linked to a mapping

        Args:
            mapping (ControlMapping): mapping to control

        Returns:
            ControlSurface: associated ControlSurface
        """
        return self._controls[mapping.getControlIndex()]
    
