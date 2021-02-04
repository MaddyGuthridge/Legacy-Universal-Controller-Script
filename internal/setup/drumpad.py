"""
internal > setup > drumpad.py

Allows for the setup of drumpads

Author: Miguel Guthridge
"""

from ..parse import detector
from .. import consts
from .setup import learn, initState

import eventconsts
import helpers

def setLearnFirstDrumPad():
    learn.setCurrent(eventconsts.TYPE_DRUM_PAD, (x_coord, y_coord), 
                     "Press the top left (" + str(x_coord+1) + ", " + str(y_coord+1) + ") drum pad. Drum pads should be entered from left to right, then top to bottom.", 
                     can_skip=True)

x_coord = 0
y_coord = 0

def setupDrums(command):
    global x_coord, y_coord
    if command.type == eventconsts.TYPE_UNKNOWN and command.is_lift:
        command.handle("Register drum pad")
        detector.addEvent(command.status, command.note, command.value, eventconsts.TYPE_DRUM_PAD, (x_coord, y_coord))
        x_coord += 1
        learn.setCurrent(eventconsts.TYPE_DRUM_PAD, (x_coord, y_coord), "Press the (" + str(x_coord+1) + ", " + str(y_coord+1) + ") drum pad")
        print("If that was the last drum pad in this row, press the stop button.")
    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP) and command.is_lift:
        if x_coord == 0:
            command.handle("Last drum pad")
            learn.current = (consts.INIT_SUCCESS, consts.INIT_SUCCESS)
            print("")
            print(helpers.getLineBreak())
            print("The initialisation is now complete!")
            print("If you want to make a file to automate the initialisation, press the play button.")
            print("If you don't, press the stop button.")
            return
        command.handle("End of drum pad row")
        x_coord = 0
        y_coord += 1
        learn.setCurrent(eventconsts.TYPE_DRUM_PAD, (x_coord, y_coord), "Press the (" + str(x_coord+1) + ", " + str(y_coord+1) + ") drum pad")
        print("If that was the last row, press the stop button again.")
        

