

from internal.parse import detector

class ParsedEvent:
    
    def __init__(self, event):
        self.status = event.status
        self.note = event.data1
        self.value = event.data2
        
        self.is_lift = not self.value
        
        self.type, self.control = detector.recognise(self.status, self.note)

    def __str__(self):
        return "Event: " + self.type + " " + self.control + " (" + str(self.status) + " " + str(self.note) + " " + str(self.value) + ")"

