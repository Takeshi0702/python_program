#【プログラミングをブロック化して１つの機能を与える】
# 前のLessonでは、ディクショナリとリストを使って、複数の円を描画するプログラムを作りました。
# これには実は、別解がある。それはクラスとオブジェクトを使う方法です。
# 
# 【プログラムをブロック化して１つの機能を与える】
# 前のLessonで作った、「ディクショナリ」と「リスト」を使って、円の座標や移動方向、描画色などのテータを管理して、それを１つずつループ処理して描画する方法は、昔からある古典的な手法である
# それに対して最近は、プログラムを部品化(コンポーネント化)して、様々な操作を実現する方法が、よく採らる
# 今回の例でいうと、１つ１つの「円」を部品として扱う
# 内部で自分の状態 (今回の例で言えば、「座標や移動方向」「描画色」)を保持している
# 部品は、外部から様々な「命令」を受け付けるように作っておく
# 例えば、「動かす」とか「消す」といった命令を受け付けられるようにしておく
# プログラムは、そうした命令を実行することで、部品をコントロールしていく
# ここで言う部品こそが「オブジェクト」で、その命令は「メソッド」に相当する
# 「これまで作ってきたプログラム」と「オブジェクトを使ったプログラム」の考え方の違いを次の図7-8-1に示した
# 大きな違いは「データをどこで管理するか」という点にある
# これまで作ってきたプロブラムでは、データがディクショナリやリストでひとまとまりにして管理されていたのに対し、オブジェクトを使ったプログラムの場合は、それぞれのオブジェクトがデータを持っており、それに対して命令を出すようにプログラミングしてる
# 
# 図7-8-1 オブジェクト側にプログラムがあり、外部からはそれに対して命令を与えるだけ
# 《これまでのプログラム》
# ・データ
#  balls = [
#    {"x" : 400, "y" : 300, "dx" : 1, "dy" : 1, "color" : "red"},
#    {"x" : 200, "y" : 100, "dx" : -1, "dy" : 1, "color" : "green"},
#    {"x" : 100, "y" : 200, "dx" : 1, "dy" : -1, "color" : "blue"}
#]
#                              ｜ 
#                              ｜ 
#                              ｜
#              　　　　　　　　　 ｜  (データをひとつずつ読んで処理していく)
# ・プログラム                　　|
#  for b in balls:             ｜
#    今の円を消す                ⬇️
#    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill = "white", width = 0)
#    X座標を動かす
#    x = x + dx
#    Y座標も動かす
#    y = y + dy
#    次の位置に円を描く
#    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill = "red", width = 0) 
# 
# 《オブジェクトを使ったプログラム》
#   for b balls:                               ↗️ 動かすプログラム(関数・メソッド) Ballオブジェクト
#     #動かす   ーーーーーーーーーーーーーーーーーーー➡　動かすプログラム(関数・メソッド) Ballオブジェクト
#     b.動かす()                 ⬆️          　　↘️ 動かすプログラム(関数・メソッド) Ballオブジェクト
#               プログラムでは「動かす」と命令するだけ                ⬆️
#                                                        　　　　⬆️
#                     canvas.create_ovalメソッドの実行など、消したり描画したりするプログラムは、オブジェクト側に備わるようにする

# 【オブジェクトはクラスから作る】 
# 実はオブジェクトはプログラマが記述するのもではない。プログラマが記述するのは、オブジェクトの基となる「クラス(class)」と呼ばれるものである
# オブジェクトを使いたい場合、プログラマは、クラスというものをプログラムとして記述しておく
# このようにしておいて、オブジェクトを使いたい時は、Pythonの特定の文法(後で説明)を使って、クラスからオブジェクトを作り出します
# こうして作ったオブジェクトのことを「インスタンス(instance)」という
# そして、クラスからオブジェクトを作り出す操作のことを、「実体化する」とか「インスタンスを作る」と言う
# 図7-8-2にも示したように、クラスとオブジェクトは、１対多数の関係です
# クラスを作成しておけば、そのクラスを基としたオブジェクトを、いくつでも作れる
# 
# 図7-8-2
#              インスタンスを作る操作                 
#          　　　　　 　　⬇️　　　　↗️  オブジェクト
#        クラス ーーーーーーーーーー▶️　 オブジェクト
#          ⬆️                   ↘️ 　オブジェクト
#   プログラマが書くのがこれ
# 
# 【クラスでデータを管理する】
# クラスとオブジェクトの話はとても難しいので、順を追って説明する
# 最終的には、円を動かすオブジェクトを作っていくので、ひとまず「動かす」と言うことは忘れて、ここでは円の座標や移動量、色を管理するデータについて考える
# 
# 《クラスを作る》
# 前Lessonでディクショナリとリストを使ったプログラムの例から分かるように、１つの円は以下５つのデータを持っている
# 「x座標、y座標、xの移動量、yの移動量、色」

#そこでまずは、この5種類のデータをオブジェクト内部で管理できるようにし、そのためのクラスを記述する。 
# クラス名は、何でも構いませんが、ここでは仮に「ball」という名前にする。Pythonでクラスを作る場合は、次のような書式で記述する
# 
# class クラス名：
#     クラスの定義内容

# ここでは、次のようにBallクラスを作る
# class Ball:
#   def_init_(self, x, y, dx,dy, color):
#   self.x = x
#   self.y = y
#   self.dx = dx
#   self.dy = dy
#   self.color = color

# ここで定義した「_init_」と言うのは、最初にオブジェクトを作る時に呼び出される特殊な関数で「コンストラクタ(constructor)」と呼ばれる
# コンストラクタは、オブジェクトの状態を、最初の状態にするときの処理をするのに使う

# 《クラスからオブジェクトを作る》
# このようにBallクラスを作った時、このクラスからオブジェクト(Ballオブジェクト)を作るには、次のように記述する。
# このようにすると、Ballオブジェクトができ、変数bに代入される(変数bは任意の名称であり、どのような変数でも構わない)

# b = Ball(400, 300, 1, 1, "red")
# このとき内部では、コンストラクタ(クラス内に記述した(init)と言う名前の関数)が実行され一連の処理が実行される
# この結果、Ballオブジェクトの中には「x」「y」「dx」「dy」「color」という名前の変数ができ、そのに引数に渡された値が代入される
# このようにオブジェクトの内部にある変数を「インスタンス変数」と呼ぶ
# 
# 《自身を示すself》
# さて「_init_」について、もう少し詳しく見る。defで定義されているように、これは関数ですが、普通の関数とクラスの内部で定義した関数とでは、大きな違いが１つある
# それは、「１つめの引数は、「オブジェクトを指す特別な変数である」」と言う点
# いま提示した例では、_init_関数を以下のように定義した
# 
# def_init_(self, x, y, dx, dy, color):
# この先頭の「「self」は、「オブジェクト」を指し示す」と言う約束になっている
# 以降、このクラスには他のいくつかのメソッドを作っていくことになるが、「先頭の引数は、いつも操作対象のオブジェクトが渡される」という点は共通です
# このようにして渡されたselfに対して「self.x」や「self.y」のように、「.」でつなげて任意の変数名を記述すると、それを変数として使える
# このようなオブジェクトの内部の変数のことを「インスタンス変数」と言う
# 《MEMO》関数の１つめの引数は、慣例的にselfと言う名前が使われますが、self以外の名前でも構わない。たとえば、「def_init_(s, x, y, dx, dy, color):」のように定義しても構わない
# この場合、インスタンス変数を参照するための書式は、「s.x」や「s.y」のようになる

# 【メソッドを実装する】
# このように「_init_」関数を使って、「self変数名」に値を代入することで、そのオブジェクトに任意のデータを保存して管理できるようになる
# 次に、このオブジェクトに、命令を与えることができる「メソッド(method)」を作っていく
# 最終的には「円を動かす」というメソッドを実装することになるが、最初からは難しいので、簡単なtestと言うメソッドを実装していく
# メソッドはクラス内部で定義された関数に過ぎない
# たとえば、次のようにtestメソッドを記述する

# class Ball:
#     def_init_(self, x, y, dx, dy, color):
#         self.x = x
#         self.y = y
#         self.dx = dx
#         self.dy = dy
#         self.color = color
#     def test(self)            # testメソッド
#         print(self.x)         # testメソッド
#         print(self.y)         # testメソッド

# ここで実装したtestメソッドは、
# def test(self)
#     print(self.x)
#     print(self.y)
# のようにした。これは、「self.x」と「self.y」を表示するだけのもの
# ここで、
# b = Ball(400, 300, 1, 1, "red")
# として、Ballオブジェクトを作ったとする
# この場合「self.x」は「400」、「self.y」は「300」になっている
# なので、以下を実行すると画面には「400」「300」と表示される
# b.test()
# 図7-8-4(P218)

# 【円を動かすメソッドを作る】
# ここまでの説明を踏まえて、「円を動かす」と言うプログラムをクラスとオブジェクトを使って実装してみる
# まずは「１つの円を動かす」というプログラムを示す。
# 動かす処理は、Ballクラスのmoveメソッドに記述
# 
# 《円をオブジェクトとして作り、動かす》
# プログラムでは、まず、次のように、Ballオブジェクトを作っている。
# ここでは変数bに代入した

# b = Ball(400, 300, 1, ,1 "red")
# 定期的にタイマーで起動するloop関数を次のように定義した(タイマー：P196参照)

# def loop():
# 動かす
# b.move(canvas)
# もう一回
# root.after(10, loop)
# 0.01秒(10ミリ秒)後に、このloop関数が実行されるように、次のようにしてタイマー登録している
# root.after(10, move)

# 【動かす操作】
# 上記のroop関数では

# b.move(canvas)
# と言うように、変数bが指しているBallオブジェクトのmoveメソッドを実行している
# moveメソッドは、次のように定義している
# 
# def move(self, canvas)
# 最初の引数は、このオブジェクトを示すことは説明済み。
# ２番目の引数は、実行されるときに渡した値(ここではb.move(canvas)としてmoveメソッドを実行しているので、このときに渡したcanvas)です
# moveメソッドではまず、円を白色で描画することで消している。
# 対象の座標は、「self.x」と「self.y」です
# canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill = "white", width = 0)

# 描画が済んだら、X座標とY座標を次の位置に移動する
# X座標、Y座標を動かす
# self.x = self.x + self.dx
# self.y = self.y + self.dy
# この処理の後、端に当たった時は移動方向を反転させると言うプログラムが続くが、ここでの説明は割愛する
# 
# 【オブジェクトに対して命令を出すことで動かす】
# プログラムは、少し難しいのですが、注目したいことは、
# b.move()
# のように、オブジェクトを代入した変数に対して、moveと言うメソッドを実行するだけで動かしていると言う点です
# moveメソッドで「どんな処理を実行するのか」は、オブジェクト(の基となるクラス)に書かれており、「オブジェクトを使っている側」からは、完全なブラックボックスです(図7-8-5：P220)
# 言い換えると、このBallと言うオブジェクトを「使っている側」は、「moveメソッドを実行すると円が動く」と言う事実だけを知っており、「どうやって動かしているのか」と言う「動かし方」は知りません
# 実際の動かし方はオブジェクトの内部に隠れるため、全体のプログラムがスッキリし、見やすくなる


# coding:utf-8
import tkinter as tk

class Ball:                                     # Ballクラスの定義
    def __init__(self, x, y, dx, dy, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color

    def move(self, canvas):                     # 円を動かすためのメソッド
    # 今の円を消す
        canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill = "white", width = 0)
        # X座標、Y座標をを動かす
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        # 次の位置に円を描く
        canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill = self.color, width = 0)
        # 端を超えていたら反対向きにする
        if self.x >= canvas.winfo_width():           
          self.dx = -1                               
        if self.x <= 0:                              
          self.dx = +1                               
        if self.y >= canvas.winfo_height():          
          self.dy = -1                               
        if self.y <= 0:                              
          self.dy = +1                               

# 円をひとつ作る
b = Ball(400, 300, 1, 1, "red")                  # Ballオブジェクトを作る

def loop():
  # 動かす
  b.move(canvas)                                 # 「動かす」と命令するだけ
  # もう一回
  root.after(10,loop)

# ウィンドウを描く
root = tk.Tk()
root.geometry("800x600")

# キャンバスを置く
canvas =tk.Canvas(root, width = 800, height = 600, bg = "white")
canvas.place(x = 0, y = 0)

# タイマーをセット
root.after(10, loop) 

root.mainloop()
# 
# 
# 【たくさんの円を動かす】
# 上記では、１つの円しか動かしていないが、これを複数にするのは、とても簡単
# リストとしてBallオブジェクトを用意する
# 
# balls = [
#     Ball(400, 300, 1, 1, "red"),
#     Ball(200, 100, -1, 1, "green"),    ２つ加えた
#     Ball(100, 200, 1, -1, "blue")      ２つ加えた
# ]
# 用意したら、これらのリストをforでループして処理するため、円を動かすloop関数を次のように修正する
# 
# def loop():
#     #動かす
#     for b in balls:           ballsから１つずつ取り出す
#         b.move(canvas)        「動かせと命令する」
# 
#     #もう一回 
#       root.after(10, loop)
# このようにオブジェクトをリストとして構成すれば、いくつでも好きなだけ円を描ける
# 修正が必要なのはデータのところだけで、クラスなどのプログラムを変更する必要はない
# 
# 




