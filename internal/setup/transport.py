"""
internal > setup > transport.py

Allows for the setup of transport buttons

Author: Miguel Guthridge
"""

import ui

from ..parse import detector
from .setup import learn
from . import fader

import eventconsts


def setupTransport(command):
    if command.is_lift:
        if learn[1] == eventconsts.CONTROL_STOP:
            setupStop(command)
        elif learn[1] == eventconsts.CONTROL_PLAY:
            setupPlay(command)
        elif learn[1] == eventconsts.CONTROL_LOOP:
            setupLoop(command)
        elif learn[1] == eventconsts.CONTROL_REC:
            setupRec(command)
        elif learn[1] == eventconsts.CONTROL_SKIP_FORWARD:
            setupSkipForward(command)
        elif learn[1] == eventconsts.CONTROL_SKIP_BACK:
            setupSkipBackward(command)
        elif learn[1] == eventconsts.CONTROL_NEXT:
            setupNextTrack(command)
        elif learn[1] == eventconsts.CONTROL_PREV:
            setupPrevTrack(command)


def setupStop(command):
    detector.addEvent(command.status, command.note, command.value, eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP)
    command.handle("Register stop button")
    learn.setCurrent(eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_LOOP, "Press the loop button", True)
    
    # Reset startup hint message
    ui.setHintMsg("")

def setupPlay(command):
    if command.type == eventconsts.TYPE_UNKNOWN:
        command.handle("Register play button")
        detector.addEvent(command.status, command.note, command.value, eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_PLAY)
        learn.setCurrent(eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP, "Press the stop button")

def setupLoop(command):
    if command.type == eventconsts.TYPE_UNKNOWN:
        command.handle("Register loop button")
        detector.addEvent(command.status, command.note, command.value, eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_LOOP)
    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP):
        command.handle("No loop button")
    else:
        return
    learn.setCurrent(eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_REC, "Press the record button", True)
    
def setupRec(command):
    if command.type == eventconsts.TYPE_UNKNOWN:
        command.handle("Register record button")
        detector.addEvent(command.status, command.note, command.value, eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_REC)
    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP):
        command.handle("No record button")
    else:
        return
    learn.setCurrent(eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_SKIP_FORWARD, "Press the fast-forward button", True)

def setupSkipForward(command):
    if command.type == eventconsts.TYPE_UNKNOWN:
        command.handle("Register fast-forward button")
        detector.addEvent(command.status, command.note, command.value, eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_SKIP_FORWARD)
        learn.setCurrent(eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_SKIP_BACK, "Press the rewind button")
    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP):
        command.handle("No skip buttons")
        learn.setCurrent(eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_NEXT, "Press the next track button", True)

def setupSkipBackward(command):
    if command.type == eventconsts.TYPE_UNKNOWN:
        command.handle("Register rewind button")
        detector.addEvent(command.status, command.note, command.value, eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_SKIP_BACK)
        learn.setCurrent(eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_NEXT, "Press the next track button", True)
        
def setupNextTrack(command):
    if command.type == eventconsts.TYPE_UNKNOWN:
        command.handle("Register next track button")
        detector.addEvent(command.status, command.note, command.value, eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_NEXT)
        learn.setCurrent(eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_PREV, "Press the previous track button")
    if command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP):
        command.handle("No track increment buttons.")
        learn.setCurrent(eventconsts.TYPE_JOG, eventconsts.CONTROL_JOG_FORWARD, "Move the jog wheel forwards", True)

def setupPrevTrack(command):
    if command.type == eventconsts.TYPE_UNKNOWN:
        command.handle("Register previous track button")
        detector.addEvent(command.status, command.note, command.value, eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_PREV)
        command.refreshId()
        learn.setCurrent(eventconsts.TYPE_JOG, eventconsts.CONTROL_JOG_FORWARD, "Move the jog wheel forwards", True)
