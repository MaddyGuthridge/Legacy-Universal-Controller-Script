import internal

from . import processdefault
from . import pluginprocessors, windowprocessors

def process(command):
    
    windowprocessors.process(command)
    
    if command.handled:
        return
    
    processdefault.process(command)
    

# Called after a window is activated
def activeStart():
    """Activates a new window or plugin
    """
    if internal.window.plugin_focused:
        pluginprocessors.activeStart()
    else:
        windowprocessors.activeStart()


def activeEnd():
    """Deactivates an old window or plugin
    """
    if internal.window.plugin_focused:
        pluginprocessors.activeEnd()
    else:
        windowprocessors.activeEnd()
