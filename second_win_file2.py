from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton,QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QGroupBox, QListWidget
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont

from instr import*
#from my_app import*
from final_win import*

class Experiment():
    def __init__(self, age, test1,test2,test3):
        self.age = edit2
        self.t1 = edit3
        self.t2 = edit4
        self.t3 = edit5

class TestWin(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.show()
        self.connects()

    def initUI(self):
        self.lab1=QLabel(txt_lab1)
        self.edit1 = QLineEdit(txt_edit1)
        self.lab2 = QLabel(txt_lab2)
        self.edit2= QLineEdit(txt_edit2)
        self.lab3 = QLabel(txt_lab3)
        self.butt1 = QPushButton(txt_butt1)
        self.edit3  =QLineEdit(txt_edit3)
        self.lab4 = QLabel(txt_lab4)
        self.butt2 = QPushButton(txt_butt2)
        self.lab5 = QLabel(txt_lab5)
        self.text_timer = QLabel(txt_timer)
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.butt3 = QPushButton(txt_butt3)
        self.edit4 = QLineEdit(txt_edit4)
        self.edit5 = QLineEdit(txt_edit5)
        self.butt4 = QPushButton(txt_butt4)
        #self.lab6 = QLabel(txt_lab6)
         

        self.h_line=QHBoxLayout()
        self.r_line=QVBoxLayout()
        self.l_line=QVBoxLayout()
        self.r_line.addWidget(self.text_timer,alignment=Qt.AlignRight)
        self.l_line.addWidget(self.lab1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.edit1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.lab2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.edit2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.lab3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.butt1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.edit3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.lab4,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.butt2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.lab5,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.butt3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.edit4,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.edit5,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.butt4,alignment=Qt.AlignCenter)
        #self.r_line.addWidget(self.lab6,alignment=Qt.AlignRight)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.age, self.t1, self.t2, self.t3)
        self.fw=FinalWin(self.exp)

    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):    
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString('hh:mm:ss') == "00:00:00":
            self.timer.stop()
        
    def timer_sits(self):
        global time
        time = QTime(0,0,30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss')[6:8])
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString('hh:mm:ss') == "00:00:00":
            self.timer.stop()
        
    def timer_final(self):
        global time 
        time =QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString('hh:mm:ss')[6:8]) >= 45:
            self.text_timer.setStyleSheet('color: rgb(0,255,0)')
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.text_timer.setStyleSheet('color: rgb(0,255,0)')
        else:
            self.text_timer.setStyleSheet('color rgb(0,0,0)')
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))    
        if time.toString('hh:mm:ss') == "00:00:00":
            self.timer.stop()

    def connects(self):
        self.butt4.clicked.connect(self.next_click)
        self.butt1.clicked.connect(self.timer_test)
        self.butt2.clicked.connect(self.timer_sits)
        self.butt3.clicked.connect(self.timer_final)
