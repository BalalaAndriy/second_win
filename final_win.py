from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton,QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton,QButtonGroup,QLineEdit, QGroupBox, QListWidget

from instr import *
from second_win import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.index = QLabel(txt_index)
        self.workheart = QLabel(txt_workheart)
        self.leyout_line = QVBoxLayout()
        self.leyout_line.addWidget(self.index, alignment = Qt.AlignCenter)
        self.leyout_line.addWidget(self.workheart, alignment = Qt.AlignCenter)
        self.setLayout(self.leyout_line)

app = QApplication([])
mw = FinalWin()
app.exec_()
        
