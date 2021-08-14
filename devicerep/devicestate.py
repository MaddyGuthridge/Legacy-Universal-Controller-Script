"""devicestate.py

Contains class representing the state of a device. Contains the list of
control sets, which themselves contain controls.

Author: Miguel Guthridge
"""

from . import ControlMapping, ControlSurface, ControlValue, ControlSet
from exceptions import MidiRecogniseException

class DeviceState:
    """Represents the current state of a controller.
    
    WARNING: DO NOT INHERIT FROM THIS CLASS. Instead create a wrapper class
    derived from DeviceObject that adds properties to an instance of this class.
    That way, the management of device controls can be abstracted away, and can
    be improved upon without breaking derived device implementations.
    """
    
    def __init__(self) -> None:
        """Creates a new, empty instance of a DeviceState object. This is
        contained within a DeviceObject, which initialises it with
        ControlSurfaces in its __init__() function.
        
        ControlSurfaces should be added to the device using the methods
        * addControlSet(name: str)
        * addControl(set: int, control: ControlSurface)
        """
        self._control_sets = []
    
    def addControlSet(self, name: str) -> int:
        """Add a control set to the device. This is used to group controls into
        logical sets (eg faders, drum pads etc)

        Args:
            name (str): name of the new control set

        Returns:
            int: control set index
        """
        index = len(self._control_sets)
        self._control_sets.append(ControlSet(name, index))
        return index
    
    def addControl(self, set: int, control: ControlSurface) -> ControlMapping:
        """Adds a control to a control set

        Args:
            set (int): set ID
            control (ControlSurface): control to add

        Returns:
            ControlMapping: mapping where the control was inserted
        """
        return self._control_sets[set].addControl(control)

    def recognise(self, event) -> ControlValue:
        """Recognise an event and return its ControlValue mapping

        Args:
            event (FlEvent): Event to recognise

        Returns:
            ControlValue: Mapping
        
        Raises:
            MidiRecogniseException: Event not recognised
        """
        for set in self._control_sets:
            res = set.recognise(event)
            if res is not None:
                return res
        
        # No matches: raise exception
        raise MidiRecogniseException("Event not recognised")
