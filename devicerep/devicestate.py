"""devicestate.py

Contains class representing the state of a device. Contains the list of
control sets, which themselves contain controls.

Author: Miguel Guthridge
"""

from . import ControlMapping, ControlValue, ControlSet
from exceptions import MidiRecogniseException
from controlsurfaces import ControlSurface

class DeviceState:
    """Represents the current state of a controller.
    
    WARNING: DO NOT INHERIT FROM THIS CLASS. Instead create a wrapper class
    derived from `DeviceObject` that adds properties to an instance of this
    class. That way, the management of device controls can be abstracted away,
    and can be improved upon without breaking derived device implementations.
    """
    
    def __init__(self) -> None:
        """Creates a new, empty instance of a `DeviceState` object. This is
        contained within a `DeviceObject`, which initialises it with
        `ControlSurfaces` in its `__init__()` function.
        
        ControlSurfaces should be added to the device using the methods
        * `addControlSet(name: str)`
        * `addControl(set: int, control: ControlSurface)`
        """
        self._control_sets = []
        
        self._set_targets = dict()
    
    def addControlSet(self, name: str) -> int:
        """Add a `ControlSet` to the device. This is used to group controls into
        logical sets (eg faders, drum pads etc)

        Args:
            name (str): name of the new control set

        Returns:
            int: control set index
        """
        index = len(self._control_sets)
        self._control_sets.append(ControlSet(name, index))
        return index
    
    def addCustomControlSet(self, control_set: ControlSet) -> int:
        """Add a custom `ControlSet` to the device. This variant of
        `addControlSet()` is used to add control set types that aren't the
        standard `ControlSet` class. This allows more fine-grained control over
        the behaviour of the device.

        Args:
            control_set (ControlSet): Control set to add

        Returns:
            int: Index of the control set
        """
        index = len(self._control_sets)
        control_set.setIndex(index)
        self._control_sets.append(control_set)
        return index
    
    def getControlSet(self, index: int) -> ControlSet:
        """Return the control set at index

        Args:
            index (int): index of control set

        Returns:
            ControlSet: control set at index
        """
        return self._control_sets[index]
    
    def getControlSetTargeting(self, target: str) -> ControlSet:
        """Returns the ControlSet mapped to target

        Args:
            target (str): target for mapping a control to parameters in
                          FL Studio

        Returns:
            ControlSet: pointed at target
        """
        return self._control_sets[self._set_targets[target]]
    
    def addControl(self, set: int, control: ControlSurface) -> ControlMapping:
        """Adds a control to a `ControlSet`

        Args:
            set (int): set ID
            control (ControlSurface): control to add

        Returns:
            ControlMapping: mapping where the control was inserted
        """
        return self._control_sets[set].addControl(control)

    def getControl(self, mapping: ControlMapping) -> ControlSurface:
        """Return a reference to a `ControlSurface`

        Args:
            mapping (ControlMapping): mapping of control

        Returns:
            ControlSurface: control associated with mapping
        """
        return self._control_sets[mapping.getControlSet()].getControl(mapping)

    def setControlTarget(self, index: int, target: str) -> None:
        """Set a ControlSet at index to map to target

        Args:
            index (int): index of ControlSet
            target (str): target in FL Studio
        """
        self._set_targets[target] = index

    def recognise(self, event) -> ControlValue:
        """Recognise an event and return its `ControlValue` mapping

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

    def resetControls(self) -> None:
        """Send a reset command to each `ControlSurface` associated with the
        device
        """
        for set in self._control_sets:
            set.resetControls()

    def onUpdate(self) -> None:
        """Run `onUpdate()` for each `ControlSurface`
        """
        for set in self._control_sets:
            set.onUpdate()
