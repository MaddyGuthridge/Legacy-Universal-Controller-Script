"""
eventconsts.py

Contains constants for identifying events.

Author: Miguel Guthridge
"""
#####################################

TYPE_UNKNOWN  = "Unknown"

#####################################
TYPE_TRANSPORT = "Transport"

CONTROL_STOP = "Stop"
CONTROL_PLAY = "Play"
CONTROL_REC = "Record"
CONTROL_LOOP = "Loop"
CONTROL_SKIP_FORWARD = "Skip Forward"
CONTROL_SKIP_BACK = "Skip Back"
CONTROL_NEXT = "Next"
CONTROL_PREV = "Previous"

#####################################
TYPE_JOG = "Jog"

CONTROL_JOG_FORWARD = "Forward"
CONTROL_JOG_BACKWARD = "Backward"
CONTROL_JOG_PUSH = "Push"
CONTROL_JOG_PULL = "Pull"

#####################################
TYPE_FADER = "Fader"

CONTROL_MASTER_FADER = -1

#####################################
# Mute button only when solo button available
TYPE_FADER_BUTTON = "Fader Button"

CONTROL_MASTER_FADER_BUTTON = -1

#####################################
TYPE_SOLO_BUTTON = "Solo button"

CONTROL_MASTER_SOLO_BUTTON = -1

#####################################
TYPE_KNOB = "Knob"

CONTROL_MASTER_KNOB = -1

#####################################
TYPE_DRUM_PAD = "Drum Pad"

#####################################
TYPE_BASIC = "Basic"
