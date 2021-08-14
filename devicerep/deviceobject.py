"""deviceobject.py

Contains the definition for a generic DeviceObject

Author: Miguel Guthridge
"""

from . import DeviceState, ControlValue, ControlMapping, ControlSurface

class DeviceObject:
    """An object representing a generic device and its state
    
    Each device should inherit from this class, filling its state object with 
    custom ControlSurfaces in order to build a complete representation of the
    device.
    
    NOTE: It is recommended to call the super().myFunction() for every
    overridden function so that common functionality can be updated without
    breaking individual device modules, and to reduce duplicate code.
    """
    def __init__(self) -> None:
        """Create an instance of the device
        
        NOTE: When extending this class, call the super().__init__() function
        and then add event instances to recognise.
        """
        self._state = DeviceState()
 
    def getControl(self, mapping: ControlMapping) -> ControlSurface:
        """Return a reference to the ControlSurface linked to a mapping

        Args:
            mapping (ControlMapping): mapping to control

        Returns:
            ControlSurface: associated ControlSurface
        """
        return self._state.getControl(mapping)
 
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

    def resetControls(self) -> None:
        """Reset all controls to their default state
        """
        self._state.resetControls()
