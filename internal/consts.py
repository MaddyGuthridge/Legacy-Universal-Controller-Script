"""
internal > consts.py

Contains constants relevant to the internal state of the controller

Author: Miguel Guthridge
"""

import midi

# Script info
################################

SCRIPT_NAME = "Universal Controller Script"
SCRIPT_AUTHOR = "Miguel Guthridge"
SCRIPT_ADDRESS = "https://github.com/MiguelGuthridge/Universal-Controller-Script"

SCRIPT_VERSION_MAJOR = 0
SCRIPT_VERSION_MINOR = 4
SCRIPT_VERSION_REVISION = 0
SCRIPT_VERSION_SUFFIX = "Beta"

MIN_FL_SCRIPT_VERSION = 7

# Help URLs
################################
HELP_URL_AUTOINIT = "https://github.com/MiguelGuthridge/Universal-Controller-Script/wiki/Autoinit-Scripts"

# Init states
################################

INIT_INCOMPLETE = "Incomplete"
INIT_SUCCESS = "Success"
INIT_SETUP = "Setup"
INIT_FAIL = "Fail"

# Timeout for no device response
INIT_TIMEOUT = 50

# MIDI Messages
################################

DEVICE_INQUIRY_MESSAGE = bytes([0xF0, 0x7E, 0x7F, 0x06, 0x01, 0xF7])

# Window constants
################################

WINDOW_PLAYLIST = midi.widPlaylist
WINDOW_PIANO_ROLL = midi.widPianoRoll
WINDOW_CHANNEL_RACK = midi.widChannelRack
WINDOW_MIXER = midi.widMixer
WINDOW_BROWSER = midi.widBrowser

WINDOW_STR_SCRIPT_OUTPUT = "Script output"
WINDOW_STR_COLOUR_PICKER = "Color selector"
FL_WINDOW_LIST = ["Mixer", "Channel rack", "Playlist", "Piano roll", "Browser"]


# Snapping constants
################################

# Mixer snap values
MIXER_VOLUME_SNAP_TO = 0.8 # Snap mixer track volumes to 100%
MIXER_PAN_SNAP_TO = 0.0 # Snap mixer track pannings to Centred
MIXER_STEREO_SEP_SNAP_TO = 0.0 # Snap mixer track stereo separation to Original

# Channel rack snap values
CHANNEL_VOLUME_SNAP_TO = 0.78125 # Snap channel volumes to ~= 78% (FL Default)
CHANNEL_PAN_SNAP_TO = 0.0 # Snap channel pans to Centred


# Debug level constants
################################
class DEBUG:
    ERROR = "Errors"
    PROCESSOR_PERFORMANCE = "Processor performance"
    LIGHTING_RESET = "Lighting reset"
    LIGHTING_MESSAGE = "Lighting message"
    DISPATCH_EVENT = "Dispatch event"
    IDLE_PERFORMANCE = "Idle Performance"
    ANIMATION_IDLE_TIMERS = "Timers"
    EVENT_DATA = "Event data"
    EVENT_ACTIONS = "Event actions"
    WINDOW_CHANGES = "Window changed"
    WARNING_DEPRECIATED_FEATURE = "Depreciated feature"
    DEVICE_TYPE = "Device type"
    NOTE_MODE = "Note mode"
    SHIFT_EVENTS = "Shift events"

FORCE_DEBUG_MODES_LIST = [DEBUG.ERROR, DEBUG.EVENT_DATA, DEBUG.EVENT_ACTIONS, DEBUG.WINDOW_CHANGES, DEBUG.WARNING_DEPRECIATED_FEATURE, DEBUG.NOTE_MODE]



LOG_TAB_LENGTH = 16
