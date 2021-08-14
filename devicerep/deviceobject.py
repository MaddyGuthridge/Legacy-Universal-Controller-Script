"""deviceobject.py

Contains the definition for a generic DeviceObject

Author: Miguel Guthridge
"""

from . import DeviceState, ControlValue

class DeviceObject:
    """An object representing a generic device and its state
    
    Each device should inherit from this class, filling its state object with 
    custom ControlSurfaces in order to build a complete representation of the
    device.
    """
    def __init__(self) -> None:
        """Create an instance of the device
        
        NOTE: When extending this class, call the super().__init__() function
        and then add event instances to recognise.
        """
        self._state = DeviceState()
 
    def recognise(self, event) -> ControlValue:
        """Recognise an event and return its ControlValue mapping

        Args:
            event (FlEvent): Event to recognise

        Returns:
            ControlValue: Mapping
        
        Raises:
            MidiRecogniseException: Event not recognised
        """
        return self._state.recognise(event)
