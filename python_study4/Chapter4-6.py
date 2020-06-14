# 【関数を使う】
# 関数は、いくつかの処理をひとまとめにして、ワンタッチで実行できるようにするためのもの
# 一連の処理を何度も実行する時には、処理を関数にまとめておく事で、作業が楽になる
# 
# 【関数は自分でも作れる】
# 実は、前のLesson3-5で数値を「str関数」を使ってきた
# 関数は、Pythonで用意されているもの以外に、自分で作れる
# 関数とは『何か値を受け取って、その値を加工して、内部で処理をして、結果を出すもの』
# 
# 《イメージ》
#         1と5を渡す
# 1,5 ーーーーーーーー➡️
#          引数      ⬇️
#                   関数 (1+2+3+4+5を計算)
#       　　   　　　 ⬇️      　 ｜
# 15 ⬅️ーーーーーーーーー         ｜
#         戻り値  ーーーーーーー 結果    
# 
# 
# 
# 【関数を定義するには】
# 関数を自分で作り、記述することを『関数を「定義する」と表現する』
# Pythonでは『def』と言う構文を使って定義する(define = 定義の略語)
# 関数を定義する時は、何でもいい『関数名』が必要
# 今回は「tashizan」とする
# 
# def tashizan (a, b):
#     この関数の中で実行したい処理
# 
# 書式にまとめると
# def 関数名(渡したい値をカンマで区切ったもの):
#     実行したい文が続く
# 
# 「実行したい文」はインデントして書く
# 「渡したい値をカンマで区切ったもの」は、関数で処理したい値のことで、『引数(ひきすう)』という
# 
# 《MEMO》
# 引数は、必要なだけカンマで区切って列挙する。
# 引数が必要ないなら「def 関数名():」のように、カッコの中に何も書かずに定義する
# 
# 
# では、「実行したい文」には何を書けばいいのか？
# ここでは「受け取ったaからbまでの合計を求める関数」を作る
# そのためには、for構文を使う
# 
# def tashizan(a, b):
#     total = 0
#     for i in range(a, b + 1):     # aからb
#         total = total + i         # まで繰り返す
#     return total               #結果を出す
# 
# ここでは、変数totalに計算結果を求めてる。
# 関数の結果となる値を設定するには、
# return total
# のように『return構文』を使う
# 
# return を使って結果となる値を設定することを『値を返す(返す = returnの和訳)』や
# 『値を戻す(戻す = returnの和訳)』と表現し、この値のことを『戻り値』と言う
# 
# 《COLUMN》
# 引数の実態は「変数」であり、
# 実行される時に実行した側からあらかじめ何らかの値が設定されてくる点だけ違う
# 
# 
# 【関数を利用する】
# 定義した関数は次のように使う
# 
# c = tashizan(1, 5)
# このように記述して、『関数を実行することを「関数を呼び出す(コールする)」』と言う
# 関数を呼び出す事で、変数cには「1+2+3+4+5の足し算の結果」が格納される
# 
# 結局、「tashizan(1, 5)」と書いてるので、tashizan関数が実行される
# この時の、関数定義では 「def tashizan(a, b):」と書いてるので、
# 「aには1」「bには5」が設定されている
# その状態で以下の部分が実行される
# 
# total = 0
# for i in range(a, b + 1):
#     total = total + i
# 
# この時のaは１、bは５なので
#                a  b
# for i in range(1, 5 + 1):　となる
# 
# つまり、１から５まで繰り返し実行されるのでtotal関数は、「1+2+3+4+5」の結果である「15」になる
# 最後に、
# 
# return total
# として、これを戻り値と設定してるので、その結果が、変数cに設定される
# この流れを図示すると下記の通りになる
# 
# #coding:utf-8
# def tashizan(a, b):
#     total = 0
#     for i in range(a, b + 1):
#         total = total + i
#     return total
# 
# c = tashizan(1, 5)
# print(c)
# 
# 《実行結果》
# 15
# 
# 上記の解説
# ① aに１、bに５が設定された状態で実行される
# ② 関数が実行されたtotalが1+2+3+4+5=15になる
# ③ returnしているので戻り値は15
# ④ その15が変数cに設定される
# 
# 
# 
# 【スコープを理解する】
# 関数を使う時には、大きな注意点が１つある
# それは、『関数内の変数と関数外の変数とで、保存場所が違う』と言う事
# 
# サンプルで説明
# 
# #coding:utf-8
# 
# a = "abc"                ① 変数aにabcを代入
# 
# def test():
#     print(a)  ➡️ "abc"    ③ aの参照
#     return
# 
# test()                   ② 関数実行
# print(a)      ➡️ "abc"    ④ aの参照
# 
# 
# ここでは「test」の名前で関数を作った
# 話を簡単にするため引数は無し、つまり「def test():」に記述
# また戻り値も「return」とだけ書いて「無し」にしてる
# (戻り値がない関数を実行する時は、結果を変数に代入する必要がないので、これまでのように、
# 「変数名 = 関数()」のように、「=」や「左辺に変数」を置かず、「test()」のように記述)
# 
# ①のように「a = "abc"」と記述して、変数aに「"abc"」を代入
# ②の「test()」によって、関数を実行する
# test関数の中で、③にあるように「print(a)」によって、aの値を表示
# この時の変数aの値は「"abc"」なので、画面には「abc」と表示される
# そして関数の処理が終われば④に戻ってくる。
# ここでも、「print(a)」を実行してるので「abc」と表示される
# つまり、このプログラムは変数aの値の「"abc"」を２回表示する
# ここまでは問題はない
# 
# 
# 【グローバルスコープとローカルスコープ】
# 問題はこの先です。
# test関数を、次のように修正
# 
# def test():
#     a = "def"   # 修正箇所
#     print(a)
#     return
# 
# 「a = "def"」 のように、変数aに「def」を代入した
# そうした事で、
# 
# def
# def
# と２回表示されそうですが、実際は
# 
# def
# abc
# と表示される
# なぜかは、「関数の外部」と「関数の内部」とでは、変数が作られる場所が違うから
# こうした変数の有効範囲のことを『スコープ(scope)』と言い、
# 関数の外部のことを『グローバルスコープ』、関数の内部のスコープのことを『ローカルスコープ』と言う
# そして、グローバルスコープに置いた変数のことは『グローバル変数』、
# ローカルスコープに置いた変数のことは『ローカル変数』と言う
# 
# 
# a = "abc"                 ① "abc"を代入 (グローバルスコープ) 外部
# 
# def test():
#     a = "def"             ② "def"を代入 (testのローカルスコープ) 内部
#     print(a)  ➡️ "def"     ③ aの参照 (testのローカルスコープ)　内部
#     return
# 
# test()
# print(a)  → "abc"         ④ aの参照 (グローバルスコープ) 外部
# 
# この結果から
# ①関数の内部(ローカルスコープ)から、関数の外部(グローバルスコープ)の変数を参照することはできる
# ②ただし関数の内部(ローカルスコープ)で、関数の外部(グローバルスコープ)の変数に代入することはできない
# 　そうした場合、ローカルスコープに別の変数が作られる
# 
# ローカルスコープは、関数同士がお互いに影響を与えないために大事な概念です
# もし、自分が作った関数が、その内部で関数「a」を使っているとき、他の人が作った関数が、その変数「a」を書き換えたりすると困るため
# この様な問題が発生しないように、関数のそれぞれの変数はローカルスコープで区切られていて、手出しできないようになってる
# 
# 《参考例》
# 
# グローバルスコープ
# 【a = 10】
# 
# testのローカルスコープ
# 〈a = 1〉
# 〈a = 2〉
# 〈a = 3〉
# 
# a = 10
# def test():
#     a = 1
#     return
# def test():
#     a = 2
#     return
# def test():
#     a = 3
#     return
# test()
# test2()
# test3()
# 
# 
# 【関数からグローバルスコープにアクセスする】
# しかし、関数からグローバルスコープの変数を書き換えたいこともある
# その時のために、関数内で「グローバルスコープに置かれたこの変数を使いたい」と書いておくと、
# その変数だけはグローバルスコープのものを利用できるようになる
# 
# 具体的には、次のように記述する
# 
# # coding:utf-8
# 
# a = "abc"
# 
# def test():
#     global a　　 # globalと書くとグローバル変数を使える
#     a = "def"
#     print(a)
#     return
# 
# test()
# print(a)
# 
# 
# このように「global a」と記述すると、変数aはローカルスコープではなくグローバルスコープを指すようになる
# このように、グローバルスコープに置かれた変数を利用するための記述のこと(globalと書いた行)を、
# 『グローバル宣言』という
# 
# グローバル宣言することによって、変数aはグローバルスコープの変数aを指すので、
# 関数内の「a = "def"」は、グローバルスコープの変数aを書き換えることになる
# 
# a = "abc"               ① "abc"を代入
# def test():
#     global a
#     a = "def"           ② "def"を代入　外部
#     print(a) → "def"    ③ aの参照　    外部
#     return
# 
# test()
# print(a) → "def"        ④ aの参照      外部
# 
# ①②③④のどれもグローバルスコープの変数aを指す
# 
# 
# 【可変長やオプションの引数】
# 『関数の引数は、一部を省略したり、名前を付けて指定したりできる』
# 
# ①引数の省略
# ここでは「def tashizan(a, b:」のように、引数aと引数bの２つのtashizan関数を宣言した
# こうすると、実行する際は「tashizan(1, 5」と、必ず２つの引数を指定しないと、どちらか欠けてもエラーになる
# つまり、「tashizan(1)」「tashizan(5)」のような書き方はエラーになる
# しかし、このようなエラーを出さずに、一部の引数を省略する方法は、
# 『デフォルト引数』という特殊な表記法を使うこと
# デフォルト引数は、関数定義に置いて、引数を宣言するときに、「引数名 = 省略された時の値」と記述することで作れる
# 例えば、
# 
# def tashizan(a, b = 100):
# のように定義しておくとする。この場合、２つめの引数を省略して、
# 
# tashizan(1)
# のように記述して実行できる
# 省略した時は、定義のときの値ーーつまり、この場合は「b = 100」と記述してるので「100」が指定されてる
# つまり、bの部分に「100」を指定したtashizan(1, 100)と記述したのと同義になる
# 
# 
# ②項目名を付けて指定する
# もう１つは、引数に「項目名を付けて指定する」というやり方
# そのため、関数を定義する方法は少し複雑なので、本書では触れないが、
# Chapter７でウィンドウに関する関数を使って「円を描画する」というプログラムを作る
# この関数の基本形は、
# 
# create_oval(X座標①, Y座標, X座標②, Y座標②)
# のように、「2点の座標を指定すると、それに内接する円(または楕円)が、黒色で描かれる」というのが基本動作
# しかし、この関数は、実は
# 
# create_oval(X座標①, Y座標, X座標②, Y座標②, fill = "red")
# のように「fill = "red"」を指定することで、「塗り色を赤くする」とか
# 
# create_oval(X座標①, Y座標, X座標②, Y座標②, fill = "red", width = 2)
# のように「width = 2」を指定することで、「線の幅を２にする」と言ったように、
# オプションの値を指定できるようになってる
# こうした、「項目名 = 値」という書き方は、関数に対して「追加の情報を渡したいとき」に、よく使われる
# 
# 
