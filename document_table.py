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

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QAction, QHeaderView, QMenu, QTableWidget, QTableWidgetItem

from settings import Settings


class DocumentTable(QTableWidget):

    m_settings = Settings()


    def __init__(self, parent=None):
        super(DocumentTable, self).__init__(parent)

        self.setAttribute(Qt.WA_DeleteOnClose)

        # Creates a default document
        self.setColumnCount(self.m_settings.newDocumentColumns)
        self.setRowCount(self.m_settings.newDocumentRows)

        # Enable context menus
        hHeaderView = self.horizontalHeader()
        hHeaderView.setContextMenuPolicy(Qt.CustomContextMenu)
        hHeaderView.customContextMenuRequested.connect(self.contextMenuHorizontalHeader)

        vHeaderView = self.verticalHeader()
        vHeaderView.setContextMenuPolicy(Qt.CustomContextMenu)
        vHeaderView.customContextMenuRequested.connect(self.contextMenuVerticalHeader)


    def setSettings(self, settings):
        """
        Sets the user preferences.
        """
        self.m_settings = settings


    def createDocument(self):
        """
        Creates a document.
        """

        # Creates a new document
        self.setColumnCount(self.m_settings.newDocumentColumns)
        self.setRowCount(self.m_settings.newDocumentRows)

        # Set header items
        self.setHorizontalHeaderItems(self.m_settings.horizontalHeaderLabels)
        self.setVerticalHeaderItems(self.m_settings.verticalHeaderLabels)


    def setHorizontalHeaderItems(self, type):
        """
        Sets the horizontal header items.
        """
        for column in range(0, self.columnCount()):

            number = column

            item = QTableWidgetItem()
            item.setTextAlignment(Qt.AlignCenter)
            item.setText(self.headerItemText(number, type))

            self.setHorizontalHeaderItem(column, item)


    def setVerticalHeaderItems(self, type):
        """
        Sets the vertical header items.
        """
        for row in range(0, self.rowCount()):

            number = row

            item = QTableWidgetItem()
            item.setTextAlignment(Qt.AlignCenter)
            item.setText(self.headerItemText(number, type))

            self.setVerticalHeaderItem(row, item)


    def headerItemText(self, number, type):
        """
        Returns the header item text.
        """
        if type == 1:
            return self.numberToDecimal(number)
        elif type == 0:
            return self.numberToLetter(number)
        else:
            return ''


    def numberToDecimal(self, number):
        """
        Returns a string equivalent of the number according to the base 10.
        """
        return f'{number + 1}'


    def numberToLetter(self, number):
        """
        Returns a string equivalent of the number according to the base 26.
        """
        chars = ''
        number += 1

        while number > 0:
            number -= 1
            chars = chr(number % 26 + 65) + chars
            number //= 26

        return chars


    def contextMenuHorizontalHeader(self, pos):
        """
        Creates a context menu for the horizonzal header.
        """
        index = self.indexAt(pos)

        # Label
        actionLabelDecimal = QAction('Decimal Number', self)
        actionLabelDecimal.setStatusTip('Change label to decimal number')
        actionLabelDecimal.setToolTip('Change label to decimal number')
        actionLabelDecimal.triggered.connect( lambda: self.onActionLabelHorizontalTriggered(index.column(), 1) )

        actionLabelLetter = QAction('Letter', self)
        actionLabelLetter.setStatusTip('Change label to letter')
        actionLabelLetter.setToolTip('Change label to letter')
        actionLabelLetter.triggered.connect( lambda: self.onActionLabelHorizontalTriggered(index.column(), 0) )

        # All labels
        actionLabelAllDecimal = QAction('Decimal Numbers', self)
        actionLabelAllDecimal.setStatusTip('Change all labels to decimal numbers')
        actionLabelAllDecimal.setToolTip('Change all labels to decimal numbers')
        actionLabelAllDecimal.triggered.connect( lambda: self.onActionLabelAllHorizontalTriggered(1) )

        # Menus
        menuLabel = QMenu('Label', self)
        menuLabel.setIcon(QIcon.fromTheme('tag', QIcon(':/icons/actions/16/tag.svg')))
        menuLabel.setStatusTip('Change label')
        menuLabel.setToolTip('Change label')
        menuLabel.addAction(actionLabelDecimal)
        menuLabel.addAction(actionLabelLetter)
        menuLabel.addSeparator()
        menuLabel.addAction(actionLabelAllDecimal)

        contextMenu = QMenu(self)
        contextMenu.addMenu(menuLabel)
        contextMenu.exec_(self.mapToGlobal(pos))


    def onActionLabelHorizontalTriggered(self, column, type):
        """
        Updates a specific horizontal header item.
        """
        self.updateHorizontalHeaderItem(column, type)


    def onActionLabelAllHorizontalTriggered(self, type):
        """
        Updates all horizontal header items.
        """
        for column in range(0, self.columnCount()):
            self.updateHorizontalHeaderItem(column, type)


    def updateHorizontalHeaderItem(self, column, type):
        """
        Updates a horizontal header item.
        """
        number = column

        item = self.horizontalHeaderItem(column)
        item.setText(self.headerItemText(number, type))


    def contextMenuVerticalHeader(self, pos):
        """
        Creates a context menu for the vertical header.
        """
        index = self.indexAt(pos)

        # Label
        actionLabelDecimal = QAction('Decimal Number', self)
        actionLabelDecimal.setStatusTip('Change label to decimal number')
        actionLabelDecimal.setToolTip('Change label to decimal number')
        actionLabelDecimal.triggered.connect( lambda: self.onActionLabelVerticalTriggered(index.row(), 1) )

        actionLabelLetter = QAction('Letter', self)
        actionLabelLetter.setStatusTip('Change label to letter')
        actionLabelLetter.setToolTip('Change label to letter')
        actionLabelLetter.triggered.connect( lambda: self.onActionLabelVerticalTriggered(index.row(), 0) )

        # All labels
        actionLabelAllDecimal = QAction('Decimal Numbers', self)
        actionLabelAllDecimal.setStatusTip('Change all labels to decimal numbers')
        actionLabelAllDecimal.setToolTip('Change all labels to decimal numbers')
        actionLabelAllDecimal.triggered.connect( lambda: self.onActionLabelAllVerticalTriggered(1) )

        # Menus
        menuLabel = QMenu('Label', self)
        menuLabel.setIcon(QIcon.fromTheme('tag', QIcon(':/icons/actions/16/tag.svg')))
        menuLabel.setStatusTip('Change label')
        menuLabel.setToolTip('Change label')
        menuLabel.addAction(actionLabelDecimal)
        menuLabel.addAction(actionLabelLetter)
        menuLabel.addSeparator()
        menuLabel.addAction(actionLabelAllDecimal)

        contextMenu = QMenu(self)
        contextMenu.addMenu(menuLabel)
        contextMenu.exec_(self.mapToGlobal(pos))


    def onActionLabelVerticalTriggered(self, row, type):
        """
        Updates a specific vertical header item.
        """
        self.updateVerticalHeaderItem(row, type)


    def onActionLabelAllVerticalTriggered(self, type):
        """
        Updates all vertical header items.
        """
        for row in range(0, self.rowCount()):
            self.updateVerticalHeaderItem(row, type)


    def updateVerticalHeaderItem(self, row, type):
        """
        Updates a vertical header item.
        """
        number = row

        item = self.verticalHeaderItem(row)
        item.setText(self.headerItemText(number, type))
