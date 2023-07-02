'''def bigger():
    while True:
        try:
            print('輸入兩個整數數字比大小')
            a = int(input("請輸入第一個數字"))
            b = int(input("請輸入第二個數字"))
            c = int(input("請輸入第三個數字"))
            max = a
            if (b>max):
                max = b 
            elif (c>max):
                max = c
            break

        except ValueError:
            print("請輸入整數數字!")
    if (max==a==b==c):
        print("三數相同")
    else:
        print("最大的數字是"+str(max))

    print("需要再一次嗎?")
    if input()=="y":
        bigger()
    else:
        print("掰掰")
        exit()'''

def bigger():
    while True:
        try:
            print('輸入兩個整數數字比大小')
            a = int(input("請輸入第一個數字"))
            b = int(input("請輸入第二個數字"))
            c = int(input("請輸入第三個數字"))
            break
        except ValueError:
            print("請輸入整數數字!")
    
    abc_list = [a,b,c]
    abc_list.sort()
    maxabc = max(abc_list)
    print("最大的數字是"+str(maxabc))

bigger()