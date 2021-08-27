"""module controlsurfaces

Contains definitions for generic control surfaces

Author: Miguel Guthridge
"""

from .controlsurface import ControlSurface

from .note import Note, NoteOn, NoteOff

from .knob import Knob
from .fader import Fader
from .button import Button, FaderButton, SoloButton, MuteButton
from .drumpad import DrumPad
from .transport_buttons import TransportButton, PlayPauseButton, StopButton, \
    JogButton, FastForwardButton, RewindButton, LoopButton, RecordButton, \
    TrackButton, NextTrackButton, PrevTrackButton
