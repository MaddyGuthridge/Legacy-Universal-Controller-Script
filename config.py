"""
config.py

Contains configuration options for the script.
"""

import eventconsts
from internal.consts import DEBUG

#-------------------------------
# USER VARIABLES
#-------------------------------

# Check for updates online. Change to False if you don't want to be notified or something
CHECK_UPDATES = True
# THIS DOESN'T WORK YET :(



LONG_PRESS_TIME = 0.5 # Change how long a long press needs to be held for
DOUBLE_PRESS_TIME = 0.2 # Change how quickly a double press needs to be done to be detected

ENABLE_SNAPPING = True # Change to False to prevent faders and knobs from snapping to default values
SNAP_RANGE = 0.05 # Will snap if within this disatnce of snap value

# If enabled, double pressing shift key keeps the shift button enabled until it is used, or pressed again.
ENABLE_SUSTAINED_SHIFT = True
# If enabled, sustained shifts will automatically lift when you press a button.
AUTOCANCEL_SUSTAINED_SHIFT = False

# Determines the navigation speed using the pitch bend wheel in the shift menu
PITCH_BEND_JOG_SPEED = 0.05

# Controls which console messages are printed. Add things from the DEBUG object
CONSOLE_DEBUG_MODE = [DEBUG.EVENT_DATA]

