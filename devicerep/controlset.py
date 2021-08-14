"""controlset.py

Contains class definition for set of controls.

Author: Miguel Guthridge
"""

from . import ControlSurface, ControlMapping, ControlValue

class ControlSet:
    """Set of grouped controls
    """
    
    def __init__(self, name: str, set_index: int) -> None:
        """Create a ControlSet instance

        Args:
            name (str): name of the control set
            set_index (int): index of the control set within the device
        """
        self._controls = []
        self._name = name
        self._index = set_index
    
    def addControl(self, control: ControlSurface) -> None:
        """Add a control to the control set and return its mapping

        Args:
            control (ControlSurface): control object
        """
        mapping = ControlMapping(self._index, len(self._controls))
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

    def resetControls(self) -> None:
        """Send a reset command to each ControlSurface
        """
        for control in self._controls:
            control.resetControl()
