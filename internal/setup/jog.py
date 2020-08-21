import eventconsts
from ..parse import detector
from .setup import learn
from . import fader

def setupJog(command):
    if learn[1] == eventconsts.CONTROL_JOG_FORWARD:
        setupForward(command)
    elif learn[1] == eventconsts.CONTROL_JOG_BACKWARD:
        setupBackward(command)
    elif learn[1] == eventconsts.CONTROL_JOG_PUSH:
        setupPush(command)
    elif learn[1] == eventconsts.CONTROL_JOG_PULL:
        setupPull(command)

def setupForward(command):
    if command.type == eventconsts.TYPE_UNKNOWN:
        command.handle("Register jog forward")
        detector.addEvent(command.status, command.note, command.value, eventconsts.TYPE_JOG, eventconsts.CONTROL_JOG_FORWARD)
        learn.setCurrent(eventconsts.TYPE_JOG, eventconsts.CONTROL_JOG_BACKWARD, "Move the jog wheel backwards")
    if command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP) and command.is_lift:
        command.handle("No jog wheel")
        fader.setLearnFirstFader()

def setupBackward(command):
    if command.type == eventconsts.TYPE_UNKNOWN:
        command.handle("Register jog backward")
        detector.addEvent(command.status, command.note, command.value, eventconsts.TYPE_JOG, eventconsts.CONTROL_JOG_BACKWARD)
        learn.setCurrent(eventconsts.TYPE_JOG, eventconsts.CONTROL_JOG_PUSH, "Push the jog wheel down.")
        print("If your controller doesn't support this, press the stop button")

def setupPush(command):
    if command.type == eventconsts.TYPE_UNKNOWN:
        command.handle("Register jog push")
        detector.addEvent(command.status, command.note, command.value, eventconsts.TYPE_JOG, eventconsts.CONTROL_JOG_PUSH)
        learn.setCurrent(eventconsts.TYPE_JOG, eventconsts.CONTROL_JOG_PULL, "Pull the jog wheel up")
    if command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP) and command.is_lift:
        command.handle("No jog wheel push")
        fader.setLearnFirstFader()

def setupPull(command):
    if command.type == eventconsts.TYPE_UNKNOWN:
        command.handle("Register jog pull")
        detector.addEvent(command.status, command.note, command.value, eventconsts.TYPE_JOG, eventconsts.CONTROL_JOG_PULL)
    elif command.getId() == (eventconsts.TYPE_TRANSPORT, eventconsts.CONTROL_STOP) and command.is_lift:
        command.handle("No jog wheel pull")
    else:
        return    
    fader.setLearnFirstFader()
    