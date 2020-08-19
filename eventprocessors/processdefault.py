import transport
import ui
import midi

import eventconsts

def process(command):
    command.addProcessor("Default processor")

    if command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_PLAY):
        if command.is_lift:
            transport.start()
            command.handle("Toggle transport")
        else: command.handle("Button press catch")
    
    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP):
        if command.is_lift:
            transport.stop()
            command.handle("Stop transport")
        else: command.handle("Button press catch")
    
    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_LOOP):
        if command.is_lift:
            transport.setLoopMode()
            command.handle("Toggle loop mode")
        else: command.handle("Button press catch")
    
    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_REC):
        if command.is_lift:
            transport.record()
            command.handle("Toggle recording")
        else: command.handle("Button press catch")

    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_SKIP_FORWARD):
        if command.is_lift:
            transport.fastForward(0)
            command.handle("End fast-forward")
        else:
            transport.fastForward(2)
            command.handle("Begin fast-forward")
        
    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_SKIP_BACK):
        if command.is_lift:
            transport.rewind(0)
            command.handle("End fast-forward")
        else:
            transport.rewind(2)
            command.handle("Begin fast-forward")

    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_NEXT):
        if command.is_lift:
            ui.next()
            command.handle("UI next")
        else: command.handle("Button press catch")
    
    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_PREV):
        if command.is_lift:
            ui.next()
            command.handle("UI previous")
        else: command.handle("Button press catch")

