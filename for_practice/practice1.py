# coding:utf-8

from practice2 import MenuItem

menu_item1 = MenuItem("サンドイッチ", 500)
menu_item2 = MenuItem("チョコケーキ", 400)
menu_item3 = MenuItem("コーヒー", 300)
menu_item4 = MenuItem("オレンジジュース", 200)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

index = 0

for menu_item in menu_items:
    print(str(index) + ". " + menu_item.info())
    index += 1

print("--------------------")

order = int(input("メニューの番号を入力してください: "))

selected_menu = menu_items[order]

print("選択されたメニュー: " + selected_menu.name)
