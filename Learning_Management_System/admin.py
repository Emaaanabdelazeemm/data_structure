import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
import csv

# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSignal






class Admin(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #F9F8FD;")
        self.UiComponents()

    def UiComponents(self):
        self.title = QLabel("Admins", self)
        self.title.setFont(QFont("Protest Riot", 25))
        self.title.setStyleSheet(" color: rgba(63,71,105)")
        self.title.setGeometry(40, 40, 300, 100)

        self.searchbar = QLineEdit(self)
        self.searchbar.setPlaceholderText("Search")

        self.searchbar.setStyleSheet(
            "border-radius : 10px; background-color: #EDE1F7; color: black; padding-left: 55px ; padding-right:30px ;font-size: 15px"
        )
        self.searchbar.setGeometry(600, 75, 280, 40)

        # search icon
        search_label = QLabel(self)
        pixmap = QPixmap("images/icons8-search-30.png")
        search_label.setPixmap(pixmap)
        search_label.move(620, 78)
        search_label.resize(30, 30)
        search_label.setStyleSheet("background-color: transparent;")

        box = QLabel(self)

        box.setGeometry(30, 250, 870, 300)
        box.setStyleSheet("background-color:#F4F4FE; border-radius : 15px;")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor("#BD80C5"))
        box.setGraphicsEffect(shadow)

        pic6 = QPixmap("images/for_admin.png")
        pic6_label = QLabel(box)
        pic6_label.setPixmap(pic6.scaled(200, 200))
        pic6_label.move(10, 10)
        self.content_label1 = QLabel(
            "Manage the data by exporting and importing\nCSV files from here!", box
        )
        self.content_label1.setFont(QFont("Protest Riot"))
        self.content_label1.setStyleSheet(
            "font-size: 25px; color:black ;padding-left:25px;"
        )
        self.content_label1.setAlignment(Qt.AlignCenter)
        self.content_label1.move(210, 50)

        self.exporting_csv = QPushButton("Export", box)
        self.importing_csv = QPushButton("Import", box)
        self.importing_csv.setGeometry(250, 170, 150, 40)
        self.exporting_csv.setGeometry(500, 170, 150, 40)
        self.exporting_csv.setCursor(Qt.PointingHandCursor)
        self.importing_csv.setCursor(Qt.PointingHandCursor)
        self.exporting_csv.setStyleSheet(
            "border-radius : 15px; background-color:#492971 ;"
        )
        self.importing_csv.setStyleSheet(
            """
                                border-radius: 15px;
                                background-color: #5558AC;
                                color: white;
                            }
                            QPushButton:hover {
                                background-color: #393984;
                            }
                            """
        )
        self.exporting_csv.setStyleSheet(
            """
                                border-radius: 15px;
                                background-color: #5558AC;
                                color: white;
                            }
                            QPushButton:hover {
                                background-color: #393984;
                            }
                            """
        )
        self.importing_csv.setFont(QFont("Arial", 15))
        self.exporting_csv.setFont(QFont("Arial", 15))
        self.importing_csv.clicked.connect(self.open_file_dialog)

        headertabel = QTableWidget(self)
        headertabel.setColumnCount(3)
        headertabel.setRowCount(1)
        headertabel.setItem(0, 0, QTableWidgetItem("Admin ID"))
        headertabel.setItem(0, 1, QTableWidgetItem("Admin Name"))
        headertabel.setItem(0, 2, QTableWidgetItem("Admin Username"))

        headertabel.setFont(QFont("Times", 14))
        headertabel.setGeometry(30, 630, 870, 50)

        headertabel.setStyleSheet(
            "QTableWidget { border: 0px; color:black  ; background-color:#F4F4FE  ; border-radius : 15px;padding-left:20px;padding-top:7px;selection-background-color: #EDE1F7; selection-color: black}"
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor("#BD80C5"))
        headertabel.setGraphicsEffect(shadow)
        headertabel.horizontalHeader().setVisible(False)
        headertabel.verticalHeader().setVisible(False)
        headertabel.setShowGrid(False)
        headertabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        tableWidget = QTableWidget(self)
        tableWidget.setRowCount(5)
        tableWidget.setColumnCount(3)
        tableWidget.setItem(0, 0, QTableWidgetItem("11067"))
        tableWidget.setItem(0, 1, QTableWidgetItem("Shahd Ahmed Ragab"))
        tableWidget.setItem(1, 0, QTableWidgetItem("14675"))
        tableWidget.setItem(1, 1, QTableWidgetItem("Hassnaa hussam"))
        tableWidget.setItem(2, 0, QTableWidgetItem("14789"))
        tableWidget.setItem(2, 1, QTableWidgetItem("Ayat Tarek"))
        tableWidget.setItem(3, 0, QTableWidgetItem("10923"))
        tableWidget.setItem(3, 1, QTableWidgetItem("Eman Abd El-Azeem"))

        tableWidget.setItem(0, 2, QTableWidgetItem("shahdd"))
        tableWidget.setItem(1, 2, QTableWidgetItem("hasnaa4"))
        tableWidget.setItem(2, 2, QTableWidgetItem("Ayatt"))
        tableWidget.setItem(3, 2, QTableWidgetItem("Eman304"))

        tableWidget.setFont(QFont("Times", 12))
        tableWidget.horizontalHeader().setVisible(False)
        tableWidget.verticalHeader().setVisible(False)
        tableWidget.setShowGrid(False)

        # Table will fit the screen horizontally
        tableWidget.setGeometry(30, 700, 870, 200)
        tableWidget.setStyleSheet(
            "QTableWidget { border: 0px; background-color:#F4F4FE; color: black ; border-radius : 15px;padding-left:20px;padding-top:7px;selection-background-color: #EDE1F7; selection-color: black}"
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor("#BD80C5"))
        tableWidget.setGraphicsEffect(shadow)
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter(
            "All Files (*.*)"
        )  # You can set specific file filters here
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            for file_path in selected_files:
                # Process the selected file
                self.process_file(file_path)

                for row in file_path:
                    print(row)

    def process_file(self, file_path):
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                file_path.append(row)
        return file_path
