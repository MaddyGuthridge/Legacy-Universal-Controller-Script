from ..parse import detector
from .. import consts
from .setup import learn, initState

import eventconsts

def setLearnFirstDrumPad():
    learn.setCurrent("Press", eventconsts.TYPE_DRUM_PAD, (x_coord, y_coord), can_skip=True)

x_coord = 0
y_coord = 0

def setupDrums(command):
    global x_coord, y_coord
    if command.type == eventconsts.TYPE_UNKNOWN and command.is_lift:
        detector.addEvent(command.status, command.note, eventconsts.TYPE_DRUM_PAD, (x_coord, y_coord))
        x_coord += 1
        learn.setCurrent("Press", eventconsts.TYPE_DRUM_PAD, (x_coord, y_coord))
        print("If that was the last drum pad in this row, press the skip back button.")
    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_SKIP_BACK) and command.is_lift:
        x_coord = 0
        y_coord += 1
        learn.setCurrent("Press", eventconsts.TYPE_DRUM_PAD, (x_coord, y_coord))
        print("If that was the last row, press the stop button.")
    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP) and command.is_lift:
        initState.setVal(consts.INIT_SUCCESS)