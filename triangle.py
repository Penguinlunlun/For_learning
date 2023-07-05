def triangle():
    print("請輸入三個邊長來判斷三角形:")
    while True:
        try:
            a = int(input("請輸入第一邊: "))
            b = int(input("請輸入第二邊: "))
            c = int(input("請輸入第三邊: "))
            break
        except ValueError:
            print("請輸入整數數字!")
    if (a==b==c):
        print("這\"是\"正三角形")
    else:
        print("這\"不是\"三角形")

    print("需要再一次嗎?")
    if input()=="y":
        triangle()
    else:
        print("掰掰")
        exit()

triangle()

