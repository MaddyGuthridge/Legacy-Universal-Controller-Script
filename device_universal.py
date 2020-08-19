# name=Universal Controller
# url=https://github.com/MiguelGuthridge/Universal-Controller-Script

"""
device_universal.py

This file is the controller file for a universal device. It forwards events onto various event processors.

Author: Miguel Guthridge
"""


import patterns
import channels
import mixer
import device
import transport
import arrangement
import general
import launchMapPages
import playlist
import ui
import screen

import midi
import utils



class TGeneric():
    def __init__(self):
        return

    def OnInit(self):
        pass

    def OnDeInit(self):
        pass

    def OnMidiIn(self, event):
        pass
    
    def OnIdle(self):
        pass




Generic = TGeneric()

def OnInit():
    Generic.OnInit()

def OnDeInit():
    Generic.OnDeInit()

def OnMidiIn(event):
    Generic.OnMidiIn(event)

def OnIdle():
    Generic.OnIdle()