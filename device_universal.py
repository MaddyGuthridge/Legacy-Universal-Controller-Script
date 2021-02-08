# name=Universal Controller
# url=https://github.com/MiguelGuthridge/Universal-Controller-Script

"""
device_universal.py

This file is the controller file for a universal device. It forwards events onto various event processors.

Author: Miguel Guthridge
"""

import internal
import helpers
import eventprocessor

def OnInit():
    internal.setup.initialise()

def OnDeInit():
    pass

def OnMidiIn(event):
    
    command = internal.parse.ParsedEvent(event)
    
    if internal.initState == internal.consts.INIT_FAIL:
        return
    elif internal.initState == internal.consts.INIT_INCOMPLETE:
        internal.setup.processInitMessage(command)
    elif internal.initState == internal.consts.INIT_SETUP:
        internal.setup.processSetup(command)
    elif internal.initState == internal.consts.INIT_SUCCESS:
        eventprocessor.process(command)
    
    if command.edited:
        event.status = command.status
        event.data1 = command.note
        event.data2 = command.value
    
    if command.handled:
        event.handled = True
    
    command_str = str(command)
    if len(command_str):
        print(command_str)

def OnIdle():
    internal.window.update()
    internal.window.incrementTicks()
    
    # FIXME: For debugging only. Remove before release
    if internal.window.absolute_tick_number < 100:
        import time
        curr_time = time.localtime()
        print("IDLE: Tick number    =", internal.window.absolute_tick_number)
        print("TIMEOUT REQUIRED     =", internal.consts.INIT_TIMEOUT)
        print("CURRENT TIME         =", curr_time.tm_hour, curr_time.tm_min, curr_time.tm_sec)
        print("INITIALISATION STATE =", internal.initState.state)
        print("")
    
    if internal.initState == internal.consts.INIT_SETUP:
        internal.setup.idleSetup()
    elif internal.initState == internal.consts.INIT_INCOMPLETE:
        internal.setup.idleInit()

