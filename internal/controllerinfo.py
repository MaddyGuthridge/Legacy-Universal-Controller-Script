"""
internal > controllerinfo.py

Provides functions to get information about features available on the controller.

Author: Miguel Guthridge
"""

import eventconsts
from .parse import detector

def hasRecord():
    return detector.checkKey(eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_REC)

def hasLoop():
    return detector.checkKey(eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_LOOP)

def hasRewindFastForward():
    return detector.checkKey(eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_SKIP_BACK)

def hasTrackNextPrev():
    return detector.checkKey(eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_NEXT)

def hasJogWheel():
    return detector.checkKey(eventconsts.TYPE_JOG, eventconsts.CONTROL_JOG_BACKWARD)

def hasJogWheel3D():
    return detector.checkKey(eventconsts.TYPE_JOG, eventconsts.CONTROL_JOG_PUSH)

def hasJogWheel4D():
    return detector.checkKey(eventconsts.TYPE_JOG, eventconsts.CONTROL_JOG_PULL)

def hasFaders():
    return detector.checkKey(eventconsts.TYPE_FADER, eventconsts.CONTROL_MASTER_FADER)

def numFaders():
    """Returns the number of faders (excluding the master fader)

    Returns:
        int: number of non-master faders
    """
    return len(detector.fader_controls) - 1

def hasFaderButtons():
    return detector.checkKey(eventconsts.TYPE_FADER_BUTTON, eventconsts.CONTROL_MASTER_FADER_BUTTON)

def numFaderButtons():
    """Returns the number of fader buttons (excluding the master fader button)

    Returns:
        int: number of non-master fader buttons
    """
    return len(detector.fader_button_controls) - 1

def hasSeperateSoloButtons():
    return detector.checkKey(eventconsts.TYPE_SOLO_BUTTON, eventconsts.CONTROL_MASTER_SOLO_BUTTON)

def numSoloButtons():
    """Returns the number of solo buttons (excluding the master solo button)

    Returns:
        int: number of non-master solo buttons
    """
    return len(detector.solo_button_controls) - 1

def hasKnobs():
    return detector.checkKey(eventconsts.TYPE_KNOB, eventconsts.CONTROL_MASTER_KNOB)

def numKnobs():
    """Returns the number of knobs (excluding the master knob)

    Returns:
        int: number of non-master knobs
    """
    return len(detector.knob_controls) - 1

def hasDrumPads():
    return len(detector.drum_pad_controls) != 0
