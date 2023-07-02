
my_list = [1, 2, 3, 4, 5]
empty_list = []


#my_list[1:4] 
#表示從索引 1 開始（包含索引 1）到索引 4 結束（不包含索引 4），所以輸出的結果是 [2, 3, 4]。

#my_list[:3] 
#表示從列表的開始（索引 0）到索引 3 結束（不包含索引 3），所以輸出的結果是 [1, 2, 3]。

#my_list[2:] 
#表示從索引 2 開始（包含索引 2）到列表的結尾，所以輸出的結果是 [3, 4, 5]。
#簡單來說   (包含):(不包含)

#索引和切片：可以使用索引操作來訪問列表中的元素。
#索引從 0 開始，負數索引表示從列表末尾倒數。例如：
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # 輸出: 1
print(my_list[-1])  # 輸出: 5


#切片操作可以提取列表的一部分。
#使用冒號 : 分隔起始索引和結束索引。例如：
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])  # 輸出: [2, 3, 4]
print(my_list[:3])  # 輸出: [1, 2, 3]
print(my_list[2:])  # 輸出: [3, 4, 5]


#修改列表元素：列表中的元素是可變的，
#可以通過索引進行修改。例如：
my_list = [1, 2, 3, 4, 5]
my_list[2] = 10
print(my_list)  # 輸出: [1, 2, 10, 4, 5]



##  element==那個"值 元素" (數字等等...)
##  index==那個"位置" {[1,2,3] 的(1)=2}


#append(element):方法用於在列表的"末尾添加一個元素"。
#該元素將被追加到列表的最後。例如：
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # 輸出: [1, 2, 3, 4]


#insert(index, element):方法用於在"指定的索引位置插入一個元素"。
#你需要指定要插入元素的索引和該元素的值。
# 插入操作將在指定索引之前將新元素插入列表中。例如：
my_list = [1, 2, 3]
my_list.insert(1, 'a')
print(my_list)  # 輸出: [1, 'a', 2, 3]


#pop(index):方法用於"刪除並記得指定索引位置的元素"。
#它將從列表中刪除該元素並返回記得它的值。
#如果不指定索引，則 pop 方法將刪除並返回列表的最後一個元素。例如：
my_list = [1, 2, 3]
popped_element = my_list.pop(1)
print(popped_element)  # 輸出: 2
print(my_list)  # 輸出: [1, 3]


#clear():方法用於清空列表中的所有元素，使列表變為空列表。
#它將移除所有的內容，讓列表長度變為 0。例如：
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # 輸出: []





#"連接"列表：
#使用 "+" 運算符可以將兩個列表連接在一起，創建一個新的列表。
list1 = [1, 2, 3]
list2 = [4, 5, 6]
new_list = list1 + list2
print(new_list)  # 輸出: [1, 2, 3, 4, 5, 6]


#"重複"列表：
#使用 "*" 運算符可以將列表重複指定的次數。
list1 = [1, 2, 3]
new_list = list1 * 3
print(new_list)  # 輸出: [1, 2, 3, 1, 2, 3, 1, 2, 3]


#"排序"列表：
#使用 sort() 方法可以對列表進行"升序"排序。
my_list = [3, 1, 4, 2]
my_list.sort()
print(my_list)  # 輸出: [1, 2, 3, 4]


#len() 函數
#返回列表中元素的"個數"。
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print(length)  # 輸出: 5


#max() 函數
#返回列表中的"最大值"。
my_list = [1, 2, 3, 4, 5]
maximum = max(my_list)
print(maximum)  # 輸出: 5


#min() 函數
#返回列表中的最小值。
my_list = [1, 2, 3, 4, 5]
minimum = min(my_list)
print(minimum)  # 輸出: 1





#也可以用for xxx in list
my_list = [1, 2, 3, 4, 5]
for element in my_list:
    print(element)
#輸出:
#1
#2
#3
#4
#5