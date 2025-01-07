from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMessageBox
from PySide6.QtCore import Qt
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("新年大红包")
        self.resize(400, 300)
        self.move(600, 310)
        
        self.click_count = 0
        
        self.title = QLabel("请选择红包金额", self)
        self.title.resize(191, 51)
        self.title.move(110, 70)
        self.title.setStyleSheet("""
            font-size: 25px;
            font-weight: bold;
        """)
        self.title.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.btn_one = self.create_btn("0.1元", 70, 160, "btn1", "green", self.btn1_clicked)
        self.btn_two = self.create_btn("100元", 210, 160, "btn2", "red", self.btn2_clicked)


    def create_btn(self, text, pos_x, pos_y, selector, color, callback=None):
        btn = QPushButton(text, self)
        btn.move(pos_x, pos_y)
        btn.setObjectName(selector)
        btn.setStyleSheet(f"""
            #{selector} {{  
                background-color: {color};
                color: white;
                font-size: 16px;
                border: none;
            }} 
            
            #{selector}:hover {{  
                background-color: {color};
                color: white;
                font-size: 18px;
                border: none;
            }}
        """)
        btn.clicked.connect(callback)
        return btn
    
    
    def btn1_clicked(self):
        QMessageBox.about(self, "好消息", "恭喜您获得了0.1元红包")
        
        
    def btn2_clicked(self):
        if self.click_count < 5:
            random_x = random.randint(50, 300)
            random_y = random.randint(20, 280)
            self.btn_two.move(random_x, random_y)
            self.click_count += 1
        else:
            QMessageBox.about(window, "谢谢你", "既然你这么坚持, 那就请给我一百元红包吧")
            self.btn_two.move(210, 160)
            self.click_count = 0


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()