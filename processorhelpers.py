"""
processorhelpers.py

From Novation LaunchKey Mk2 Script by Miguel Guthridge.
Available under GNU GPL3 at https://github.com/MiguelGuthridge/Novation-LaunchKey-Mk2-Script

From v1.4.0

This script includes objects useful for event processors. 
It is worth investigating potential applications of these functions when writing your processors, 
or adding other frequently-required functions here.

Author: Miguel Guthridge
"""

import time

import utils
import ui

import config
import eventconsts
import internal
import internal.consts
import helpers


def snap(value, snapTo):
    """Returns a snapped value

    Args:
        value (float): value being snapped
        snapTo (float): value to snap to

    Returns:
        float: value after snapping
    """
    if abs(value - snapTo) <= config.SNAP_RANGE and config.ENABLE_SNAPPING:
        return snapTo
    else: return value

def didSnap(value, snapTo):
    """Returns a boolean indicating whether a value was snapped

    Args:
        value (float): value being snapped
        snapTo (float): value to snap to

    Returns:
        bool: whether the value would snap
    """
    if abs(value - snapTo) <= config.SNAP_RANGE and config.ENABLE_SNAPPING:
        return True
    else: return False

def toFloat(value, min = 0, max = 1):
    """Converts a MIDI event value (data2) to a float to set parameter values.

    Args:
        value (int): MIDI event value (0-127)
        min (float, optional): lower value to set between. Defaults to 0.
        max (float, optional): upper value to set between. Defaults to 1.

    Returns:
        float: range value
    """
    return (value / 127) * (max - min) + min


lastPressID = -1
lastPressTime = -1
def isDoubleClickPress(id):
    """Returns whether a press event was a double click

    Args:
        id (int): Event ID

    Returns:
        bool: whether the event was a double click
    """
    global lastPressID
    global lastPressTime
    ret = False
    currentTime = time.perf_counter()
    if id == lastPressID and (currentTime - lastPressTime < config.DOUBLE_PRESS_TIME):
        ret = True
    lastPressID = id
    lastPressTime = currentTime
    return ret


lastLiftID = -1
lastLiftTime = -1
def isDoubleClickLift(id):
    """Returns whether a lift event was a double click

    Args:
        id (int): Event ID

    Returns:
        bool: whether the event was a double click
    """
    global lastLiftID
    global lastLiftTime
    ret = False
    currentTime = time.perf_counter()
    if id == lastLiftID and (currentTime - lastLiftTime < config.DOUBLE_PRESS_TIME):
        ret = True
    lastLiftID = id
    lastLiftTime = currentTime
    return ret



class Action:
    """Stores an action as a string
    """
    def __init__(self, act, silent):
        """Create an event action

        Args:
            act (str): The action taken
            silent (bool): Whether the action should be set as a hint message
        """
        self.act = act
        self.silent = silent

class ActionList:
    """Stores a list of actions taken by a single processor
    """
    def __init__(self, name):
        """Create an action list

        Args:
            name (str): Name of the processor
        """
        self.name = name
        self.list = []
        self.didHandle = False

    
    def appendAction(self, action, silent, handle):
        """Append action to list of actions

        Args:
            action (str): The action taken
            silent (bool): Whether the action should be set as a hint message
            handle (bool): Whether this action handled the event
        """
        self.list.append(Action(action, silent))

        # Set flag indicating that this processor handled the event
        if handle:
            self.didHandle = True

    def getString(self):
        """Returns a string of the actions taken

        Returns:
            str: actions taken
        """
        # Return that no action was taken if list is empty
        if len(self.list) == 0:
            return helpers.getTab(self.name + ":", 2) + "[No actions]"

        # No indentation required if there was only one action
        elif len(self.list) == 1:
            ret = helpers.getTab(self.name + ":", 2) + self.list[0].act

        # If there are multiple actions, indent them
        else:
            ret = self.name + ":"
            for i in range(len(self.list)):
                ret += '\n' + helpers.getTab("") + self.list[i].act

        if self.didHandle:
            ret += '\n' + helpers.getTab("") + "[Handled]"
        return ret

    # Returns the latest non-silent action to set as the hint message
    def getHintMsg(self):
        """Returns string of hint message to set, empty string if none

        Returns:
            str: Hint message
        """
        ret = ""
        for i in range(len(self.list)):
            if self.list[i].silent == False:
                ret = self.list[i].act
        return ret


class ActionPrinter:
    """Object containing actions taken by all processor modules
    """

    def __init__(self):
        # String that is output after each event is processed
        self.eventProcessors = []

    
    def addProcessor(self, name):
        """Add an event processor

        Args:
            name (str): Name of the processor
        """
        self.eventProcessors.append(ActionList(name))

    
    def appendAction(self, act, silent=False, handled=False):
        """Appends an action to the current event processor

        Args:
            act (str): The action taken
            silent (bool, optional): Whether the action should be set as a hint message. Defaults to False.
            handled (bool, optional): Whether the action handled the event. Defaults to False.
        """

        # Add some random processor if a processor doesn't exist for some reason
        if len(self.eventProcessors) == 0:
            self.addProcessor("NoProcessor")
            helpers.debugLog("Added NoProcessor Processor", internal.consts.DEBUG.WARNING_DEPRECIATED_FEATURE)
        # Append the action
        self.eventProcessors[len(self.eventProcessors) - 1].appendAction(act, silent, handled)

    def flush(self):
        """Log all actions taken, and set a hint message if applicable
        """
        ret = ""
        
        # Log all actions taken
        for x in range(len(self.eventProcessors)):
            ret += self.eventProcessors[x].getString() + '\n'

        # Get hint message to set (ignores silent messages)
        hint_msg = ""
        for x in range(len(self.eventProcessors)):
            cur_msg = self.eventProcessors[x].getHintMsg()

            # Might want to fix this some time, some handler modules append this manually
            if cur_msg != "" and cur_msg != "[Did not handle]":
                hint_msg = cur_msg

        if hint_msg != "":
            # Sometimes this fails...
            try:
                ui.setHintMsg(hint_msg)
            except:
                pass
        self.eventProcessors.clear()
        
        return ret


class RawEvent:
    """Stores event in raw form. A quick way to generate events for editing.
    """
    def __init__(self, status, data1, data2, shift = False):
        """Create a RawEvent object

        Args:
            status (int): Status byte
            data1 (int): First data byte
            data2 (int): 2nd data byte
            shift (bool, optional): Whether the event is shifted. Defaults to False.
        """
        self.status = status
        self.data1 = data1
        self.data2 = data2
        self.shift = shift
