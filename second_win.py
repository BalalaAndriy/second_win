from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton,QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QGroupBox, QListWidget

from instr import*
from final_win import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.connects()
        self.show()

    def initUI(self):
        self.hintname=QLabel(txt_hintname)
        self.name = QLineEdit(txt_name)
        self.hintage = QLabel(txt_hintage)
        self.age= QLineEdit(txt_age)
        self.test1 = QLabel(txt_test1)
        self.starttest1 = QPushButton(txt_starttest1)
        self.hinttest1 = QLineEdit(txt_hinttest1)
        self.test2 = QLabel(txt_test2)
        self.starttest2 = QPushButton(txt_starttest2)
        self.test3 = QLabel(txt_test3)
        self.starttest3 = QPushButton(txt_starttest3)
        self.hinttest2 = QLineEdit(txt_hinttest2)
        self.hinttest3 = QLineEdit(txt_hinttest3)
        self.sendresults = QPushButton(txt_sendresults)
        self.timer = QLabel(txt_timer)
        
        self.h_line=QHBoxLayout()
        self.r_line=QVBoxLayout()
        self.l_line=QVBoxLayout()
        self.l_line.addWidget(self.hintname,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.name, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.hintage,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.age,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.test1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.starttest1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.hinttest1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.test2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.starttest2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.test3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.starttest3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.hinttest2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.hinttest3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.sendresults,alignment=Qt.AlignCenter)
        self.r_line.addWidget(self.timer,alignment=Qt.AlignRight)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    
    def next_click(self):
        self.mw =FinalWin()
        self.hide()
    
    def connects(self):
        self.sendresults.clicked.connect(self.next_click)
