"""
internal > setup.py

This script helps with initialising the script, and setting up the event detector object.

Author: Miguel Guthridge
"""

from .. import consts
from ..parse import detector

import helpers
import eventconsts

class InitState:
    state = consts.INIT_INCOMPLETE

    def getVal(self):
        return self.state
    
    def setVal(self, new_val):
        if self.state == consts.INIT_SETUP and new_val == consts.INIT_SUCCESS:
            print("")
            print("Setup complete!")
            print("")
        self.state = new_val

    def __eq__(self, other):
        return self.state == other
    
initState = InitState()

class Learner:
    current = [0, 0]
    
    def setCurrent(self, new_type, new_control, message, can_skip=False):
        self.current = (new_type, new_control)
        print("")
        print(message)
        if can_skip:
            print("If your controller doesn't have this, press the stop button")
    
    def __getitem__(self, key):
        return self.current[key]

learn = Learner()

def initialise():
    print(helpers.getLineBreak())
    print(consts.SCRIPT_NAME)
    print("By " + consts.SCRIPT_AUTHOR)
    print(helpers.getLineBreak())
    print("Version " + str(consts.SCRIPT_VERSION_MAJOR) + "." + str(consts.SCRIPT_VERSION_MINOR) + str(consts.SCRIPT_VERSION_REVISION) 
          + " " + consts.SCRIPT_VERSION_SUFFIX)
    print(helpers.getLineBreak())
    print(helpers.getLineBreak())
    print("")
    
    # For the moment just initialise the script to setup mode.
    # Eventually we'll try to read a configuration file to load the state of the script

    try:
        __import__("autoinit")
        initState.setVal(consts.INIT_SUCCESS)
    except:
        initState.setVal(consts.INIT_SETUP)

    if initState == consts.INIT_SETUP:
        learn.setCurrent(eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP, "Press the stop button")


def processSetup(command):
    command.addProcessor("Setup processor")
    if learn[0] == eventconsts.TYPE_TRANSPORT:
        transport.setupTransport(command)
    elif learn[0] == eventconsts.TYPE_JOG:
        jog.setupJog(command)
    elif learn[0] == eventconsts.TYPE_FADER:
        fader.setupFader(command)
    elif learn[0] == eventconsts.TYPE_FADER_BUTTON:
        fader.setupFaderButton(command)
    elif learn[0] == eventconsts.TYPE_KNOB:
        fader.setupKnob(command)
    elif learn[0] == eventconsts.TYPE_DRUM_PAD:
        drumpad.setupDrums(command)
    elif learn[0] == consts.INIT_SUCCESS:
        offerPrintout(command)
    
    command.refreshId()
    
    if not command.handled:
        command.handle("Setup catch-all")

def offerPrintout(command):
    if command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_PLAY) and command.is_lift:
        detector.dumpAutoinitScript()
        initState.setVal(consts.INIT_SUCCESS)
        command.handle("Dump autoinit script, finished initialisation")
    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP) and command.is_lift:
        command.handle("Finished initialisation")
        initState.setVal(consts.INIT_SUCCESS)

from . import transport, jog, fader, drumpad

