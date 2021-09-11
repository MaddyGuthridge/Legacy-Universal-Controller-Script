"""
eventprocessor > processdefault.py

Provides default actions for controllers.

Author: Miguel Guthridge
"""

import transport
import ui
import midi

import eventconsts

def process(command):
    command.addProcessor("Default processor")
    if command.type == eventconsts.TYPE_TRANSPORT:
        processTransport(command)
    if command.type == eventconsts.TYPE_JOG:
        processJog(command)
    
def processJog(command):
    if command.control == eventconsts.CONTROL_JOG_FORWARD:
        ui.next()
        command.handle("UI Next")
    elif command.control == eventconsts.CONTROL_JOG_BACKWARD:
        ui.previous()
        command.handle("UI Previous")

def processTransport(command):
    if command.control == eventconsts.CONTROL_PLAY:
        if command.is_lift:
            transport.start()
            command.handle("Toggle transport")
        else: command.handle("Button press catch")
    
    elif command.control == eventconsts.CONTROL_STOP:
        if command.is_lift:
            transport.stop()
            command.handle("Stop transport")
        else: command.handle("Button press catch")
    
    elif command.control == eventconsts.CONTROL_LOOP:
        if command.is_lift:
            transport.setLoopMode()
            command.handle("Toggle loop mode")
        else: command.handle("Button press catch")
    
    elif command.control == eventconsts.CONTROL_REC:
        if command.is_lift:
            transport.record()
            command.handle("Toggle recording")
        else: command.handle("Button press catch")

    elif command.control == eventconsts.CONTROL_SKIP_FORWARD:
        if command.is_lift:
            transport.fastForward(0)
            command.handle("End fast-forward")
        else:
            transport.fastForward(2)
            command.handle("Begin fast-forward")
        
    elif command.control == eventconsts.CONTROL_SKIP_BACK:
        if command.is_lift:
            transport.rewind(0)
            command.handle("End fast-forward")
        else:
            transport.rewind(2)
            command.handle("Begin fast-forward")

    elif command.control == eventconsts.CONTROL_NEXT:
        if command.is_lift:
            ui.next()
            command.handle("UI next")
        else: command.handle("Button press catch")
    
    elif command.control == eventconsts.CONTROL_PREV:
        if command.is_lift:
            ui.previous()
            command.handle("UI previous")
        else: command.handle("Button press catch")

