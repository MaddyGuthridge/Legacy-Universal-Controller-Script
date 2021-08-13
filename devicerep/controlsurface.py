"""controlsurface.py

Contains class definition for a generic control surface

Author: Miguel Guthridge
"""

from . import ControlMapping, ControlValue

class ControlSurface:
    """Object representing a generic control surface
    """
    def __init__(self) -> None:
        """Create a ControlSurface instance
        """
        self._mapping = None
        
        # Set all values to default
        self.resetControl()

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
        # TODO: Set up a basic event detection system
        raise NotImplementedError("Method must be overridden")

    def resetControl(self) -> None:
        """Reset the state of the control to its default value, including the
        value, colour, and description.
        
        Calls the setProperty() methods, so that any required MIDI events are
        sent to the controller to reset values there.
        """
        self.setVal(0)
        self.setColour(0x000000)
        self.setDescription("")

    def setVal(self, new_val: 'ControlValue') -> None:
        """Set the value of this control to that of the event
        
        NOTE: This should be extended by device-specific implementations to send
        a MIDI message if the device can set values for a type.
        If the control surface requires specific value types (eg direction for a
        click wheel or d-pad), the type of `new_val` should be overridden too.

        Args:
            new_val (ControlValue): New value for the control
        """
        self._value = new_val.getValue()

    def getValue(self) -> 'ControlValue':
        """Get the current value of the control

        Returns:
            ControlValue: current value associated with control
        """
        if self._mapping is None:
            raise Exception("Control was never mapped")
        return ControlValue(self._mapping, self._value)

    def setColour(self, colour: int) -> None:
        """Set a new colour for the control

        NOTE: As with setValue(), this should be extended to send the required
        MIDI events if the device supports it.

        Args:
            colour (int): Hex colour 0xRRGGBB
        """
        self._colour = colour
    
    def getColour(self) -> int:
        """Get the current colour of the control

        Returns:
            int: Hex colour 0xRRGGBB
        """
        return self._colour
    
    def setDescription(self, desc: str) -> None:
        """Set a new description for the control

        NOTE: As with setValue(), this should be extended to send the required
        MIDI events if the device supports it.

        Args:
            desc (str): new description
        """
        self._description = desc
    
    def getDescription(self) -> str:
        """Get the current description of the control

        Returns:
            str: Description
        """
        return self._description
