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
    detector.addEvent(command.status, command.note, eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP)
    
    learn.setCurrent("Press", eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_PLAY, "button")

def setupPlay(command):
    if command.type == eventconsts.TYPE_UNKNOWN:
        detector.addEvent(command.status, command.note, eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_PLAY)
        learn.setCurrent("Press", eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_LOOP, "button")

def setupLoop(command):
    if command.type == eventconsts.TYPE_UNKNOWN:
        detector.addEvent(command.status, command.note, eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_LOOP)
        learn.setCurrent("Press", eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_REC, "button")
    
def setupRec(command):
    if command.type == eventconsts.TYPE_UNKNOWN:
        detector.addEvent(command.status, command.note, eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_REC)
        learn.setCurrent("Press", eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_SKIP_FORWARD, "button")

def setupSkipForward(command):
    if command.type == eventconsts.TYPE_UNKNOWN:
        detector.addEvent(command.status, command.note, eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_SKIP_FORWARD)
        learn.setCurrent("Press", eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_SKIP_BACK, "button")

def setupSkipBackward(command):
    if command.type == eventconsts.TYPE_UNKNOWN:
        detector.addEvent(command.status, command.note, eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_SKIP_BACK)
        learn.setCurrent("Press", eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_NEXT, "button", True)
        
def setupNextTrack(command):
    if command.type == eventconsts.TYPE_UNKNOWN:
        detector.addEvent(command.status, command.note, eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_NEXT)
        learn.setCurrent("Press", eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_PREV, "button")
    if command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP):
        fader.setLearnFirstFader()

def setupPrevTrack(command):
    if command.type == eventconsts.TYPE_UNKNOWN:
        detector.addEvent(command.status, command.note, eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_PREV)
        command.refreshId()
        fader.setLearnFirstFader()
