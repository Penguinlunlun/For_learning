# 請寫一個程式，接收用戶輸入的整數列表（以空格分隔），計算列表中所有數字的平均值並輸出結果。
# 範例：
# 輸入：3 5 7 9 2
# 輸出：平均值為 5.2

# 狀態 : <<自行解出來>>
while True:
    try:
        in_list = input("輸入數個整數求平均（以空格分隔）").split()
        in_list = [int(num) for num in in_list]
        break
    except:
        print("輸入錯誤!")

final_num = 0
for num in in_list:
    final_num += num
print("平均值為",(final_num) / (len(in_list)) )




