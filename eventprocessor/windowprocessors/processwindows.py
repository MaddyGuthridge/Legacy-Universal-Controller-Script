"""
eventprocessor > windowprocessors > processwindows.py

From Novation LaunchKey Mk2 Script by Miguel Guthridge.
Available under GNU GPL3 at https://github.com/MiguelGuthridge/Novation-LaunchKey-Mk2-Script
Adapted from v2.0.0

This script forwards events to event processors for FL Studio Windows.

Author: Miguel Guthridge
"""


import config
import internal
import internal.consts

from . import processmixer
from . import processbrowser
from . import processchannelrack
from . import processplaylist

from . import processdefault

def getWindowObject():
    """Returns reference to module associated with a window

    Returns:
        module: active FL Window
    """
    if internal.window.active_fl_window == internal.consts.WINDOW_MIXER:
        return processmixer
    
    elif internal.window.active_fl_window == internal.consts.WINDOW_BROWSER:
        return processbrowser
    
    elif internal.window.active_fl_window == internal.consts.WINDOW_CHANNEL_RACK:
        return processchannelrack

    elif internal.window.active_fl_window == internal.consts.WINDOW_PLAYLIST:
        return processplaylist

    else: return processdefault

def process(command):

    current_window = getWindowObject()
    current_window.process(command)

    return

def activeStart():

    current_window = getWindowObject()
    current_window.activeStart()

    return

def activeEnd():

    current_window = getWindowObject()
    current_window.activeEnd()

    return

def topWindowStart():
    current_window = getWindowObject()
    current_window.topWindowStart()

    return

def topWindowEnd():
    current_window = getWindowObject()
    current_window.topWindowEnd()

    return