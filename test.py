def find_max_sum(nums):
    max_sum = 0
    selected_nums = []
    
    for i in range(len(nums)):
        max_sum += max(nums[i])
        selected_nums.append(max(nums[i]))
    
    divisible_nums = [num for num in selected_nums if max_sum % num == 0]
    
    return max_sum, divisible_nums


# 讀取輸入
N, M = map(int, input().split())

nums = []
for _ in range(N):
    group = list(map(int, input().split()))
    nums.append(group)

# 呼叫函式計算最大總和與可整除的數字
max_sum, divisible_nums = find_max_sum(nums)

# 輸出結果
print(max_sum)
if divisible_nums:
    print(*divisible_nums)
else:
    print(-1)



