# 問題：
# 寫一個程式，計算一個整數列表中所有偶數的總和。

# 要求：

# 輸入：一個整數列表
# 輸出：所有偶數的總和
# 使用適當的"迴圈"和"條件"語句來實現

# 範例：
# 輸入：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 輸出：30

# 狀態: <<自解失敗 由GPT解答>>
# 學到.split()、列表推導式(new_list = [expression for item in iterable])


# 以下是自解(失敗)
while True:
    try:
        input_list = ((input("輸入一個整數列表")))
        break
    except:
        print("輸入錯誤!")

my_list = []
for i in range((len(input_list))+1,(len(input_list))-1):
    if (int(input_list[i]))&2 == 0:
        my_list.append(input_list[i])
        my_list.sort()

for b in range(len(my_list)):
    add = add + int(my_list[b])

print(add)



#以下是GPT解
while True:
    try:
        input_list = input("輸入一個整數列表（以空格分隔）: ").split()
        input_list = [int(num) for num in input_list]  # 將輸入的數字轉換成整數列表
        break
    except ValueError:
        print("輸入錯誤，請重新輸入!")

even_sum = 0
for num in input_list:
    if num % 2 == 0:  # 判斷是否為偶數
        even_sum += num

print("所有偶數的總和為:", even_sum)
