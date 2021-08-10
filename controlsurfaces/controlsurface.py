"""controlsurface.py

Contains class definition for a generic control surface

Author: Miguel Guthridge
"""

class ControlSurface:
    """Object representing a generic control surface
    """
    def __init__(self, control_map:ControlMapping):
        """Create a ControlSurface instance

        Args:
            control_map (ControlMapping): mapping for control within device
        """
        self.mapping = control_map
        # MIDI Value of the control
        self.value = 0
        # Hex colour of the control
        self.colour = 0xFFFFFF
        # Description string for the control
        self.description = ""

    def recognise(self, event) -> ControlValue:
        """If the event is recognised as mapping to this control surface,
        returns a control value representing the internal value, and how it
        maps to this control

        Args:
            event (FlEvent): event to recognise

        Returns:
            ControlValue: whether event was a match
        """
        return NotImplemented

    def setVal(self, new_val:ControlValue) -> None:
        """Set the value of this control to that of the event

        Args:
            new_val (ControlValue): New value for the control
        """
        self.value = new_val.value
