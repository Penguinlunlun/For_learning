def total():
    num = int(input("請輸入人數:"))
    pay = num*300
    if pay >= 3000:
        pay = pay * 0.8
        print("總金額為:",int(pay))
    elif pay <3000:
        pay = pay
        print("總金額為:",pay)

total()
 