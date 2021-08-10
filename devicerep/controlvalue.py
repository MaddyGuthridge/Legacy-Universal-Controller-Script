"""controlvalue.py

Contains class definition for a value mapped to a control
This class can be overridden to allow for mappings for compelx controls such as
jog wheels, although it should always provide a getValue() method to allow for
correct integration with plugins.

Author: Miguel Guthridge
"""

class ControlValue:
    """Value mapped to a control
    """
    def __init__(self, mapping: ControlMapping, value: int) -> None:
        self._mapping = mapping
        self._value = value
    
    def getMapping(self) -> ControlMapping:
        """Get the mapping that this value is associated with

        Returns:
            ControlMapping: mapping
        """
        return self._mapping
    
    def getValue(self) -> int:
        """Get the value

        Returns:
            int: value
        """
        return self._value
