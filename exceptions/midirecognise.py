"""midirecognise.py

Contains definition for MidiRecogniseException

Author: Miguel Guthridge
"""

class MidiRecogniseException(ValueError):
    """Midi event doesn't map to any known controls for device
    """
