"""

"""
# -*- encoding: utf-8 -*-

import os
import gtk
import gedit
import gobject

from ui import UserInterface
from dojotools import Monitor, Timer

class DojoToolsGeditHelper:
    def __init__(self, plugin, window):
        self._window = window
        self._plugin = plugin

    def deactivate(self):
        self._window = None
        self._plugin = None

    def update_ui(self):
        # Called whenever the window has been updated (active tab
        # changed, etc.)
        print "Plugin update for", self._window

class DojoToolsGedit(gedit.Plugin):
    def __init__(self):
        gedit.Plugin.__init__(self)
        self._instances = {}

    def activate(self, window):
        timer = Timer(300)
        ui = UserInterface(timer)
        monitor = Monitor(
            ui = ui,
            directory = '/home/cesar/Dojo/codigosDojo/setembro/25/',
            commands = ["python /home/cesar/Dojo/codigosDojo/setembro/25/teste_Jo_Ken_Po.py",],
            patterns_file = '/home/cesar/Dojo/codigosDojo/setembro/25/.ignore',
            commit = False,
        )

        gtk.main()
        self._instances[window] = DojoToolsGeditHelper(self, window)

    def deactivate(self, window):
        self._instances[window].deactivate()
        del self._instances[window]

    def update_ui(self, window):
        self._instances[window].update_ui()
