"""noteoff.py

Note Off Event

Author: Miguel Guthridge
"""

from devicerep import ControlSurface, ControlValue

class NoteOff(ControlSurface):
    """Note-off event
    """
    def __init__(self, note_num: int, channel:int = 0):
        """Create a note-off event

        Args:
            note_num (int): note to recognise
            channel (int, optional): channel to recognise (defaults to 0,
                           accepts 0-15)
        """
        super().__init__()
        
        if not (0 <= channel <= 0xF):
            raise ValueError("Invalid MIDI channel")

        self._note_num = note_num
        self._event_status = 0x80 + channel
        self._secondary_event_status = 0x90 + channel
    
    def recognise(self, event) -> 'ControlValue':
        """Recognise a NoteOff event
        """
        
        # Check for note-off
        if event.data1  == self._note_num:
            if (
                event.status == self._event_status
                # Note-off can also be zero-velocity note-on
                or (
                    event.status == self._secondary_event_status
                and event.data2 == 0
                )
            ):
                return ControlValue(self._mapping, event.data2)
        
        # Not a note-off
        return None
