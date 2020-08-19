from ..parse import detector
from .. import consts
from .setup import learn
from .import drumpad

import eventconsts

def setLearnFirstFader():
    learn.setCurrent("Tweak", eventconsts.TYPE_FADER, "Master", can_skip=True)

fader_num = -1

def setupFader(command):
    global fader_num
    if command.type == eventconsts.TYPE_UNKNOWN:
        if fader_num == -1:
            detector.addEvent(command.status, command.note, eventconsts.TYPE_FADER, eventconsts.CONTROL_MASTER_FADER)
            command.handle("Register master fader")
        else:
            detector.addEvent(command.status, command.note, eventconsts.TYPE_FADER, fader_num)
            command.handle("Register fader")
        fader_num += 1
        learn.setCurrent("Tweak", eventconsts.TYPE_FADER, fader_num)
        print("If your controller doesn't have this many faders, press the stop button.")
    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP) and command.is_lift:
        command.handle("No more faders")
        # Do fader buttons
        setLearnFirstFaderButton()

def setLearnFirstFaderButton():
    learn.setCurrent("Press", eventconsts.TYPE_FADER_BUTTON, "Master", can_skip=True)

fader_button_num = -1

def setupFaderButton(command):
    global fader_button_num
    if command.type == eventconsts.TYPE_UNKNOWN:
        if fader_button_num == -1:
            detector.addEvent(command.status, command.note, eventconsts.TYPE_FADER_BUTTON, eventconsts.CONTROL_MASTER_FADER_BUTTON)
            command.handle("Register master fader button")
        else:
            detector.addEvent(command.status, command.note, eventconsts.TYPE_FADER_BUTTON, fader_button_num)
            command.handle("Register fader button")
        fader_button_num += 1
        learn.setCurrent("Press", eventconsts.TYPE_FADER_BUTTON, fader_button_num)
        print("If your controller doesn't have this many fader buttons, press the stop button.")
    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP) and command.is_lift:
        command.handle("No more fader buttons")
        # Do knobs
        setLearnFirstKnob()

def setLearnFirstKnob():
    learn.setCurrent("Tweak", eventconsts.TYPE_KNOB, "Master", can_skip=True)

knob_num = -1

def setupKnob(command):
    global knob_num
    if command.type == eventconsts.TYPE_UNKNOWN:
        if knob_num == -1:
            detector.addEvent(command.status, command.note, eventconsts.TYPE_KNOB, eventconsts.CONTROL_MASTER_KNOB)
            command.handle("Register master knob")
        else:
            detector.addEvent(command.status, command.note, eventconsts.TYPE_KNOB, knob_num)
            command.handle("Register knob")
        knob_num += 1
        learn.setCurrent("Tweak", eventconsts.TYPE_KNOB, knob_num)
        print("If your controller doesn't have this many knobs, press the stop button.")
    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP) and command.is_lift:
        command.handle("No more knobs")
        drumpad.setLearnFirstDrumPad()
