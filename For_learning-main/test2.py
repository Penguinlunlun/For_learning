list = [('apple', 25), ('orange', 10), ('fig', 12), ('apricot', 20)]

#用def來定義
def by_name(item):
    return item[0]
def by_name_len(fu):
    return len(fu[0])
def by_price(fi):
    return fi[1]
    
print(sorted(list, key=by_name))          #關鍵字參數key指定
print(sorted(list, key=by_name_len))  
print(sorted(list, key=by_price))