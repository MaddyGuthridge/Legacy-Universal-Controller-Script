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
    
    def setCurrent(self, action, new_type, new_control, control_type="", can_skip=False):
        self.current = (new_type, new_control)
        print("")
        if type(new_control) is int:
            new_control = helpers.getNumSuffix(new_control + 1)
        print(action, "the", new_control, new_type, control_type)
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

    initState.setVal(consts.INIT_SETUP)

    if initState == consts.INIT_SETUP:
        learn.setCurrent("Press", eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP, "button")


def processSetup(command):
    command.addProcessor("Setup processor")
    if learn[0] == eventconsts.TYPE_TRANSPORT:
        transport.setupTransport(command)
    elif learn[0] == eventconsts.TYPE_FADER:
        fader.setupFader(command)
    elif learn[0] == eventconsts.TYPE_FADER_BUTTON:
        fader.setupFaderButton(command)
    elif learn[0] == eventconsts.TYPE_KNOB:
        fader.setupKnob(command)
    elif learn[0] == eventconsts.TYPE_DRUM_PAD:
        drumpad.setupDrums(command)
    
    command.refreshId()
    
    if not command.handled:
        command.handle("Setup catch-all")



from . import transport, fader, drumpad

