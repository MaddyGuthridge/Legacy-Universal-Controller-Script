
from internal import consts
from internal.parse import detector
import processorhelpers
import config

class ParsedEvent:
    
    def __init__(self, event):
        self.status = event.status
        self.note = event.data1
        self.value = event.data2
        
        self.handled = False
        
        self.is_lift = not self.value
        
        self.refreshId()
        
        self.actions = processorhelpers.ActionPrinter()

    def __str__(self):
        
        ret = ""
        if consts.DEBUG.EVENT_DATA in config.CONSOLE_DEBUG_MODE:
            ret +=  "Event: " + self.type + " " + str(self.control) + " (" + str(self.status) + " " + str(self.note) + " " + str(self.value) + ")"
        if consts.DEBUG.EVENT_ACTIONS in config.CONSOLE_DEBUG_MODE:
            ret += '\n' + self.actions.flush()
        
        return ret

    def getId(self):
        return (self.type, self.control)
    
    def refreshId(self):
        self.type, self.control = detector.recognise(self.status, self.note)
        
    def handle(self, action, silent=False):
        self.handled = True
        self.actions.appendAction(action, silent, True)
        
    def act(self, action, silent=True):
        self.actions.appendAction(action, silent, False)
    
    def addProcessor(self, name):
        self.actions.addProcessor(name)

