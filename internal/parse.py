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
        id = (status, note)
        if id in self.transport_controls:
            return "Transport", self.transport_controls[id]
        
        elif id in self.fader_controls:
            return "Fader", self.fader_controls[id]

        elif id in self.fader_button_controls:
            return "Fader Button", self.fader_button_controls[id]
        
        elif id in self.knob_controls:
            return "Knob", self.knob_controls[id]
        
        # Turn this one into a for loop since it's 2D
        elif id in self.coord_controls:
            return "Coord", self.fader_controls[id]
        
        elif id in self.basic_controls:
            return "Basic", self.basic_controls[id]


detector = EventDetector()

class ParsedEvent:
    
    def __init__(self, event):
        self.status = event.status
        self.note = event.data1
        self.value = event.data2
        
        
    
    



