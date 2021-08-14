"""deviceobject.py

Contains the definition for a generic DeviceObject

Author: Miguel Guthridge
"""

from . import DeviceState, ControlValue, ControlMapping, ControlSurface

class DeviceObject:
    """An object representing a generic device and its state.
    
    Each device should inherit from this class, filling its state object with 
    custom `ControlSurface`s in order to build a complete representation of the
    device.
    
    NOTE: It is recommended to call the `super().myFunction()` for every
    overridden function so that common functionality can be updated without
    breaking individual device modules, and to reduce duplicate code.
    """
    def __init__(self) -> None:
        """Create an instance of the device
        
        NOTE: For an actual device, after calling `super().__init__()`, you
        should set up all the device's ControlSurfaces in your `__init__()`
        function by using the provided methods in `self._state`.
        """
        self._state = DeviceState()
 
    def getControl(self, mapping: ControlMapping) -> ControlSurface:
        """Return a reference to the `ControlSurface` linked to the given 
        mapping. Used to perform actions on the control surface, for example
        getting or setting its value.

        Args:
            mapping (ControlMapping): mapping to control

        Returns:
            ControlSurface: associated ControlSurface
        """
        return self._state.getControl(mapping)
 
    def recognise(self, event) -> ControlValue:
        """Recognise an event and return its `ControlValue` mapping

        Args:
            event (FlEvent): Event to recognise

        Returns:
            ControlValue: Mapping
        
        Raises:
            MidiRecogniseException: Event not recognised
        """
        return self._state.recognise(event)

    def resetControls(self) -> None:
        """Reset all controls to their default state. This is useful to call
        when switching between plugins to ensure that there aren't any ghost
        parameters that appear linked.
        """
        self._state.resetControls()
