
#有,=有元組
a = 1,2,3
#不管有沒有()也算是一組元組


# 創建元組
my_tuple = (1, 2, 3, 'a', 'b', 'c')

# 訪問元組元素
print(my_tuple[0])   # 輸出: 1
print(my_tuple[-1])  # 輸出: 'c'

# 元組是不可變的，無法修改元素
# my_tuple[0] = 10  # 這將引發 TypeError

# 元組的操作
print(len(my_tuple))                  # 輸出: 6
print(my_tuple + (4, 5, 6))           # 輸出: (1, 2, 3, 'a', 'b', 'c', 4, 5, 6)
print(my_tuple * 2)                   # 輸出: (1, 2, 3, 'a', 'b', 'c', 1, 2, 3, 'a', 'b', 'c')

print('a' in my_tuple)                # 輸出: True
print(('a', 'b') in my_tuple)          # 輸出: False
print((('a', 'b'),) in my_tuple)    # 輸出: True



# 元組的解包
a, b, c, d, e, f = my_tuple
print(a, b, c, d, e, f)  # 輸出: 1 2 3 'a' 'b' 'c'

#解包搭配函式
def get_user_info():
    name = "John"
    age = 25
    email = "john@example.com"
    return name, age, email

# 調用函數並將返回的值進行解包
user_name, user_age, user_email = get_user_info()

# 使用解包後的值
print("Name:", user_name)
print("Age:", user_age)
print("Email:", user_email)