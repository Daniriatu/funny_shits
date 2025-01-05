import animation
import time


list = [
    "银行卡余额查询完毕",
    "支付宝余额查询完毕",
    "微信零钱余额查询完毕",
]


def main():
    input("输入您的姓名，小助手即可为您进行资产评估：")
    print("正在为您分析中，请稍后")
    for i in range(len(list)):
        analize(list[i])
    print("已查询到您是个大穷逼，再见！👋")


@animation.wait()
def analize(text):
    time.sleep(3)
    print(text)


if __name__ == "__main__":
    main()