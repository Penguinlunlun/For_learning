def ma99():
    while True:
        fu = input("請輸入你要的運算\"符號\"(+,-,*,/)")
        if fu == ("+"):
            a,b = answer()
            print("答案是:"+str(a+b))
            break

        elif fu == ("-"):
            a,b = answer()
            print("答案是:"+str(a-b))
            break                 

        elif fu == ("*"):
            a,b = answer()
            print("答案是:"+str(a*b))
            break

        elif fu == ("/"):
            a,b = answer()
            if b != 0:
                print("答案是：" + str(a / b))
                break
            else:
                print("除數不能為零")
                break

        else:
            print("無效的運算符號")
            continue
        
        retr()
        


def answer():
    a = int(input("第一個數字"))
    b = int(input("第二個數字"))
    return a,b


def retr():
    while True:
        yn = input("想要再一次嗎？(y/n)")

        if yn =="y":
            ma99()
        elif yn =="n":
            print("感謝使用")
            exit()
        else:
            print("請輸入y或n")

ma99()
