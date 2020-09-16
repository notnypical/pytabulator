# This Python file uses the following encoding: utf-8
#
# Copyright 2020 NotNypical, <https://notnypical.github.io>.
#
# This file is part of pyTabulator.
#
# pyTabulator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyTabulator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyTabulator.  If not, see <https://www.gnu.org/licenses/>.
#

from PySide2.QtCore import QByteArray, QRect, QSettings
from PySide2.QtWidgets import QApplication, QDialog, QDialogButtonBox, QVBoxLayout

from keyboard_shortcuts_page import KeyboardShortcutsPage


class KeyboardShortcutsDialog(QDialog):

    def __init__(self, parent=None):
        """
        Initializes the KeyboardShortcutsDialog class.
        """
        super(KeyboardShortcutsDialog, self).__init__(parent)

        self.setupUI()

        self.readSettings()


    def setupUI(self):
        """
        Sets up the user interface.
        """

        buttonBox = QDialogButtonBox(QDialogButtonBox.Close)
        buttonBox.rejected.connect(self.close)

        # Main layout
        layout = QVBoxLayout()
        layout.addWidget(KeyboardShortcutsPage(self.parentWidget()), 1)
        layout.addWidget(buttonBox)

        self.setLayout(layout)


    def readSettings(self):
        """
        Restores user preferences and other dialog properties.
        """
        settings = QSettings()

        # Read user preferences
        geometryDialogRestore = self.valueToBool(settings.value('Settings/geometryDialogRestore', True))

        # Set dialog properties
        geometry = settings.value('KeyboardShortcutsDialog/geometry', QByteArray())
        if geometryDialogRestore and geometry:
            self.restoreGeometry(geometry)
        else:
            availableGeometry = QRect(QApplication.desktop().availableGeometry(self))
            self.resize(availableGeometry.width() / 3, availableGeometry.height() / 3);
            self.move((availableGeometry.width() - self.width()) / 2, (availableGeometry.height() - self.height()) / 2);


    def writeSettings(self):
        """
        Saves user preferences and other dialog properties.
        """
        settings = QSettings()

        # Read user preferences
        geometryDialogRestore = self.valueToBool(settings.value('Settings/geometryDialogRestore', True))

        # Store dialog properties
        if geometryDialogRestore:
            settings.setValue('KeyboardShortcutsDialog/geometry', self.saveGeometry())


    @staticmethod
    def valueToBool(value):
        """
        Converts a specified value to an equivalent Boolean value.

        Args:
            value (bool): The specified value.

        Returns:
            bool: The equivalent Boolean value.
        """
        return value.lower() == 'true' if isinstance(value, str) else bool(value)


    def closeEvent(self, event):
        """
        Processes the close event.

        Args:
            event (QCloseEvent): The close event.
        """
        self.writeSettings()
        event.accept()