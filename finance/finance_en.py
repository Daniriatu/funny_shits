import animation
import time


list = [
    "Paypal account balance checked",
    "Bank account balance checked",
    "Credit card debt checked",
]


def main():
    input("Tell me your name and I can help you with your finance situation: ")
    print("Analyzing...")
    for i in range(len(list)):
        analize(list[i])
    print("We don't deal with broke loser, you're on you own. Bye! 👋")


@animation.wait()
def analize(text):
    time.sleep(3)
    print(text)


if __name__ == "__main__":
    main()