"""
internal > parse.py

This file contains the object which maps events to control types and allow for the detection of events.
"""

class EventDetector:
    transport_controls = dict()
    fader_controls = dict()
    fader_button_controls = dict()
    knob_controls = dict()
    coord_controls = dict()
    basic_controls = dict()
    
    def recognise(self, status, note):
        id_val = (status, note)
        if id_val in self.transport_controls:
            return "Transport", self.transport_controls[id_val]
        
        elif id_val in self.fader_controls:
            return "Fader", self.fader_controls[id_val]

        elif id_val in self.fader_button_controls:
            return "Fader Button", self.fader_button_controls[id_val]
        
        elif id_val in self.knob_controls:
            return "Knob", self.knob_controls[id_val]
        
        elif id_val in self.coord_controls:
            return "Coord", self.fader_controls[id_val]
        
        elif id_val in self.basic_controls:
            return "Basic", self.basic_controls[id_val]

        else:
            return "Unrecognised", "Null"
    
    def addEvent(self, status, note, event_type, control):
        id_val = (status, note)
        if event_type == "Transport":
            self.transport_controls[id_val] = control
        
        elif event_type == "Fader":
            self.fader_controls[id_val] = control
        
        elif event_type == "Fader Button":
            self.fader_button_controls[id_val] = control
        
        elif event_type == "Knob":
            self.knob_controls[id_val] = control
        
        elif event_type == "Coord":
            self.coord_controls[id_val] = control
        
        elif event_type == "Basic":
            self.basic_controls[id_val] = control


detector = EventDetector()

class ParsedEvent:
    
    def __init__(self, event):
        self.status = event.status
        self.note = event.data1
        self.value = event.data2
        
        self.type, self.control = detector.recognise(self.status, self.note)
    
    



