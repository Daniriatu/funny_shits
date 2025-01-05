from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QDate, QTimer


def handle_clicked():
    QProgressBar().show()
    QMessageBox().about(window, "result", "你的人生关键期是一辈子！")
        
    
    
app = QApplication()
timer = QTimer()

window = QMainWindow()
window.setWindowTitle("人生关键期计算器")
window.resize(300, 400)
window.move(500, 310)

title = QLabel("人生关键期计算器", window)
title.resize(181, 51)
title.move(60, 50)
title.setStyleSheet("font-size: 20px")
title.setAlignment(Qt.AlignHCenter)
title.setAlignment(Qt.AlignVCenter)

label_1 = QLabel("出生日期", window)
label_1.resize(65, 21)
label_1.move(110, 120)
label_1.setStyleSheet("font-size: 16px")
label_1.setAlignment(Qt.AlignHCenter)
label_1.setAlignment(Qt.AlignVCenter)

date = QDateEdit(window)
date.move(100, 150)
date.setDate(QDate.currentDate())  # 设置默认日期为今天
date.setReadOnly(False)           # 确保可以编辑
date.setDisplayFormat("yyyy-MM-dd")

label_2 = QLabel("性别", window)
label_2.resize(65, 21)
label_2.move(120, 200)
label_2.setStyleSheet("font-size: 16px")
label_2.setAlignment(Qt.AlignHCenter)
label_2.setAlignment(Qt.AlignVCenter)

male = QRadioButton("男", window)
male.resize(41, 20)
male.move(70, 230)

female = QRadioButton("女", window)
female.resize(41, 20)
female.move(120, 230)

unknown = QRadioButton("未知", window)
unknown.resize(51, 20)
unknown.move(170, 230)

progress_bar = QProgressBar()
progress_bar.move(100, 270)
progress_bar.setMinimum(0)
progress_bar.setMaximum(100)
progress_bar.setValue(0)
progress_bar.setVisible(False)

button = QPushButton("开始计算",window)
button.move(95, 290)
button.clicked.connect(handle_clicked)

window.show()
app.exec()