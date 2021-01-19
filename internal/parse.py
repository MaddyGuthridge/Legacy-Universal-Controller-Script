"""
internal > parse.py

This file contains the object which maps events to control types and allow for the detection of events.

Author: Miguel Guthridge
"""

import eventconsts
import helpers
import config
from . import consts
import processorhelpers

import device

class EventDetector:
    transport_controls = dict()
    jog_controls = dict()
    fader_controls = dict()
    fader_button_controls = dict()
    solo_button_controls = dict()
    knob_controls = dict()
    drum_pad_controls = dict()
    basic_controls = dict()
    
    drum_pads_num_x = 0
    drum_pads_num_y = 0
    
    def checkKey(self, event_type, control):
        """Checks if a control is available on the controller.

        Args:
            event_type (str): Event type name
            control (key): Control key

        Returns:
            bool: Whether the key exists
        """
        if event_type == eventconsts.TYPE_TRANSPORT:
            return control in self.transport_controls.values()
        
        elif event_type == eventconsts.TYPE_JOG:
            return control in self.jog_controls.values()
        
        elif event_type == eventconsts.TYPE_FADER:
            return control in self.fader_controls.values()
        
        elif event_type == eventconsts.TYPE_FADER_BUTTON:
            return control in self.fader_button_controls.values()
        
        elif event_type == eventconsts.TYPE_SOLO_BUTTON:
            return control in self.solo_button_controls.values()
        
        elif event_type == eventconsts.TYPE_KNOB:
            return control in self.knob_controls.values()
        
        elif event_type == eventconsts.TYPE_DRUM_PAD:
            return control in self.drum_pad_controls.values()
        
        elif event_type == eventconsts.TYPE_BASIC:
            return control in self.basic_controls.values()
    
    def recognise(self, status, note, value):
        id_val = (status, note)
        event_val = (status, note, value)
        channel = status & int('00001111', 2)
        type_val = status >> 4
        if id_val in self.transport_controls:
            return eventconsts.TYPE_TRANSPORT, self.transport_controls[id_val]
        
        elif event_val in self.jog_controls:
            return eventconsts.TYPE_JOG, self.jog_controls[event_val]
        
        elif id_val in self.fader_controls:
            return eventconsts.TYPE_FADER, self.fader_controls[id_val]

        elif id_val in self.fader_button_controls:
            return eventconsts.TYPE_FADER_BUTTON, self.fader_button_controls[id_val]
        
        elif id_val in self.solo_button_controls:
            return eventconsts.TYPE_SOLO_BUTTON, self.solo_button_controls[id_val]
        
        elif id_val in self.knob_controls:
            return eventconsts.TYPE_KNOB, self.knob_controls[id_val]
        
        elif (channel, note) in self.drum_pad_controls:
            # Use only note because drum pads use note events
            return eventconsts.TYPE_DRUM_PAD, self.drum_pad_controls[(channel, note)]
        
        elif id_val in self.basic_controls:
            return eventconsts.TYPE_BASIC, self.basic_controls[id_val]

        elif initState.getVal() == consts.INIT_SUCCESS and type_val == 9:
            return eventconsts.TYPE_BASIC, eventconsts.CONTROL_NOTE_ON
        
        elif initState.getVal() == consts.INIT_SUCCESS and type_val == 8:
            return eventconsts.TYPE_BASIC, eventconsts.CONTROL_NOTE_OFF

        else:
            return eventconsts.TYPE_UNKNOWN, "Null"
    
    def addEvent(self, status, note, value, event_type, control):
        id_val = (status, note)
        event_val = (status, note, value)
        channel = status & int('00001111', 2)
        if event_type == eventconsts.TYPE_TRANSPORT:
            self.transport_controls[id_val] = control
        
        elif event_type == eventconsts.TYPE_JOG:
            self.jog_controls[event_val] = control
        
        elif event_type == eventconsts.TYPE_FADER:
            self.fader_controls[id_val] = control
        
        elif event_type == eventconsts.TYPE_FADER_BUTTON:
            self.fader_button_controls[id_val] = control
        
        elif event_type == eventconsts.TYPE_SOLO_BUTTON:
            self.solo_button_controls[id_val] = control
        
        elif event_type == eventconsts.TYPE_KNOB:
            self.knob_controls[id_val] = control
        
        elif event_type == eventconsts.TYPE_DRUM_PAD:
            # Use only note because drum pads use note events
            self.drum_pad_controls[(channel, note)] = control
            if control[0] > self.drum_pads_num_x:
                self.drum_pads_num_x = control[0] + 1
            if control[1] > self.drum_pads_num_y:
                self.drum_pads_num_y = control[1] + 1
        
        elif event_type == eventconsts.TYPE_BASIC:
            self.basic_controls[id_val] = control

    def dumpAutoinitScript(self):
        """Prints python text in order to make an autoinit script
        """
        print(helpers.getLineBreak())
        print("###  AUTOINIT SCRIPT  |  COPY FROM HERE DOWNWARDS  ###")
        print("")
        print("\"\"\"\ndeviceconfig > " + helpers.getModuleName(device.getName()) + " > autoinit.py\n\nThis script is generated by the script.\n")
        print("Author: The fact that this file is computer-generated poses some serious moral questions about who should receive the attribution.\n\"\"\"")
        print("")
        print("from internal.parse import detector")
        print("")
        print("")
        print("# Transport buttons")
        print("")
        for key, value in self.transport_controls.items():
            print("detector.addEvent(" + str(key[0]) + ", " + str(key[1])
                  + ", 0, \"" + eventconsts.TYPE_TRANSPORT + "\", \""
                  + str(value) + "\")"
                )
        print("")
        print("")
        print("# Jog wheel")
        print("")
        for key, value in self.jog_controls.items():
            print("detector.addEvent(" + str(key[0]) + ", " + str(key[1])
                  + ", " + str(key[2]) + ", \"" + eventconsts.TYPE_JOG + "\", \""
                  + str(value) + "\")"
                )
        print("")
        print("")
        print("# Faders")
        print("")
        for key, value in self.fader_controls.items():
            print("detector.addEvent(" + str(key[0]) + ", " + str(key[1])
                  + ", 0, \"" + eventconsts.TYPE_FADER + "\", "
                  + str(value) + ")"
                )
        print("")
        print("")
        print("# Fader Buttons")
        print("")
        for key, value in self.fader_button_controls.items():
            print("detector.addEvent(" + str(key[0]) + ", " + str(key[1])
                  + ", 0, \"" + eventconsts.TYPE_FADER_BUTTON + "\", "
                  + str(value) + ")"
                )
        print("")
        print("")
        print("# Solo Buttons")
        print("")
        for key, value in self.solo_button_controls.items():
            print("detector.addEvent(" + str(key[0]) + ", " + str(key[1])
                  + ", 0, \"" + eventconsts.TYPE_SOLO_BUTTON + "\", "
                  + str(value) + ")"
                )
        print("")
        print("")
        print("# Knobs")
        print("")
        for key, value in self.knob_controls.items():
            print("detector.addEvent(" + str(key[0]) + ", " + str(key[1])
                  + ", 0, \"" + eventconsts.TYPE_KNOB + "\", "
                  + str(value) + ")"
                )
        print("")
        print("")
        print("# Drum pads")
        print("")
        for key, value in self.drum_pad_controls.items():
            print("detector.addEvent(" + str(key[0]) + ", " + str(key[1])
                  + ", 0, \"" + eventconsts.TYPE_DRUM_PAD + "\", "
                  + str(value) + ")"
                )
        print("")
        print("")
        print("###  AUTOINIT SCRIPT  |  COPY FROM HERE UPWARDS  ###")
        print(helpers.getLineBreak())
        print("")
        print("In order to make your controller initialise automatically,")
        print("copy the above block of text into a blank text file.")
        print("Save the file in the script's directory in the following location:\n")
        print("Folder: deviceconfig > " + helpers.getModuleName(device.getName()))
        print("File: autoinit.py")
        return ""
        
detector = EventDetector()


class ParsedEvent:
    
    def __init__(self, event):
        self.status = event.status
        self.note = event.data1
        self.value = event.data2
        
        self.handled = False
        self.ignored = False
        self.edited = False
        
        self.actions = processorhelpers.ActionPrinter()
        
        self.sysex = event.sysex
        
        # Identify sysex messages manually
        if self.sysex is not None:
            self.type = eventconsts.TYPE_SYSEX
            self.control = ""
            return
        
        self.is_lift = not self.value
        
        self.refreshId()
        
        if self.value:
            self.is_double_click = processorhelpers.isDoubleClickPress(self.getId())
        else:
            self.is_double_click = processorhelpers.isDoubleClickLift(self.getId())
        
        

    def __str__(self):
        
        ret = ""
        if consts.DEBUG.EVENT_DATA in config.CONSOLE_DEBUG_MODE:
            ret +=  helpers.getTab("Event: ") + helpers.getTab(self.type + " ")\
                 + helpers.getTab(str(self.control))\
                      + " (" + str(self.status) + " " + str(self.note) + " " + str(self.value) + ")"
            
        if consts.DEBUG.EVENT_ACTIONS in config.CONSOLE_DEBUG_MODE:
            ret += '\n' + self.actions.flush()
        
        return ret

    def edit(self, event, reason, ignore=True):
        
        self.ignored = ignore
        self.act(reason, True)
        
        self.status = event.status
        self.note = event.data1
        self.value = event.data2
        
        self.is_lift = not self.value
        
        self.edited = True
        
        self.refreshId()

    def getId(self):
        return (self.type, self.control)
    
    def refreshId(self):
        self.type, self.control = detector.recognise(self.status, self.note, self.value)
        
    def handle(self, action, silent=False):
        self.handled = True
        self.ignored = True
        self.actions.appendAction(action, silent, True)
    
    def ignore(self, action, silent=True):
        self.ignored = True
        self.actions.appendAction(action, silent, False)
        
    def act(self, action, silent=True):
        self.actions.appendAction(action, silent, False)
    
    def addProcessor(self, name):
        self.actions.addProcessor(name)


from .setup.setup import initState
