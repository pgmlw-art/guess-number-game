print("主人！！！")
print("这是一个猜数字游戏~")
print("我会在心里默念一个1~1000的数字\n而主人需要猜出这个数是多少~")
print("让我们开始吧！")
import random
随机数=random.randint(1,1000)
第一次猜=True
while True:
    if 第一次猜:
        提问="猜猜看~"
        第一次猜=False
    else:
        提问="再猜猜呢~"


    while True:
        c=input(提问)
        try:
            猜测=int(c)
            break
        except ValueError:
            print("请输入数字哦~")

    if 随机数>猜测:
        print("小了")

    elif 随机数<猜测:
        print("大了")

    else:
        print("答对啦！")
        break
