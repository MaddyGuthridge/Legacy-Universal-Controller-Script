"""
internal > setup.py

This script helps with initialising the script, and setting up the event detector object.

Author: Miguel Guthridge
"""

from . import consts
from .parse import detector

import helpers
import eventconsts

class InitState:
    state = consts.INIT_INCOMPLETE

    def getVal(self):
        return self.state
    
    def setVal(self, new_val):
        self.state = new_val

    def __eq__(self, other):
        return self.state == other
    
initState = InitState()

SETUP_CURRENT_LEARN = ""

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
        setSetupLearn(eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP, "Press the stop button")

def setSetupLearn(new_type, new_control, message=""):
    global SETUP_CURRENT_LEARN
    
    SETUP_CURRENT_LEARN = (new_type, new_control)
    print(message)

def processSetup(command):
    if SETUP_CURRENT_LEARN[0] == eventconsts.TYPE_TRANSPORT:
        setupTransport(command)
    
    
def setupTransport(command):
    if command.is_lift:
        if SETUP_CURRENT_LEARN[1] == eventconsts.CONTROL_STOP:
            setupStop(command)
        elif SETUP_CURRENT_LEARN[1] == eventconsts.CONTROL_PLAY:
            setupPlay(command)
    
    
def setupStop(command):
    detector.addEvent(command.status, command.note, eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP)
    
    setSetupLearn(eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_PLAY, "Press the play button")

def setupPlay(command):
    if command.type == eventconsts.TYPE_UNKNOWN:
        detector.addEvent(command.status, command.note, eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_PLAY)

