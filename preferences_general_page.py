# This Python file uses the following encoding: utf-8
#
# Copyright 2020-2021 NotNypical, <https://notnypical.github.io>.
#
# This file is part of Tabulator-QtPy, <https://github.com/notnypical/tabulator-qtpy>.
#
# Tabulator-QtPy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Tabulator-QtPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Tabulator-QtPy.  If not, see <https://www.gnu.org/licenses/>.
#

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QCheckBox, QGroupBox, QLabel, QVBoxLayout, QWidget


class PreferencesGeneralPage(QWidget):

    preferencesChanged = Signal()


    def __init__(self, parent=None):
        super().__init__(parent)

        # Title
        title = QLabel(self.tr('<strong style="font-size:large;">General</strong>'))

        # State & Geometries
        self.chkRestoreApplicationState = QCheckBox(self.tr('Save and restore the application state'))
        self.chkRestoreApplicationState.stateChanged.connect(self.onPreferencesChanged)

        self.chkRestoreApplicationGeometry = QCheckBox(self.tr('Save and restore the application geometry'))
        self.chkRestoreApplicationGeometry.stateChanged.connect(self.onPreferencesChanged)

        self.chkRestoreDialogGeometry = QCheckBox(self.tr('Save and restore dialog geometries'))
        self.chkRestoreDialogGeometry.stateChanged.connect(self.onPreferencesChanged)

        stateGeometriesLayout = QVBoxLayout()
        stateGeometriesLayout.addWidget(self.chkRestoreApplicationState)
        stateGeometriesLayout.addWidget(self.chkRestoreApplicationGeometry)
        stateGeometriesLayout.addWidget(self.chkRestoreDialogGeometry)

        stateGeometriesGroup = QGroupBox(self.tr('State && Geometries'))
        stateGeometriesGroup.setLayout(stateGeometriesLayout)

        # Main layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(title)
        self.layout.addWidget(stateGeometriesGroup)
        self.layout.addStretch()


    def setZeroMargins(self):

        self.layout.setContentsMargins(0, 0, 0, 0)


    def title(self):

        return self.tr('General')


    def onPreferencesChanged(self):

        self.preferencesChanged.emit()


    def setRestoreApplicationState(self, checked):

        self.chkRestoreApplicationState.setChecked(checked)


    def restoreApplicationState(self):

        return self.chkRestoreApplicationState.isChecked()


    def setRestoreApplicationGeometry(self, checked):

        self.chkRestoreApplicationGeometry.setChecked(checked)


    def restoreApplicationGeometry(self):

        return self.chkRestoreApplicationGeometry.isChecked()


    def setRestoreDialogGeometry(self, checked):

        self.chkRestoreDialogGeometry.setChecked(checked)


    def restoreDialogGeometry(self):

        return self.chkRestoreDialogGeometry.isChecked()
