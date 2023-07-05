import random
def guess_game():
    guessnumber = random.randint(1,100)
    guesstimes = 0
    print("請輸入1~100的數字:")
    while True:
        try:
            guess = int(input())
            if guess > guessnumber:
                guesstimes = guesstimes + 1
                print("太大了!")

            elif guess < guessnumber:
                guesstimes = guesstimes + 1
                print("太小了!")

            elif guess == guessnumber:
                print("恭喜你猜對了!")
                print("你總共猜了"+str(guesstimes+1)+"次")
                break

        except ValueError:
            print("請輸入整數數字!")

    print("想再玩一次嗎?(y/n)")
    if input() == "y":
        guess_game()
    else:
        print("謝謝你的遊玩!")
        exit()
    
guess_game()
