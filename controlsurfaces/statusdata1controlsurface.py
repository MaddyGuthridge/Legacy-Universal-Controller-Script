"""status_data1_control_surface.py

Type definition for events that use status and data1 as identification and
data2 as value

Author: Miguel Guthridge
"""

from devicerep import ControlSurface, ControlValue

class StatusData1ControlSurface(ControlSurface):
    """A generic control that uses status and data for event identification and
    data2 as value
    """
    
    def __init__(self, status: int, data1: int) -> None:
        super().__init__()
        self._status = status
        self._data1 = data1

    def recognise(self, event) -> 'ControlValue':
        if not (event.status == self._status
            and event.data1 == self._data1):
            return None
        else:
            return ControlValue(self._mapping, event.data2)
