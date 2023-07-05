def menu():
    print("帳號、密碼管理系統")
    print("=========================")
    print("1. 輸入帳號、密碼")
    print("2. 顯示帳號、密碼")
    print("3. 修  改  密  碼")
    print("4. 刪除帳號、密碼")
    print("0. 結  束  程  式")
    print("=========================")


import os 
def read_data():
    if not os.path.exists('password.txt'):
        return dict()
    try:
        with open('password.txt','r',encoding = 'UTF-8') as r:
            final_data = r.read()
            if final_data != '':
                final_data = eval(final_data)
                return final_data
            else:
                return dict()
            
    except FileNotFoundError:
        print("找不到 password.txt 檔案")
        return dict()
    except Exception as e:
        print("讀取資料時發生錯誤:", str(e))
        return dict()
         

def input_data():
    global final_data
    while True:
        account = input("請輸入帳號(enter確認)")
        if account == "":
            print("你沒輸入!")
            print()
            continue
        if account in final_data:
            print(f"{account}此帳號已存在")
            continue
        else:
            break
    
    password = input("請輸入密碼")
    final_data[account]=password
    with open('password.txt','w',encoding = 'UTF-8') as w:
        w.write(str(final_data))
    print(f"{account}以存入完畢")
    print()


def show_data():
    global final_data
    final_data = read_data()
    print("帳號\t密碼")             
    print("================")
    if not final_data:
        print("目前沒有任何帳號和密碼")
        print()
    else:
        for key in final_data:
            pass_star =  "*" * len(final_data[key])
            print(f"{key}\t{pass_star}")
    input("按任意鍵返回主選單")
    print()


def fix_data():
    global final_data
    while True:
        fix_accont = input("請輸入要修改的帳號(enter確認)")
        if fix_accont == "":
            print("你沒輸入!")
            print()
            continue
        if not fix_accont in final_data:
            print(f"沒有此\"{fix_accont}\"帳號")
            continue
        else:
            break
    print(f"請輸入{fix_accont}原來的密碼")
    old_password = input()

    if final_data[fix_accont]== old_password:
        new_password = input("認證通過,請輸入新密碼")
        final_data[fix_accont] = new_password

        with open('password.txt','w',encoding = 'UTF-8') as f:
            f.write(str(final_data))
        input("修改完畢 按任意鍵返回主選單")
        print()
    else:
        print("認證失敗！原密碼不正確。")
        print()
        input("按任意鍵返回主選單")
        print()

def del_data():
    global final_data
    while True:
        del_accont = input("請輸入要刪除的帳號(enter確認)")
        if del_accont == "":
            print("你沒輸入")
            print()
            continue
        if not del_accont in final_data:
            print(f"沒有{del_accont}這個帳號")
            print()
            continue
        else:
            break
    print(f"確認刪除{del_accont}這個帳號?")
    an = input("(y/n)?")
    if an == "y" or "Y":
        del final_data[del_accont]
        with open("password.txt","w",encoding= "UTF-8") as d:
            d.write(str(final_data))
            input("刪除完畢 按任意鍵返回主選單")
            print()
    elif an == "n" or "N":
        print('請重新考慮')
        print()
    
    else:
        print("無效字元")
        print()
    
def clear():
    global final_data
    origin_pass = "5226"
    an = input("輸入管理員密碼")
    if an == origin_pass:
        anyn = input("確定要刪除所有內容嗎？(y/n): ")
        if anyn.lower() == "y":
            with open('password.txt', 'w', encoding='UTF-8') as f:
                f.write("")
            print("已刪除所有內容")
        else:
            print("取消刪除")
    else:
        print("輸入錯誤")
    print()



final_data = read_data()
final_data = dict()

while True:
    try:
        menu()
        choice = int(input("請輸入編號來選擇："))
        print()

        if choice==1:
            input_data()

        elif choice==2:
            show_data()

        elif choice==3:
            fix_data()

        elif choice==4:
            del_data()
        
        elif choice==88:
            clear()

        else:
            break    
    except:
        print("數字拉!!@")
        print()
        input("按任意鍵返回主選單")
        print()
 
print("掰掰~!")