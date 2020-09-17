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

from PySide2.QtCore import QByteArray, QRect
from PySide2.QtWidgets import (QApplication, QDialog, QDialogButtonBox, QHBoxLayout,
                               QListWidget, QStackedWidget, QVBoxLayout, QWidget)

from application_settings import ApplicationSettings
from settings import Settings


class PreferencesDialog(QDialog):

    m_settings = Settings()


    def __init__(self, parent=None):
        """
        Initializes the PreferencesDialog class.
        """
        super(PreferencesDialog, self).__init__(parent)

        # Settings box
        self.applicationSettings = ApplicationSettings(self)
        self.applicationSettings.settingChanged.connect(self.onSettingsChanged)

        stackedBox = QStackedWidget()
        stackedBox.addWidget(self.applicationSettings)
        stackedBox.setCurrentIndex(0)

        listBox = QListWidget()
        listBox.addItem(self.applicationSettings.title())
        listBox.setCurrentRow(stackedBox.currentIndex())
        listBox.currentRowChanged.connect(stackedBox.setCurrentIndex)

        settingsBox = QHBoxLayout()
        settingsBox.addWidget(listBox, 1)
        settingsBox.addWidget(stackedBox, 3)

        # Button box
        buttonBox = QDialogButtonBox(QDialogButtonBox.RestoreDefaults | QDialogButtonBox.Ok | QDialogButtonBox.Apply | QDialogButtonBox.Cancel)
        self.buttonApply = buttonBox.button(QDialogButtonBox.Apply)
        buttonBox.button(QDialogButtonBox.RestoreDefaults).clicked.connect(self.onButtonDefaultsClicked)
        buttonBox.accepted.connect(self.onButtonOkClicked)
        buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.onButtonApplyClicked)
        buttonBox.rejected.connect(self.close)

        # Main layout
        layout = QVBoxLayout()
        layout.addLayout(settingsBox, 1)
        layout.addWidget(buttonBox)

        self.setLayout(layout)

        self.updateSettings(self.m_settings)


    def onSettingsChanged(self):
        """
        Enables the apply button if the settings have been changed.
        """
        self.buttonApply.setEnabled(True)


    def windowGeometry(self):
        """
        Returns the geometry of the widget.
        """
        return self.saveGeometry()


    def setWindowGeometry(self, geometry):
        """
        Sets the geometry of the widget.
        """
        if geometry:
            self.restoreGeometry(geometry)
        else:
            availableGeometry = QRect(QApplication.desktop().availableGeometry(self))
            self.resize(availableGeometry.width() / 2, availableGeometry.height() / 2)
            self.move((availableGeometry.width() - self.width()) / 2, (availableGeometry.height() - self.height()) / 2)


    def settings(self):
        """
        Returns the user preferences.
        """
        return self.m_settings


    def setSettings(self, settings):
        """
        Sets the user preferences.
        """
        self.updateSettings(settings)
        self.saveSettings()


    def updateSettings(self, settings):
        """
        Updates the settings.
        """

        # Application: Appearance
        self.applicationSettings.setRestoreWindowGeometry(settings.restoreWindowGeometry)
        self.applicationSettings.setRestoreDialogGeometry(settings.restoreDialogGeometry)


    def saveSettings(self):
        """
        Reads the user preferences and saves them.
        """

        # Application: Appearance
        self.m_settings.restoreWindowGeometry = self.applicationSettings.restoreWindowGeometry()
        self.m_settings.restoreDialogGeometry = self.applicationSettings.restoreDialogGeometry()

        self.buttonApply.setEnabled(False)


    def onButtonDefaultsClicked(self):
        """
        Restores default values of user preferences.
        """
        settings = Settings()
        self.updateSettings(settings)


    def onButtonOkClicked(self):
        """
        Closes the dialog with saving user preferences.
        """
        self.saveSettings()
        self.close()


    def onButtonApplyClicked(self):
        """
        Saves user preferences.
        """
        self.saveSettings()
