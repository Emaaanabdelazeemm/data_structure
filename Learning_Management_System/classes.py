from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QPushButton,
    QLineEdit,
    QApplication,
    QLabel,
)
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys

# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Classes(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Classes Page", self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

        # more Font
        QFontDatabase.addApplicationFont("./ProtestRiot-Regular.ttf")
        QFontDatabase.addApplicationFont("./Exo2-Regular.ttf")
        QFontDatabase.addApplicationFont("./Exo2-SemiBold.ttf")
        self.setWindowTitle("Classes ")
        self.setStyleSheet("background-color:  #5558AC; border-radius:40px;")
        self.UiComponents()

    def UiComponents(self):
        # back ground
        back_ground = QLabel(self)
        back_ground.setStyleSheet("background-color: #F9F8FD; border-radius:30px;")
        back_ground.setGeometry(0, 0, 1640, 950)

        self.showAddedCourse("Data Structures & Algorithms", "CMP 2210", 40, 355)
        self.showAddedCourse("Database", "CMP 2242", 40, 470)
        self.showAddedCourse("Chemistry", "CHE 1241", 40, 585)
        self.showAddedCourse("Circuits", "EPE 1241", 40, 700)
        self.showAddedCourse("OOP Principles", "CMP 1242", 40, 815)

        self.showAddedCourse("Linear Algebra", "MTH 1242", 850, 355)
        self.showAddedCourse("Elctronics", "ELC 2242", 850, 470)
        self.showAddedCourse("Bio-Measurements", "SBE 2230", 850, 585)
        self.showAddedCourse("Bio-Statistics", "SBE 2240", 850, 700)
        self.showAddedCourse("Fluids & Thermo Dynamics", "MEC 102", 850, 815)

        self.hello("Hassnaa")

        # # the side bar
        # side_bar = QLabel(self)
        # side_bar.setStyleSheet("background-color: #5558AC; ")
        # side_bar.setGeometry(0, 0, 300, 1000)

        # courses word label
        courses_label = QLabel(self)
        courses_label.setText("Courses")
        courses_label.setFont(QFont("Protest Riot", 25))
        courses_label.setStyleSheet("color: rgba(63,71,105); background-color:#F9F8FD")
        courses_label.resize(500, 60)
        courses_label.move(40, 270)
        courses_label.setBold = True

        # search textbox
        searchBox = QLineEdit(self)
        searchBox.setPlaceholderText("Search")
        searchBox.setFont(QFont("Arial", 12))
        searchBox.setGeometry(1210, 95, 280, 40)
        searchBox.setStyleSheet(
            "border-radius : 10px; background-color: #EDE1F7; color: black; padding-left: 55px"
        )

        # search icon
        search_label = QLabel(self)
        pixmap = QPixmap("images/icons8-search-30.png")
        search_label.setPixmap(pixmap)
        search_label.move(1225, 100)
        search_label.resize(30, 30)
        search_label.setStyleSheet("background-color: transparent;")

        # number of courses
        num_label = QLabel(self)
        num_label.setText("Courses \ncompleted")
        num_label.setFont(QFont("Arial", 14))
        num_label.move(910, 160)
        num_label.resize(280, 120)
        num_label.setStyleSheet(
            "border-radius : 10px; background-color: #EDE1F7;padding-left:125px;"
        )
        num10_label = QLabel(self)
        num10_label.setText("10")
        num10_label.setFont(QFont("Protest Riot", 60))
        num10_label.move(930, 160)
        num10_label.resize(120, 100)
        num10_label.setStyleSheet("background-color: transparent;")

        # courses in progress
        inprogress_label = QLabel(self)
        inprogress_label.setText("Courses \nin progress")
        inprogress_label.setFont(QFont("Arial", 14))
        inprogress_label.move(1210, 160)
        inprogress_label.resize(280, 120)
        inprogress_label.setStyleSheet(
            "border-radius : 10px; background-color: #EDE1F7; padding-left:125px;"
        )
        num4_label = QLabel(self)
        num4_label.setText("4")
        num4_label.setFont(QFont("Protest Riot", 60))
        num4_label.move(1250, 160)
        num4_label.resize(120, 100)
        num4_label.setStyleSheet("background-color: transparent;")

    def showAddedCourse(self, name, code, x, y):
        # rectangle of course
        course_rect = QLabel(self)
        course_rect.setStyleSheet("background-color: #F4F4FE; border-radius : 15px; ")
        course_rect.resize(640, 90)
        course_rect.move(x, y)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor("#BD80C5"))
        course_rect.setGraphicsEffect(shadow)

        # course name
        course_name = QLabel(self)
        course_name.setText(f"{name}\n")
        course_name.setFont(QFont("Exo2", 15))
        course_name.setStyleSheet("background-color: transparent; ")
        course_name.resize(400, 50)
        course_name.move(x + 20, y + 17)
        course_name.setBold = True

        # course code
        course_code = QLabel(self)
        course_code.setText(f"{code}\n")
        course_code.setFont(QFont("Exo2", 10))
        course_code.setStyleSheet("background-color: transparent; ")
        course_code.resize(100, 50)
        course_code.move(x + 20, y + 51)

        # view course button
        view_btn = QPushButton(self)
        view_btn.setText(" View Course")
        view_btn.setFont(QFont("Exo2", 12))
        view_btn.setStyleSheet(
            " QPushButton::hover"
            "{"
            "background-color : #393984;"
            "};background-color: #5558AC; border-radius : 15px; padding: 10px; color:white;  "
        )
        view_btn.resize(160, 50)
        view_btn.move(x + 420, y + 20)
        view_btn.setCursor(Qt.PointingHandCursor)

        match code:
            case "CMP 2210":
                self.code1 = "CMP 2210"
                view_btn.clicked.connect(self.showCourse1)
            case "CMP 2242":
                self.code2 = "CMP 2242"
                view_btn.clicked.connect(self.showCourse2)
            case "CHE 1241":
                view_btn.clicked.connect(self.showCourse3)
            case "EPE 1241":
                view_btn.clicked.connect(self.showCourse4)
            case "CMP 1242":
                view_btn.clicked.connect(self.showCourse5)
            case "MTH 1242":
                view_btn.clicked.connect(self.showCourse6)
            case "ELC 2242":
                view_btn.clicked.connect(self.showCourse7)
            case "SBE 2230":
                view_btn.clicked.connect(self.showCourse8)
            case "SBE 2240":
                view_btn.clicked.connect(self.showCourse9)
            case "MEC 102":
                view_btn.clicked.connect(self.showCourse10)
        # view_btn.clicked.connect(self.showCourse)

    def showCourse1(self):
        # dialog appear when button is clicked
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(800, 500)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        # tabel contains basic info
        info_tabel = QTableWidget(self)
        info_tabel.resize(600, 800)
        info_tabel.move(500, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6)
        # tabel content
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        info_tabel.setItem(5, 0, QTableWidgetItem("Students"))
        info_tabel.setItem(5, 1, QTableWidgetItem("Grade"))
        info_tabel.setItem(0, 1, QTableWidgetItem("Data Structures & Algorithms"))
        info_tabel.setItem(1, 1, QTableWidgetItem("CMP 2210"))
        info_tabel.setItem(2, 1, QTableWidgetItem("3201"))
        info_tabel.setItem(3, 1, QTableWidgetItem("10 Am"))
        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            " background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        # adding tabel to dialog
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse2(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(800, 500)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(600, 800)
        info_tabel.move(500, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6)
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        info_tabel.setItem(5, 0, QTableWidgetItem("Students"))
        info_tabel.setItem(5, 1, QTableWidgetItem("Grade"))
        info_tabel.setItem(0, 1, QTableWidgetItem("Database"))
        info_tabel.setItem(1, 1, QTableWidgetItem("CMP 2242"))
        info_tabel.setItem(2, 1, QTableWidgetItem("14200"))
        info_tabel.setItem(3, 1, QTableWidgetItem("8 Am"))
        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse3(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(800, 500)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(600, 800)
        info_tabel.move(500, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6)
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        info_tabel.setItem(5, 0, QTableWidgetItem("Students"))
        info_tabel.setItem(5, 1, QTableWidgetItem("Grade"))
        info_tabel.setItem(0, 1, QTableWidgetItem("Chemistry"))
        info_tabel.setItem(1, 1, QTableWidgetItem("CHE 1241"))
        info_tabel.setItem(2, 1, QTableWidgetItem("17102"))
        info_tabel.setItem(3, 1, QTableWidgetItem("12 pm"))
        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse4(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(800, 500)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(600, 800)
        info_tabel.move(500, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6)
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        info_tabel.setItem(5, 0, QTableWidgetItem("Students"))
        info_tabel.setItem(5, 1, QTableWidgetItem("Grade"))
        info_tabel.setItem(0, 1, QTableWidgetItem("Circuits"))
        info_tabel.setItem(1, 1, QTableWidgetItem("EPE 1241"))
        info_tabel.setItem(2, 1, QTableWidgetItem("1125"))
        info_tabel.setItem(3, 1, QTableWidgetItem("1 pm"))
        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse5(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(800, 500)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(600, 800)
        info_tabel.move(500, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6)
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        info_tabel.setItem(5, 0, QTableWidgetItem("Students"))
        info_tabel.setItem(5, 1, QTableWidgetItem("Grade"))
        info_tabel.setItem(0, 1, QTableWidgetItem("OOP Principles"))
        info_tabel.setItem(1, 1, QTableWidgetItem("CMP 1242"))
        info_tabel.setItem(2, 1, QTableWidgetItem("3102"))
        info_tabel.setItem(3, 1, QTableWidgetItem("8 Am"))
        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse6(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(800, 500)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(600, 800)
        info_tabel.move(500, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6)
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        info_tabel.setItem(5, 0, QTableWidgetItem("Students"))
        info_tabel.setItem(5, 1, QTableWidgetItem("Grade"))
        info_tabel.setItem(0, 1, QTableWidgetItem("Linear Algebra"))
        info_tabel.setItem(1, 1, QTableWidgetItem("MTH 1242"))
        info_tabel.setItem(2, 1, QTableWidgetItem("3202"))
        info_tabel.setItem(3, 1, QTableWidgetItem("10 Am"))
        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse7(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(800, 500)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(600, 800)
        info_tabel.move(500, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6)
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        info_tabel.setItem(5, 0, QTableWidgetItem("Students"))
        info_tabel.setItem(5, 1, QTableWidgetItem("Grade"))
        info_tabel.setItem(0, 1, QTableWidgetItem("Elctronics"))
        info_tabel.setItem(1, 1, QTableWidgetItem("ELC 2242"))
        info_tabel.setItem(2, 1, QTableWidgetItem("3201"))
        info_tabel.setItem(3, 1, QTableWidgetItem("10:30 Am"))
        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse8(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(800, 500)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(600, 800)
        info_tabel.move(500, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6)
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        info_tabel.setItem(5, 0, QTableWidgetItem("Students"))
        info_tabel.setItem(5, 1, QTableWidgetItem("Grade"))
        info_tabel.setItem(0, 1, QTableWidgetItem("Bio-Measurements"))
        info_tabel.setItem(1, 1, QTableWidgetItem("SBE 2230"))
        info_tabel.setItem(2, 1, QTableWidgetItem("1204"))
        info_tabel.setItem(3, 1, QTableWidgetItem("12 pm"))
        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse9(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(800, 500)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(600, 800)
        info_tabel.move(500, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6)
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        info_tabel.setItem(5, 0, QTableWidgetItem("Students"))
        info_tabel.setItem(5, 1, QTableWidgetItem("Grade"))
        info_tabel.setItem(0, 1, QTableWidgetItem("Bio-Statistics"))
        info_tabel.setItem(1, 1, QTableWidgetItem("SBE 2240"))
        info_tabel.setItem(2, 1, QTableWidgetItem("3103"))
        info_tabel.setItem(3, 1, QTableWidgetItem("2 pm"))
        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse10(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(800, 500)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(600, 800)
        info_tabel.move(500, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6)
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        info_tabel.setItem(5, 0, QTableWidgetItem("Students"))
        info_tabel.setItem(5, 1, QTableWidgetItem("Grade"))
        info_tabel.setItem(0, 1, QTableWidgetItem("Fluids & Thermo Dynamics"))
        info_tabel.setItem(1, 1, QTableWidgetItem("MEC 102"))
        info_tabel.setItem(2, 1, QTableWidgetItem("17102"))
        info_tabel.setItem(3, 1, QTableWidgetItem("8 Am"))
        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def hello(self, name):
        # hello label
        hello_label = QLabel(self)
        hello_label.resize(800, 150)
        hello_label.setStyleSheet(
            "background-color: #EDE1F7; border-radius:20px; padding-left:25px; padding-top:15px  "
        )
        hello_label.move(40, 95)
        hello_label.setText(f"Hello {name}!\n")
        hello_label.setFont(QFont("Protest Riot", 28))

        # It's good to see you again label
        label2 = QLabel(self)
        label2.resize(300, 150)
        label2.move(40, 123)
        label2.setText(" It's good to see you again.")
        label2.setFont(QFont("Protest Riot", 14))
        label2.setStyleSheet(
            "background-color: transparent; border-radius:20px; padding-left:25px;margin-top:0px ;"
        )

        # image label
        img_label = QLabel(self)
        img_label.resize(200, 210)
        img_label.move(510, 35)
        img_label.setStyleSheet(
            "background-color: transparent; margin:0px; padding:0px"
        )
        pixmap = QPixmap("images/student1.png")
        img_label.setPixmap(pixmap)





