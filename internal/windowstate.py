"""
internal > windowstate.py

Contains objects and functions to do with managing active FL windows.

Author: Miguel Guthridge
"""

import ui

from . import consts
import config
import eventprocessor

from eventprocessor import windowprocessors
from eventprocessor import pluginprocessors

from helpers import debugLog, getLineBreak


class WindowMgr:
    """Contains and manages the state of FL Windows as well as tickers for animations.
    """
    def __init__(self):
        self.plugin_focused = False
        self.previous_plugin = ""
        self.active_plugin = ""
        self.active_fl_window = -1
        self.animation_tick_number = 0
        self.idle_tick_number = 0
        self.absolute_tick_number = 0
        self.in_popup = False

    
    def getInPopup(self):
        """Returns whether a popup menu is active

        Returns:
            bool: whether a popup is active
        """
        return self.in_popup

    
    def update(self):
        """Update active window

        Returns:
            bool: Changed
        """
        
        popup_active = ui.isInPopupMenu()
        if popup_active:                
            self.in_popup = True
            
        else:
            self.in_popup = False
            
        
        old_window = self.active_fl_window
        # Update FL Window
        if   ui.getFocused(consts.WINDOW_MIXER):        
            new_fl_window = consts.WINDOW_MIXER

        elif ui.getFocused(consts.WINDOW_PIANO_ROLL):   
            new_fl_window = consts.WINDOW_PIANO_ROLL

        elif ui.getFocused(consts.WINDOW_CHANNEL_RACK): 
            new_fl_window = consts.WINDOW_CHANNEL_RACK

        elif ui.getFocused(consts.WINDOW_PLAYLIST):     
            new_fl_window = consts.WINDOW_PLAYLIST

        elif ui.getFocused(consts.WINDOW_BROWSER):      
            new_fl_window = consts.WINDOW_BROWSER
        
        else: new_fl_window = -1

        # Detect change in

        # If active FL window changes
        if (new_fl_window != self.active_fl_window or self.plugin_focused == True) and new_fl_window != -1:

            # End active window
            eventprocessor.activeEnd()

            # End old window
            if new_fl_window != self.active_fl_window:
                windowprocessors.topWindowEnd()

            # Set active window
            self.active_fl_window = new_fl_window
            self.plugin_focused =  False

            debugLog("Active Window: " + getFlWindowString(self.active_fl_window), consts.DEBUG.WINDOW_CHANGES)
            debugLog("[Background: " + self.active_plugin + "]", consts.DEBUG.WINDOW_CHANGES)
            debugLog(getLineBreak())

            # Start new window
            if new_fl_window != old_window:
                windowprocessors.topWindowStart()

            # Start new window active
            eventprocessor.activeStart()

            return True
        
        else: # Check for changes to Plugin
            new_plugin = ui.getFocusedFormCaption()
            
            old_plugin = self.active_plugin
            
            special_flag = False

            # Check for special windows
            if new_plugin == consts.WINDOW_STR_COLOUR_PICKER or new_plugin == consts.WINDOW_STR_SCRIPT_OUTPUT:
                special_flag = True

            if not special_flag:
                new_plugin = ui.getFocusedPluginName()

            if new_plugin == "":
                return False

            # If window changed
            if new_plugin != self.active_plugin or self.plugin_focused == False:

                # End active plugin
                eventprocessor.activeEnd()

                # End replaced plugin
                if new_plugin != self.active_plugin:
                    self.previous_plugin = self.active_plugin
                    pluginprocessors.topPluginEnd()

                # Set new plugin
                self.plugin_focused = True
                self.active_plugin = new_plugin

                debugLog("Active Window: " + self.active_plugin, consts.DEBUG.WINDOW_CHANGES)
                debugLog("[Background: " + getFlWindowString(self.active_fl_window) + "]", consts.DEBUG.WINDOW_CHANGES)
                debugLog(getLineBreak(), consts.DEBUG.WINDOW_CHANGES)

                # Start new plugin
                if new_plugin != old_plugin:
                    pluginprocessors.topPluginStart()

                # Start new plugin active
                eventprocessor.activeStart()

                return True
            else: return False

    def getString(self):
        """Returns current window as a string

        Returns:
            str: Current window name
        """
        if self.plugin_focused:
            return self.active_plugin

        else:
            return getFlWindowString(self.active_fl_window)

    
    def revertPlugin(self):
        """Reverts to previous plugin
        
        Note to self: I don't know when this is used - probably delete at some point.
        """
        self.active_plugin = self.previous_plugin
        self.previous_plugin = ""

# Create instance of window object
window = WindowMgr()


def getFlWindowString(index):
    """Returns FL Window as string given window index

    Args:
        index (int): FL Window index

    Returns:
        str: FL Window name
    """
    if index == -1: return "NONE"
    return consts.FL_WINDOW_LIST[index]
