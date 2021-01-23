"""
internal > setup.py

This script helps with initialising the script, and setting up the event detector object.

Author: Miguel Guthridge
"""

import ui

from .. import consts

import helpers
import eventconsts
import deviceconfig

import device

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
    
    device_name = device.getName()
    
    print(helpers.getLineBreak())
    print(consts.SCRIPT_NAME)
    print("By " + consts.SCRIPT_AUTHOR)
    print(helpers.getLineBreak())
    print("Version " + str(consts.SCRIPT_VERSION_MAJOR) + "." + str(consts.SCRIPT_VERSION_MINOR) + "." + str(consts.SCRIPT_VERSION_REVISION)
          + " " + consts.SCRIPT_VERSION_SUFFIX)
    print(helpers.getLineBreak())
    print("Running on \"" + device_name + "\"")
    print(helpers.getLineBreak())
    print(helpers.getLineBreak())
    print("")
    
    # Send universal device enquiry
    device.midiOutSysex(consts.DEVICE_ENQUIRY_MESSAGE)
    

def processInitMessage(command):
    # Recieves a universal device query response
    
    # If command isn't response to device enquiry
    if not command.type is eventconsts.TYPE_SYSEX:
        return
    
    device_name = command.sysex[5 : -5].hex()
    
    # Import the configuration for the controller
    result = deviceconfig.loadSetup(device_name)
    
    if result == 0:
        print("An autoinit file could not be found for your device")
        print("Beginning manual setup")
        initState.setVal(consts.INIT_SETUP)
    
    elif result == -1:
        print("A compatible configuration was found but an error occurred while importing it")
        initState.setVal(consts.INIT_FAIL)
    
    else:
        if result == 1:
            print("Device properties imported successfully")
        if result == 2:
            print("Device properties loaded from global configuration")
        initState.setVal(consts.INIT_SUCCESS)
    
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
    elif learn[0] == eventconsts.TYPE_SOLO_BUTTON:
        fader.setupSoloButton(command)
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

def idleSetup():
    # Set hint message before setup begins
    if learn[0] is eventconsts.TYPE_TRANSPORT and learn[1] is eventconsts.CONTROL_STOP:
        ui.setHintMsg("Navigate to \"View > Script output\" to set up your controller")

from . import transport, jog, fader, drumpad

from ..parse import detector
