
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
import csv

# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Students(QWidget):
    def __init__(self):
        super().__init__()
        self.UiComponents()

        self.setWindowTitle("Students ")

        self.setStyleSheet("background-color: #F9F8FD;")

    def UiComponents(self):
        # for corners
        # pinkLabel = QLabel(self)
        # pinkLabel.setStyleSheet("border-radius : 50px; background-color: white;")
        # pinkLabel.setGeometry(0, 8, 1200, 975)

        pinkLabel2 = QLabel(self)
        pinkLabel2.setStyleSheet("border-radius : 50px; background-color: #F4F4FE;")
        pinkLabel2.setGeometry(1100, 8, 550, 975)

        # student word label
        studentWordLabel = QLabel(self)
        studentWordLabel.setText("Students")
        studentWordLabel.setFont(QFont("Protest Riot", 25))
        studentWordLabel.setStyleSheet(
            "background-color: transparent; color: rgba(63,71,105);"
        )
        studentWordLabel.setGeometry(40, 40, 400, 60)
        studentWordLabel.setBold = True

        # statistic word label
        statisticWordLabel = QLabel(self)
        statisticWordLabel.setText("Statistics")
        statisticWordLabel.setFont(QFont("Protest Riot", 25))
        statisticWordLabel.setStyleSheet(
            "background-color: transparent;  color: rgba(63,71,105);"
        )
        statisticWordLabel.setGeometry(1250, 40, 400, 60)
        statisticWordLabel.setBold = True

        # the two buttons label above
        btLabel = QLabel(self)
        btLabel.setStyleSheet("border-radius : 10px; background-color: #B67ADC;")
        btLabel.setGeometry(900, 130, 105, 40)

        self.filter = QPushButton(self)
        self.filter.setFont(QFont("Protest Riot", 15))
        self.filter.resize(32, 32)
        self.filter.move(915, 135)
        self.filter.setStyleSheet(
            " QPushButton::hover"
            "{"
            "background-color : #50336D;"
            "};border-radius : 10px;background-color:#7A51A1 ;color:white; bold"
        )
        self.filter.setCursor(Qt.PointingHandCursor)
        self.icon = QIcon(
            "icons8-filter-50.jpg"
        )  # Replace 'icon.png' with the path to your icon file
        self.filter.setIcon(self.icon)
        # self.filter.clicked(self.go_to_anotherWindow())

        self.list = QPushButton(self)
        self.list.setFont(QFont("Protest Riot", 15))
        self.list.resize(32, 32)
        self.list.move(960, 135)
        self.list.setStyleSheet(
            "border-radius : 10px;background-color: #7A51A1 ;color:white; bold"
        )
        self.list.setCursor(Qt.PointingHandCursor)
        self.icon = QIcon(
            "icons8-list-30.jpg"
        )  # Replace 'icon.png' with the path to your icon file
        self.list.setIcon(self.icon)

        # add student button
        addStudent = QPushButton(self)
        addStudent.setText("Add Student")
        addStudent.setFont(QFont("Exo2", 11))
        addStudent.setGeometry(750, 130, 120, 40)
        addStudent.setStyleSheet(
            " QPushButton::hover"
            "{"
            "background-color : #7A51A1;"
            "};border-radius : 10px; background-color: #B67ADC; color: white;"
        )
        addStudent.setCursor(Qt.PointingHandCursor)

        # search textbox
        searchBox = QLineEdit(self)
        searchBox.setPlaceholderText("Search")
        searchBox.setFont(QFont("Arial", 12))
        searchBox.move(620, 405)
        searchBox.setGeometry(750, 70, 280, 40)
        searchBox.setStyleSheet(
            "border-radius : 10px; background-color: #EDE1F7; color: black; padding-left: 55px"
        )
        # search icon
        search_label = QLabel(self)
        pixmap = QPixmap("images/icons8-search-30.png")
        search_label.setPixmap(pixmap)
        search_label.move(765, 75)
        search_label.resize(30, 30)
        search_label.setStyleSheet("background-color: transparent;")

        # the table
        headertabel = QTableWidget(self)
        headertabel.setColumnCount(4)
        headertabel.setRowCount(1)
        headertabel.setItem(0, 0, QTableWidgetItem("Student ID"))
        headertabel.setItem(0, 1, QTableWidgetItem("Student Name"))
        headertabel.setItem(0, 2, QTableWidgetItem("Student Year"))
        headertabel.setItem(0, 3, QTableWidgetItem("Student Department"))
        headertabel.resizeRowToContents(4)
        headertabel.setFont(QFont("Exo2", 14))
        headertabel.setGeometry(40, 250, 1010, 46)
        headertabel.setStyleSheet(
            "QTableWidget { border: 0px; background-color: #F4F4FE; color: #536e8f; border-radius : 20px;padding-left:15px;selection-background-color: #EDE1F7; selection-color: black}"
        )
        headertabel.horizontalHeader().setVisible(False)
        headertabel.verticalHeader().setVisible(False)
        headertabel.setShowGrid(False)
        headertabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        headertabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor("#BD80C5"))
        headertabel.setGraphicsEffect(shadow)

        tableWidget = QTableWidget(self)
        tableWidget.setRowCount(5)
        tableWidget.setColumnCount(4)
        tableWidget.setItem(0, 0, QTableWidgetItem("11067"))
        tableWidget.setItem(0, 1, QTableWidgetItem("Shahd Ahmed Ragab"))
        tableWidget.setItem(1, 0, QTableWidgetItem("14675"))
        tableWidget.setItem(1, 1, QTableWidgetItem("Hassnaa hussam"))
        tableWidget.setItem(2, 0, QTableWidgetItem("14789"))
        tableWidget.setItem(2, 1, QTableWidgetItem("Ayat Tarek"))
        tableWidget.setItem(3, 0, QTableWidgetItem("10923"))
        tableWidget.setItem(3, 1, QTableWidgetItem("Eman Abd El-Azeem"))

        tableWidget.setItem(0, 2, QTableWidgetItem("second"))
        tableWidget.setItem(1, 2, QTableWidgetItem("third"))
        tableWidget.setItem(2, 2, QTableWidgetItem("first"))
        tableWidget.setItem(3, 2, QTableWidgetItem("fourth"))
        tableWidget.setItem(0, 3, QTableWidgetItem("SBE"))
        tableWidget.setItem(2, 3, QTableWidgetItem("ARC"))
        tableWidget.setItem(1, 3, QTableWidgetItem("CMP"))
        tableWidget.setItem(3, 3, QTableWidgetItem("CVE"))
        tableWidget.resizeColumnToContents(10)
        tableWidget.resizeColumnToContents(5)

        tableWidget.setFont(QFont("Times", 12))
        tableWidget.horizontalHeader().setVisible(False)
        tableWidget.verticalHeader().setVisible(False)
        tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        tableWidget.setShowGrid(False)

        # Table will fit the screen horizontally
        tableWidget.setGeometry(40, 310, 1010, 600)
        tableWidget.setStyleSheet(
            "QTableWidget { border: 0px; background-color: #F4F4FE; color: #536e8f; border-radius : 15px;padding-left:15px;selection-background-color: #EDE1F7; selection-color: black}"
        )
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor("#BD80C5"))
        tableWidget.setGraphicsEffect(shadow)


# def go_to_anotherWindow(self):

# self.addstudent = AddStudent()
# self.addstudent.show()
# self.hide()


