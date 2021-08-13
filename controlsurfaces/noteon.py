"""noteon.py

Note On Event

Author: Miguel Guthridge
"""

from devicerep import ControlSurface, ControlValue

class NoteOn(ControlSurface):
    """Note-on event
    """
    def __init__(self, note_num: int, channel:int = 0):
        """Create a note-on event

        Args:
            note_num (int): note to recognise
            channel (int, optional): channel to recognise (defaults to 0,
                           accepts 0-15)
        """
        super().__init__()
        
        if not (0 <= channel <= 0xF):
            raise ValueError("Invalid MIDI channel")
        
        self._note_num = note_num
        self._event_status = 0x90 + channel
    
    def recognise(self, event) -> 'ControlValue':
        """Recognise a NoteOn event
        """
        
        # Check for non-notes
        if (
            event.status != self._event_status
         or event.data1  != self._note_num
         or event.data2  == 0       # Zero velocity means note off
        ):
            return None
        
        # Recognised NoteOn event
        return ControlValue(self._mapping, event.data2)
