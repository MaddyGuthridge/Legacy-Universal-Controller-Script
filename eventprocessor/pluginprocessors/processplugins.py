"""
eventprocessor > pluginprocessors > processplugins.py

From Novation LaunchKey Mk2 Script by Miguel Guthridge.
Available under GNU GPL3 at https://github.com/MiguelGuthridge/Novation-LaunchKey-Mk2-Script
Adapted from v2.0.0

This script forwards events to any plugin processors that can handle the currently active plugin.
More plugin processors can be added by adding them to the import list.

Author: Miguel Guthridge
"""

#
# Add custom event processors to this list
#
imports = []
#
#
#

import config
import internal
from .. import pluginprocessors

# Import custom processors specified in list above
print("Importing Plguin Processors")
customProcessors = []
for x in range(len(imports)):
    try:
        customProcessors.append( __import__("eventprocessor.pluginprocessors." + imports[x]) )
        print (" - Successfully imported:", getattr(pluginprocessors, imports[x]).PLUGINS)
    except ImportError:
        print (" - Error importing: " + imports[x])
        raise
print("Plugin Processor import complete")

# Called when plugin is top plugin
def topPluginStart():
    for x in imports:
        object_to_call = getattr(pluginprocessors, x)
        if canHandle(object_to_call):
            object_to_call.topPluginStart()
    return

# Called when plugin is no longer top plugin
def topPluginEnd():
    for x in imports:
        object_to_call = getattr(pluginprocessors, x)
        if canHandle(object_to_call):
            object_to_call.topPluginEnd()
    return

# Called when plugin brought to foreground
def activeStart():
    for x in imports:
        object_to_call = getattr(pluginprocessors, x)
        if canHandle(object_to_call):
            object_to_call.activeStart()
    return

# Called when plugin no longer in foreground
def activeEnd():
    for x in imports:
        object_to_call = getattr(pluginprocessors, x)
        if canHandle(object_to_call):
            object_to_call.activeEnd()
    return

def process(command):
    for x in imports:
        object_to_call = getattr(pluginprocessors, x)
        if canHandle(object_to_call):
            object_to_call.process(command)
        
        if command.handled: return

def canHandle(object_to_call):
    for x in range(len(object_to_call.PLUGINS)):
        if object_to_call.PLUGINS[x] == internal.window.active_plugin:
            return True

    return False

