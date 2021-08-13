"""controlsurface.py

Contains class definition for a generic control surface

Author: Miguel Guthridge
"""

from . import ControlMapping, ControlValue

class ControlSurface:
    """Object representing a generic control surface
    """
    def __init__(self):
        """Create a ControlSurface instance

        Args:
            control_map (ControlMapping): mapping for control within device
        """
        self._mapping = None
        # MIDI Value of the control
        self._value = 0
        # Hex colour of the control
        self._colour = 0xFFFFFF
        # Description string for the control
        self._description = ""

    def setMapping(self, mapping: 'ControlMapping') -> None:
        """Set the mapping of the control
        
        WARNING: This should only be called by the DeviceState object when
        adding the control to a device

        Args:
            mapping (ControlMapping): new mapping
        """
        if self._mapping is None:
            self._mapping = mapping
        else:
            raise Exception("Mapping already set")

    def recognise(self, event) -> 'ControlValue':
        """If the event is recognised as mapping to this control surface,
        returns a control value representing the internal value, and how it
        maps to this control. Otherwise returns None

        Args:
            event (FlEvent): event to recognise

        Returns:
            ControlValue: whether event was a match
        """
        return NotImplemented

    def setVal(self, new_val: 'ControlValue') -> None:
        """Set the value of this control to that of the event

        Args:
            new_val (ControlValue): New value for the control
        """
        self._value = new_val.getValue()

    def getValue(self) -> 'ControlValue':
        """Get the current value of the control

        Returns:
            ControlValue: current value
        """
        if self._mapping is None:
            raise Exception("Control was never mapped")
        return ControlValue(self._mapping, self._value)
