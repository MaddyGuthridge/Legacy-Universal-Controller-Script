# name=Universal Controller
# url=https://github.com/MiguelGuthridge/Universal-Controller-Script

"""
device_universal.py

This file is the controller file for a universal device. It forwards events onto various event processors.

Author: Miguel Guthridge
"""

import internal
import eventprocessor

def OnInit():
    internal.setup.initialise()

def OnDeInit():
    pass

def OnMidiIn(event):
    
    command = eventprocessor.ParsedEvent(event)
    
    
    
    if internal.initState == internal.consts.INIT_FAIL:
        return
    elif internal.initState == internal.consts.INIT_SETUP:
        internal.setup.processSetup(command)
    elif internal.initState == internal.consts.INIT_SUCCESS:
        print(command)

def OnIdle():
    pass