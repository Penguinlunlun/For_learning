def add():
    print("請依序輸入兩個數字來相加:")
    print('第一個數字是?')
    number1 =int(input())
    print('第二個數字是?')
    number2 =int(input())
    number = number1 + number2
    print("你輸入的數字相加後是:", number)
    return add

add()



