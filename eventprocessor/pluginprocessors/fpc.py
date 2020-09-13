"""
eventprocessor > pluginprocessors > _template.py

Adapted from Novation LaunchKey Mk2 Script by Miguel Guthridge.
Available under GNU GPL3 at https://github.com/MiguelGuthridge/Novation-LaunchKey-Mk2-Script
Adapted from v2.0.0

The file acts as a template for plugin handlers. Copy it and edit to add your own plugin handlers.
To get it to be imported by the event processor, add its filename (without the .py) to processplugins.py

Author: Miguel Guthridge
"""

# Add names of plugins your script can process to this list
PLUGINS = ["FPC"]


# Import any modules you might need
import config
import internal
import eventconsts
import processorhelpers

FPC_DRUM_CONSTS = [
    [49, 55, 51, 53],
    [48, 47, 45, 43],
    [40, 38, 46, 44],
    [37, 36, 42, 54]
]

NOTE_STATUS = 0x90

def topPluginStart():
    """Called when plugin is top plugin (not neccesarily focused)
    """
    return

def topPluginEnd():
    """Called when plugin is no longer top plugin (not neccesarily focused)
    """
    return

def activeStart():
    """Called when plugin brought to foreground (focused)
    """
    return

def activeEnd():
    """Called when plugin no longer in foreground (end of focused)
    """
    
    return

def process(command):
    """Called when processing commands. 

    Args:
        command (ParsedEvent): contains useful information about the event. 
            Use this to determing what actions your processor will take.
    """
    # Add event processor to actions list (useful for debugging)
    command.addProcessor("FPC Processor")

    if command.type == eventconsts.TYPE_DRUM_PAD:
        
        # Get new note num
        controller_x, controller_y = internal.controllerinfo.sizeDrumPads()
        new_note = None
        action_suffix = ""
        if controller_x >= 4 and controller_y >= 4 and checkTupleRange(command.control, 4, 4):
            new_note = getNumber4x4(command.control)
            action_suffix = "(4x4)"
        if controller_x >= 8 and controller_y >= 2 and checkTupleRange(command.control, 8, 2):
            new_note = getNumber8x2(command.control)
            action_suffix = "(8x2)"
    
        if type(new_note) is not None:
            command.edit(processorhelpers.RawEvent(NOTE_STATUS, new_note, command.value), "Remap for FPC " + action_suffix)
        

    return

def getNumber4x4(coords):
    return FPC_DRUM_CONSTS[coords[1]][coords[0]]

def getNumber8x2(coords):
    # Remap into 4x4
    x = coords[0]
    y = coords[1]
    if x < 4:
        y += 2
    elif x >= 4:
        x -= 4
    return getNumber4x4((x, y))

def checkTupleRange(coord, x, y):
    return coord[0] <= x and coord[1] <= y
