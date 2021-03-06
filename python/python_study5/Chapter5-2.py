# 5-2
# ランダムな値を生成するには、「randomモジュール」を使う
# 書式は「import モジュール名」
# ※ランダムな値の事は乱数(らんすう)ともいう
#randomモジュールをインポートすると、「import モジュール関数名」でランダムな値に関する様々な機能が使える様になる。
# 「randint(ランドイント)」という関数を使うと、特定の範囲から整数のランダムな値を取得できる。
# 例えば「random.randint(0,9)」と書けば0から9までのランダムな値を取得できる。

# random.seed(a,vresion)　ランダムな値の基となる値を設定する。
# random.randint(a,b)　　　a以上b以下のランダムな整数を返す
# random.choice(seq)      の中からランダムに１つ取り出す
# random.shuffle(x)       xをランダムな順に並べ替える
# random.random           0.0以上〜1.0未満のランダムな小数値を返す


#ランダムな1桁の数を表示する
#coding : utf-8
import random #randomモジュールインポート

a = random.randint(0 , 9) #0から9までのランダムな値を作る、実行するたびに結果が変わる
print(a)

# 文字入力する
# 文字入力するにはいくつか方法があるが「input」関数を使うのが簡単
# 例えばこの様に使う　「b = input("数を入れてね>")」
# カッコの中はユーザーに表示したいメッセージ
# 画面には「数を入れてね>」と表示され、文字入力待ちの状態になる
# ユーザーが文字を入力すると、その結果がinput関数から返され、上記のbに格納される

#coding:utf-8

b = input("数を入れてね>") #ユーザーから文字を入力してもらう
print(b)                 #入力された文字を表示
#ターミナル上で入力すると確認できる

#応用
e = input("数を入れてね>") 
print(e) 

# ランダムに1桁の数字を作るプログラムで当たりかどうかを確認する簡単なゲームを作る
# if a == b:
#     print("当たり")
#else:
#     print("はずれ")
# を使用するが、「if」と「else」はインデント(字下げ)を行う

#  coding:utf-8
import random

a = random.randint(0, 9) #コンピューターが考えたランダムな値
print(a)                 #テストのために考えを見せている

b = input("数を入れてね>") #人間が入力した値
if a == b:               #等しいかを判定(実は間違い→後述)
  print("当たり")         #等しければ当たり
else:
  print("はずれ")

#↑が正しく表示されない理由は「数値」と「文字列」を比較しているから
#「random.randint(0, 9)」で作ったランダムな値は、0から9の「数値」。それに対して、「input」で入力したものは、「文字列」として認識される。
# pythonの場合「==」で「数値」と「文字列」を比較して、等しいと判断する事はない
#それには「文字列」で入力したものを一旦「数値」に変化すればいい
#その場合「int」を使う
#b = int(input("数を入れてね>"))

#coding:utf-8
import random
a = random.randint(0 , 9)
print(a)

b = int(input("数を入れてね>")) #修正箇所
if a == b:
  print("当たり")
else:
  print("はずれ")
