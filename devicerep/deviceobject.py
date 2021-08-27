"""deviceobject.py

Contains the definition for a generic DeviceObject

Author: Miguel Guthridge
"""

from . import DeviceState, ControlValue, ControlMapping, ControlSet
from controlsurfaces import ControlSurface

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
        
        You should also define which control sets should be mapped towards which
        FL Studio targets. This includes, but is not necessarily limited to:
        * NAVIGATION:   Controls used for navigating the script's interface.
                        These controls should be capable of displaying complex
                        detail for effective navigation.
        * PARAMETER_1:  Mapped to (generally linear) parameters for FL Studio 
                        windows and plugins.
        * PARAMETER_2:  Mapped to (generally rotary) parameters for FL Studio
                        windows and plugins.
        * DRUM_PADS:    Controls used as drum pads. Can be potentially used as
                        drums in FPC, or keyswitches in orchestral plugins.
        These should be set in self._state. Although the same parameter sets can
        be mapped to multiple targets, this can potentially add to clutter,
        especially for the parameter targets.
        """
        self._state = DeviceState()
        
    def getControlSetTargeting(self, target: str) -> ControlSet:
        """Return the ControlSet that maps to a certain FL Studio target

        Args:
            target (str): FL Studio target (use a constant)
        
        # TODO: Change this to an enum?

        Returns:
            ControlSet: Control set
        """

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

    def onUpdate(self) -> None:
        """Called during `onIdle()`. This function is used to trigger
        communication with the MIDI device, usually to set colours for
        LED-equipped `ControlSurface`s, labels for controls with a text label,
        or values for controls that can be automatically moved as the linked
        value changes.
        """
        self._state.onUpdate()
