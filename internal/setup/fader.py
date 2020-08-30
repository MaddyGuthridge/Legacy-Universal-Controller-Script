"""
internal > setup > fader.py

Allows for the setup of faders

Author: Miguel Guthridge
"""

from ..parse import detector
from .. import consts
from .setup import learn
from .import drumpad

import helpers
import eventconsts

def setLearnFirstFader():
    learn.setCurrent(eventconsts.TYPE_FADER, eventconsts.CONTROL_MASTER_FADER, "Tweak the fader to use as the master fader", can_skip=True)

fader_num = -1

def setupFader(command):
    global fader_num
    if command.type == eventconsts.TYPE_UNKNOWN:
        if fader_num == -1:
            detector.addEvent(command.status, command.note, command.value, eventconsts.TYPE_FADER, eventconsts.CONTROL_MASTER_FADER)
            command.handle("Register master fader")
        else:
            detector.addEvent(command.status, command.note, command.value, eventconsts.TYPE_FADER, fader_num)
            command.handle("Register fader")
        fader_num += 1
        learn.setCurrent(eventconsts.TYPE_FADER, fader_num, ("Tweak the " + helpers.getNumSuffix(fader_num + 1) + " fader"))
        print("If your controller doesn't have this many faders, press the stop button.")
    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP) and command.is_lift:
        command.handle("No more faders")
        checkFaderButtonType()

has_solo_buttons = False

def checkFaderButtonType():
    learn.setCurrent(eventconsts.TYPE_FADER_BUTTON, -2, "If your controller has seperate solo and mute buttons, press the play button. Otherwise, press the stop button.")

def processCheckFaderButtons(command):
    if command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP) and command.is_lift:
        # Do fader buttons
        setLearnFirstFaderButton()
        
    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_PLAY) and command.is_lift:
        global has_solo_buttons
        has_solo_buttons = True
        # Do fader buttons
        setLearnFirstFaderButton()

def setLearnFirstFaderButton():
    mute_fader = "mute" * has_solo_buttons + "fader" * (not has_solo_buttons)
    learn.setCurrent(eventconsts.TYPE_FADER_BUTTON, eventconsts.CONTROL_MASTER_FADER_BUTTON, "Press the button to use as the master " + mute_fader + " button", can_skip=True)

fader_button_num = -1

def setupFaderButton(command):
    mute_fader = "mute" * has_solo_buttons + "fader" * (not has_solo_buttons)
    if learn.current[1] == -2:
        processCheckFaderButtons(command)
        return
    global fader_button_num
    if command.type == eventconsts.TYPE_UNKNOWN:
        if fader_button_num == -1:
            detector.addEvent(command.status, command.note, command.value, eventconsts.TYPE_FADER_BUTTON, eventconsts.CONTROL_MASTER_FADER_BUTTON)
            command.handle("Register master " + mute_fader + " button")
        else:
            detector.addEvent(command.status, command.note, command.value, eventconsts.TYPE_FADER_BUTTON, fader_button_num)
            command.handle("Register " + mute_fader + " button")
        fader_button_num += 1
        learn.setCurrent(eventconsts.TYPE_FADER_BUTTON, fader_button_num, ("Press the " + helpers.getNumSuffix(fader_button_num + 1) + " " + mute_fader + " button"))
        print("If your controller doesn't have this many " + mute_fader + " buttons, press the stop button.")
    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP) and command.is_lift:
        command.handle("No more " + mute_fader + " buttons")
        if has_solo_buttons:
            # Do solo buttons
            setLearnFirstSoloButton()
        else:
            # Do knobs
            setLearnFirstKnob()
        
def setLearnFirstSoloButton():
    learn.setCurrent(eventconsts.TYPE_SOLO_BUTTON, eventconsts.CONTROL_MASTER_SOLO_BUTTON, "Press the button to use as the master solo button", can_skip=True)

solo_button_num = -1

def setupSoloButton(command):
    global solo_button_num
    if command.type == eventconsts.TYPE_UNKNOWN:
        if solo_button_num == -1:
            detector.addEvent(command.status, command.note, command.value, eventconsts.TYPE_SOLO_BUTTON, eventconsts.CONTROL_MASTER_SOLO_BUTTON)
            command.handle("Register master solo button")
        else:
            detector.addEvent(command.status, command.note, command.value, eventconsts.TYPE_SOLO_BUTTON, solo_button_num)
            command.handle("Register solo button")
        solo_button_num += 1
        learn.setCurrent(eventconsts.TYPE_SOLO_BUTTON, solo_button_num, ("Press the " + helpers.getNumSuffix(solo_button_num + 1) + " solo button"))
        print("If your controller doesn't have this many solo buttons, press the stop button.")
    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP) and command.is_lift:
        command.handle("No more solo buttons")
        # Do knobs
        setLearnFirstKnob()

def setLearnFirstKnob():
    learn.setCurrent(eventconsts.TYPE_KNOB, eventconsts.CONTROL_MASTER_KNOB, "Tweak the knob to use as the master knob", can_skip=True)

knob_num = -1

def setupKnob(command):
    global knob_num
    if command.type == eventconsts.TYPE_UNKNOWN:
        if knob_num == -1:
            detector.addEvent(command.status, command.note, command.value, eventconsts.TYPE_KNOB, eventconsts.CONTROL_MASTER_KNOB)
            command.handle("Register master knob")
        else:
            detector.addEvent(command.status, command.note, command.value, eventconsts.TYPE_KNOB, knob_num)
            command.handle("Register knob")
        knob_num += 1
        learn.setCurrent(eventconsts.TYPE_KNOB, fader_num, ("Tweak the " + helpers.getNumSuffix(knob_num + 1) + " knob"))
        print("If your controller doesn't have this many knobs, press the stop button.")
    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP) and command.is_lift:
        command.handle("No more knobs")
        drumpad.setLearnFirstDrumPad()
