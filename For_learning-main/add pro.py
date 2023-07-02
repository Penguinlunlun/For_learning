def add_numbers(number1, number2):
    add = number1 + number2
    return add


print("請依序輸入兩個數字來相加:")
while True:
    try:
        inputnum1 =int(input("第一個數字是?"))
        inputnum2 =int(input("第二個數字是?"))
        break
    except ValueError:
        print("請輸入整數數字!")

    except TypeError:
        print("輸入錯誤!")

sum = int(add_numbers(inputnum1,inputnum2))
print('你輸入的數字相加後是:'+str(sum))
