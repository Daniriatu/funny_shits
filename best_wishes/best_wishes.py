import turtle
import random
import time

# 设置屏幕
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("2025 祝大家财源广进！")
screen.setup(width=800, height=600)
screen.tracer(0)  # 关闭自动刷新

# 创建画笔
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# 显示祝福文字
def draw_message():
    pen.penup()
    pen.goto(-10, -50)
    pen.color("red")
    pen.write("2025 新年快乐！\n财源滚滚来！！！", align="center", font=("Arial", 68, "bold"))

# 掉落的¥符号类
class FallingYen:
    def __init__(self):
        self.symbol = turtle.Turtle()
        self.symbol.hideturtle()
        self.symbol.penup()
        self.symbol.color("gold")
        self.symbol.goto(random.randint(-380, 380), random.randint(10, 800))
        self.symbol.write("💰", align="center", font=("Arial", 32, "bold"))
        self.y_position = self.symbol.ycor()
        self.speed = random.uniform(10, 15)

    def move(self):
        self.symbol.clear()
        self.y_position -= self.speed
        if self.y_position < -300:  # 如果¥掉到屏幕外，重置到顶部
            self.y_position = random.randint(100, 300)
            self.symbol.goto(random.randint(-380, 380), self.y_position)
        self.symbol.goto(self.symbol.xcor(), self.y_position)
        self.symbol.write("💰", align="center", font=("Arial", 32, "bold"))

# 创建多个¥符号
yen_symbols = [FallingYen() for _ in range(100)]

# 绘制祝福文字
draw_message()

# 动画主循环
while True:
    for yen in yen_symbols:
        yen.move()
    screen.update()  # 刷新屏幕
    time.sleep(0.03)  # 控制动画速度
