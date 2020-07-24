# 【条件分岐する/if構文】
# プログラミングで複雑な動作をさせるには、
# 「もし、このようなときには、こうする、そうでなければ、こうする」と言うような条件分岐が不可欠
# (繰り返し実行できると、長いプログラムも短く書く事ができる)
# (条件分岐を理解すれば、もっと複雑なプログラムも書けるようになる)
# 
# 
# 【条件分岐】
# Pythonでは、次の書式のif構文を記述すると、条件分岐できる
# 
# 「書式」 if構文の条件分岐
# if 条件文：
#     条件が成り立っているときに実行する文
# else:
#     条件が成り立っていないときに実行する文
# 
# ※ else: が不要であれば、if条件文だけで記述できる
# 条件分岐も『インデントして記述』する。そうしないとErrorになる
# 
# 例) 全体で10回繰り返し、「aが5以下」の時は「小さいです」、それ以外は「大きいです」と表示させる
# 
# # coding:utf-8
# for a in range(1, 11):
#     if a <= 5:
#       print("小さいです")
#     else:
#       print("大きいです")
# 
# 
# 《実行結果》
# 小さいです
# 小さいです
# 小さいです
# 小さいです
# 小さいです
# 大きいです
# 大きいです
# 大きいです
# 大きいです
# 大きいです
# 
# 
# 『別回答』
# # coding:utf-8
# for a in range(10):
#     if a + 1 <= 5:
#       print("小さいです")
#     else:
#       print("大きいです")
# 
# 「range(10)」にまとめて「a + 1」にして簡単にした（P92参照）
# 
# 
# 【条件を組み合わせる】
# 指定できる条件は、１つではなく組み合わせることもできる。
# 条件を組み合わせる時は、「and」「or」、そして「not」を使う
# こうした組み合わせを『倫理演算子』と言う
# 
# 《倫理演算子表》
# and   ２つの条件の両方が成り立つ時       (a == 1) and (b == 2)   aが1で、かつ、bが2の時
# or    ２つの条件のいずれかが成り立つ時　　(a == 1) or (b == 2)　 　aが1、もしくは、bが2の時
# not   条件の否定                      not (a == 2)            aが2と等しくない時(a! = 2と書くのと同じ)
# 
# 
# 《COLUMN》【重要】
# Pythonでは「and」を省略できる
# 「1以上、5以下であるか」を調べるには、普通は
# if (a >= 1) and (a <= 5):
# と記述するが、Pythonでは
# if 1 <= a <= 5:
# と省略して書く事ができる。
# ただし、省略できるのはPythonだけで他の言語では許されない
# 
# 
# 実際に、条件を組み合わせたプログラムを作ってみる
# 今回は１から１０までを繰り返し実行し、
# ・２の倍数の時は「○」
# ・２の倍数の時は「×」
# ・２の倍数かつ３の倍数の時は「△」
#   と表記する
# 
# # coding:utf-8
# for a in range(1, 11):      他には、「for a in range(1, 10 + 1):」とも書ける
#     print(a)
#     if a % 2 == 0:
#         print("○")
#     if a % 3 == 0:
#         print("×")
#     if (a % 2 == 0) and (a % 3 == 0):
#         print("△")
# 
# 「倍数の時は」という条件は以下のように記述する
# if a % 2 == 0:    (２の倍数の時は)
# 
# 【重要】
# 「%」は余りを計算する演算子
# 「余りが０」なら、「その倍数である」とみなしている
# Pythonには「倍数かどうか」を調べる命令は存在しない
# しかし、それと同じ意味になるように「割ったときに、余りが０かどうか」と考え、
# Pythonでできる書き方に変更することでプログラミングができる
# プログラミングするときは、
# 『プログラミングとして表現できる、同じ意味での考え方の置き換え』は常にあるので、
# 「頭をちょっとひねる」事が必要になる
# 
# 「２の倍数」かつ「３の倍数」の場合は、andを使って、以下のように表現しました
# if (a % 2 == 0) and (a % 3 == 0):
# 
# 
# 【elifを使って「ではない時の条件」を並べる】
# 場合によっては、「ではない」時に、別の条件を指定したい事がある
# 
# ①12の倍数のときは「○」と表示する
# ②①でなく４の倍数の時は「△」と表示する
# ③①でも②でもなく２の倍数の時は「×」と表示する
# ④上記のどれでもないときは「☆」と表示する
# 　この処理は、次のように記述できる
# 
# if (a % 12 == 0):
#   # ①12の倍数のとき
#   print("○")
# else:
#   # ②12の倍数ではないとき
#   if (a % 4 == 0):
#     # ②４の倍数のとき
#     print("△")
#   else:
#     if (a % 2 == 0):
#       # ③２の倍数のとき
#       print("×")
#     else:
#       # ④どれでもないとき
#       print("☆")
# 
# このプログラミングは、「if」「else」がとても多く、一目でどのような処理をしてるかわからない
# 実はPythonには「else」と「if」を合体した『elif』がある
# 
# if (a % 12 == 0):
#   # ①12の倍数のとき
#   print("○")
# elif (a % 4 == 0):
#   # ②４の倍数のとき
#   print("△")
# elif if (a % 2 == 0):
#   # ③２の倍数のとき
#   print("×")
# else:
#   # ④どれでもないとき
#   print("☆")
# 
# 『elifは、「そうではないときは」を列挙したい時によく使われる表記方法』
# これを使う事で行数を減らせ、スッキリと書ける
# 
# 
# 【条件が成り立ったときに繰り返しをやめる・『break』を使う】
# if文を使った条件判断は、for や while などの繰り返し構文と組み合わせることもよくある
# つまり、「何度か繰り返すのだけれども、特定の条件が成り立ったときには、繰り返しをやめたい」と言うパターンです
# for構文や while構文では、構文の内部で『break』と言う特別な命令を実行すると、その時点で繰り返しをやめ、次の表記に移動する
# 
# 例）「1+2+3+4+••••」と足して行って、50を超えたらその時の答えを表示する
# 
# total = 0
# a = 1
# while total <= 50:      # 「total <= 50」 50以下の時に繰り返す
#     total = total + a
#     a = a + 1
# print(total)
# 
# 《実行結果》
# 55
# 
# 
# 他には『break』を使って、下記のように記述できる
# 
# total = 0
# a = 1
# while True:             #「while True」 永遠に切り返す
#     total = total + a
#     a = a + 1
#     if total > 50:      # 50を超えたら
#       break             # 繰返しをやめる 
# print(total)
# 
# 《実行結果》
# 55
# 
# 
# 「while True」と記述して、永遠を繰り返すようにした。
# その中で、変数aの値を1,2,••••と増やしながら、変数totalに加えていく。そして、
# if tptal > 50:
#     break
# の条件によって、total変数の内容が50を超えた時は、breakを実行する
# この結果、whileのループから抜け出し、「print(total)」が実行され、プログラムが終了する
# 
# breakを使って処理を終了する例は、
# 「ユーザーに何か文字入力してもらうときに、特定の文字の並び(例えば「数字だけ」といった制約)でない時は、
# ずっと「正しい文字の並びで入力されるまで繰り返し入力させる」と言うような場合」
# 
# 《COLUMN》
# 『何もしないことを示すpass』
# if文では、時々「条件が成り立った時に、何も実行すべきものがない」事がある。
# その時に、「条件が成り立ったときに実行したい文」を省略して、
# if 条件式:
# else:
#        条件が成り立たなかったとき
# と記述するとエラーになる。こんな時に、Pythonでは「何もしない文」が用意してある
# それが『pass』である。以下のようにすればエラーにはならない
# 
# if 条件式:
#         pass       #何もしない文
# else:
#        条件が成り立たなかったとき 
# 
# 