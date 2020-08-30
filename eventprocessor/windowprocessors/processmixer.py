"""
eventprocessor > windowprocessors > processmixer.py

From Novation LaunchKey Mk2 Script by Miguel Guthridge.
Available under GNU GPL3 at https://github.com/MiguelGuthridge/Novation-LaunchKey-Mk2-Script
Adapted from v2.0.0

This script processes events when the mixer window is active. It provides functionality
such as setting track volumes.

Author: Miguel Guthridge
"""

import mixer
import transport

import eventconsts
import internal
import internal.consts
import config
import processorhelpers


# Process is called to handle events
def process(command):

    command.actions.addProcessor("Mixer Processor")

    current_track = mixer.trackNumber()

    #---------------------------------
    # Faders
    #---------------------------------
    if command.type == eventconsts.TYPE_FADER:
        processFaders(command)

    #---------------------------------
    # Knobs
    #---------------------------------
    if command.type == eventconsts.TYPE_KNOB:
        processKnobs(command)


    #---------------------------------
    # Mixer Buttons - mute/solo tracks
    #---------------------------------
    if command.type == eventconsts.TYPE_FADER_BUTTON or command.type == eventconsts.TYPE_SOLO_BUTTON:
        processFaderButtons(command)

    #---------------------------------
    # Other
    #---------------------------------

# Process fader events
def processFaders(command):
    current_track = mixer.trackNumber()
    fader_num = command.control + 1

    if fader_num == 0:
        track_num = current_track
    else:
        track_num = fader_num

    setVolume(command, track_num, command.value)

# Process knob events
def processKnobs(command):
    current_track = mixer.trackNumber()

    knob_num = command.control + 1

    if knob_num == 0:
        track_num = current_track
    else:
        track_num = knob_num

    setPan(command, track_num, command.value)

# Process fader button events
def processFaderButtons(command):
    current_track = mixer.trackNumber()
    
    fader_num = command.control + 1

    if fader_num == 0:
        track_num = current_track
    else:
        track_num = fader_num

    processMuteSolo(track_num, command)


def activeStart():
    return

def activeEnd():
    return

def topWindowStart():
    return

def topWindowEnd():
    return

def processMuteSolo(track, command):
    if command.value == 0: 
        command.handle("Button lift")
        return
    if internal.controllerinfo.hasSeperateSoloButtons():
        if command.type == eventconsts.TYPE_FADER_BUTTON:
            mixer.muteTrack(track)
            if mixer.isTrackMuted(track):
                command.handle("Mute track " + str(track))
            else: 
                command.handle("Unmute track " + str(track))
        elif command.type == eventconsts.TYPE_SOLO_BUTTON:
            mixer.soloTrack(track)
            if mixer.isTrackSolo(track):
                command.handle("Solo track " + str(track))
            else: 
                command.handle("Unsolo track " + str(track))
                
    else:
        if mixer.isTrackSolo(track):
            mixer.soloTrack(track)
            command.handle("Unsolo track " + str(track))
            return
        mixer.muteTrack(track)
        if command.is_double_click:
            mixer.soloTrack(track)
            command.handle("Solo track " + str(track))
        else: 
            if mixer.isTrackMuted(track):
                command.handle("Mute track " + str(track))
            else: 
                command.handle("Unmute track " + str(track))

def setVolume(command, track, value):
    volume = getVolumeSend(value)
    mixer.setTrackVolume(track, volume)
    command.handle("Set " + mixer.getTrackName(track) + " volume to " + getVolumeValue(value))
    if processorhelpers.didSnap(processorhelpers.toFloat(value), internal.consts.MIXER_VOLUME_SNAP_TO):
        command.handle("[Snapped]")

# Returns volume value set to send to FL Studio
def getVolumeSend(inVal):
    if config.ENABLE_SNAPPING:
        return processorhelpers.snap(processorhelpers.toFloat(inVal), internal.consts.MIXER_VOLUME_SNAP_TO)
    else: return processorhelpers.toFloat(inVal)


def getVolumeValue(inVal):
    
    return str(round(getVolumeSend(inVal) / internal.consts.MIXER_VOLUME_SNAP_TO * 100)) + "%"

def setPan(command, track, value):
    volume = getPanSend(value)
    mixer.setTrackPan(track, volume)
    command.handle("Set " + mixer.getTrackName(track) + " pan to " + getPanValue(value))
    if processorhelpers.didSnap(processorhelpers.toFloat(value, -1), internal.consts.MIXER_PAN_SNAP_TO):
        command.handle("[Snapped]")

# Returns volume value set to send to FL Studio
def getPanSend(inVal):
    if config.ENABLE_SNAPPING:
        return processorhelpers.snap(processorhelpers.toFloat(inVal, -1), internal.consts.MIXER_PAN_SNAP_TO)
    else: return processorhelpers.toFloat(inVal, -1)


def getPanValue(inVal):
    
    a = round(getPanSend(inVal) * 100)
    if a < 0: b = str(a) + "% Left"
    elif a > 0: b = str(a) + "% Right"
    else: b = "Centred"
    return b
