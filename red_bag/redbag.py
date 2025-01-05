from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMessageBox
from PySide6.QtCore import Qt
import random

click_count = 0


def btn1_clicked():
  QMessageBox.about(window, "好消息", "恭喜您获得了0.1元红包")


def btn2_clicked():
    global click_count
    move_button_randomly()
    print(click_count)

# 按钮移动逻辑
def move_button_randomly():
    global click_count
    if click_count < 5:  # 限制移动次数
        # 随机生成新位置
        x = random.randint(50, 300)
        y = random.randint(20, 280)
        button_two.move(x, y)
        click_count += 1
    else:
        # 显示消息框
        QMessageBox.about(window, "谢谢你", "既然你这么坚持, 那就请给我一百元红包吧")
        button_two.move(210, 160)
        click_count = 0


app = QApplication()

window = QMainWindow()
window.setWindowTitle("新年大红包")
window.resize(400, 300)
window.move(500, 310)

title = QLabel("请选择红包金额", window)
title.resize(191, 51)
title.move(110, 70)
title.setStyleSheet(
  """
  font-size: 25px;
  font-weight: bold;
"""
)
title.setAlignment(Qt.AlignHCenter)
title.setAlignment(Qt.AlignVCenter)

button_one = QPushButton("0.1元", window)
button_one.move(70, 160)
button_one.setObjectName("btn1")  # 设置按钮的 objectName
button_one.setStyleSheet("""
    #btn1 {
        background-color: green;
        color: white;
        font-size: 16px;
        border: none
    }
    #btn1:hover {
        background-color: green;  /* 鼠标悬停时的背景色 */
        color: white;  /* 鼠标悬停时字体颜色 */
        font-size: 18px;  /* 悬停时字体变大 */
    }
""")
button_one.clicked.connect(btn1_clicked)

button_two = QPushButton("100元",window)
button_two.move(210, 160)
button_two.setObjectName("btn2")  # 设置按钮的 objectName
button_two.setStyleSheet("""
    #btn2 {
        background-color: red;
        color: white;
        font-size: 16px;
        border: none
    }
    #btn2:hover {
        background-color: red;  /* 鼠标悬停时的背景色 */
        color: white;  /* 鼠标悬停时字体颜色 */
        font-size: 18px;  /* 悬停时字体变大 */
    }
""")
button_two.clicked.connect(btn2_clicked)

window.show()
app.exec()