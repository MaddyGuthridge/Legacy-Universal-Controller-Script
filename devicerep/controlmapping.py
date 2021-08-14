"""controlmapping.py

Contains class definition for a mapping to a device's control

Author: Miguel Guthridge
"""

from . import ControlSurface

class ControlMapping:
    """Mapping to a control in a device
    """
    def __init__(self, control_type:int, control_index:int) -> None:
        """Create a control mapping object

        Args:
            control_type (int): the type of control
            control_index (int): the index of that control
        """
        self._set = control_type
        self._index = control_index

    def getControlSet(self) -> int:
        """Returns control set associated with the control

        Returns:
            int: set index
        """
        return self._set
    
    def getControlIndex(self) -> int:
        """Returns index of control within control set

        Returns:
            int: index
        """
        return self._index

    def getMappedControl(self, device) -> ControlSurface:
        #return device.getControlSet(self._set).getControl(self._index)
        pass
