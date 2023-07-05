import time
import sys

def update_progress(progress):
    bar_length = 50
    filled_length = int(bar_length * progress)
    bar = '=' * filled_length + '-' * (bar_length - filled_length)
    percentage = int(progress * 100)
    sys.stdout.write(f'\r[{bar}] {percentage}%')
    sys.stdout.flush()

# 模擬進度更新
total_iterations = 100
for i in range(total_iterations + 1):
    progress = i / total_iterations
    update_progress(progress)
    time.sleep(0.1)




