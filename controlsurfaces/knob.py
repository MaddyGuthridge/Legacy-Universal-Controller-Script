"""knob.py

Knob control surface

Author: Miguel Guthridge
"""

from devicerep import ControlSurface, ControlValue

class Knob(ControlSurface):
    """Knob control surface
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
