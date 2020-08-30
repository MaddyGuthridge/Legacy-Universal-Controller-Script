"""
eventprocessor > windowprocessors > processchannelrack.py

From Novation LaunchKey Mk2 Script by Miguel Guthridge.
Available under GNU GPL3 at https://github.com/MiguelGuthridge/Novation-LaunchKey-Mk2-Script
Adapted from v2.0.0

This script handles events when the channel rack is active.
It provides functionality such as setting channel volumes/pans.

Author: Miguel Guthridge
"""

import math # For logarithm

import channels
import ui

import config
import internal.consts
import internal
import eventconsts
import processorhelpers



def process(command):

    command.actions.addProcessor("Channel rack Processor")

    current_channel = channels.selectedChannel()

    

    #---------------------------------
    # Faders
    #---------------------------------
    if command.type == eventconsts.TYPE_FADER:
        fader_num = command.control

        if fader_num == eventconsts.CONTROL_MASTER_FADER:
            channel_num = current_channel
        else:
            channel_num = fader_num

        setVolume(command, channel_num, command.value)

    #---------------------------------
    # Knobs
    #---------------------------------
    if command.type == eventconsts.TYPE_KNOB:
        knob_num = command.control

        if knob_num == eventconsts.CONTROL_MASTER_KNOB:
            channel_num = current_channel
        else:
            channel_num = knob_num

        setPan(command, channel_num, command.value)


    #---------------------------------
    # Mixer Buttons - mute/solo tracks
    #---------------------------------
    if command.type == eventconsts.TYPE_FADER_BUTTON:
        fader_num = command.control
        if fader_num == eventconsts.CONTROL_MASTER_FADER_BUTTON:
            channel_num = current_channel
        else:
            channel_num = fader_num

        processMuteSolo(channel_num, command)

    return


def activeStart():
    return

def activeEnd():
    return

def topWindowStart():
    
    return

def topWindowEnd():
    return


def processMuteSolo(channel, command):

    if channels.channelCount() <= channel:
        command.handle("Channel out of range. Couldn't process mute", silent=True)
        return

    if command.value == 0: return
    if channels.isChannelSolo(channel) and channels.channelCount() != 1:
        channels.soloChannel(channel)
        action = "Unsolo channel"
        
    elif command.is_double_click:
        channels.soloChannel(channel)
        action = "Solo channel"
    else: 
        channels.muteChannel(channel)
        if channels.isChannelMuted(channel):
            action = "Mute channel"
        else: 
            action = "Unmute channel"

    command.handle(action)

def setVolume(command, channel, value):

    if channels.channelCount() <= channel:
        command.handle("Channel out of range. Couldn't set volume", silent=True)
        return

    volume = getVolumeSend(value)
    channels.setChannelVolume(channel, volume)
    action = "Set " + channels.getChannelName(channel) + " volume to " + getVolumeValue(value)
    if processorhelpers.didSnap(processorhelpers.toFloat(value), internal.consts.CHANNEL_VOLUME_SNAP_TO):
        action += " [Snapped]"
    command.handle(action)

def setPan(command, channel, value):
    if channels.channelCount() <= channel:
        command.handle("Channel out of range. Couldn't set pan", silent=True)
        return

    volume = getPanSend(value)
    channels.setChannelPan(channel, volume)
    action = "Set " + channels.getChannelName(channel) + " pan to " + getPanValue(value)
    if processorhelpers.didSnap(processorhelpers.toFloat(value, -1), internal.consts.CHANNEL_PAN_SNAP_TO):
        action = "[Snapped]"
    command.handle(action)

# Returns volume value set to send to FL Studio
def getVolumeSend(inVal):
    if config.ENABLE_SNAPPING:
        return processorhelpers.snap(processorhelpers.toFloat(inVal), internal.consts.CHANNEL_VOLUME_SNAP_TO)
    else: return processorhelpers.toFloat(inVal)


def getVolumeValue(inVal):
    
    return str(round(getVolumeSend(inVal) * 100)) + "%"



# Returns volume value set to send to FL Studio
def getPanSend(inVal):
    if config.ENABLE_SNAPPING:
        return processorhelpers.snap(processorhelpers.toFloat(inVal, -1), internal.consts.CHANNEL_PAN_SNAP_TO)
    else: return processorhelpers.toFloat(inVal, -1)


def getPanValue(inVal):
    
    a = round(getPanSend(inVal) * 100)
    if a < 0: b = str(a) + "% Left"
    elif a > 0: b = str(a) + "% Right"
    else: b = "Centred"
    return b
