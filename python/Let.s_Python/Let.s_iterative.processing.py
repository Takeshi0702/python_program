# https://www.javadrive.jp/python/
# 【繰り返し処理】

# while文を使った繰り返し
# for文を使った繰り返し
# for文の中でrange関数を使って指定した回数だけ繰り返し処理を行う
# break文を使った繰り返し処理の強制終了とcontinue文を使った繰り返し処理のスキップ


# 【while文を使った繰り返し】
# while文を使った繰り返し

# Python で繰り返し処理を行う時に利用できる while 文の使い方について解説します。 while 文は条件式が真の間、続くブロック内の処理を繰り返します。

# 目次

# while文の処理の流れ
# while文の最後に実行される処理を記述する(while..else文)

# while文の処理の流れ
# while 文は指定した条件式が真の間、処理を繰り返し実行します。基本的な書式は次の通りです。

# while 条件式:
#     条件式が真の時に実行する文
# 条件式が真となった場合、その後に記述されたブロックの中の文を順に実行します。複数の文を実行させたい場合にはブロック内に記述してください。

# while 条件式:
#     条件式が真の時に実行する文1
#     条件式が真の時に実行する文2
#     条件式が真の時に実行する文3
# ※ Python ではブロックをインデントを使って定義します。詳しくは「Pythonにおけるインデントを使ったブロックの定義」を参照されてください。

# 次のような例で考えてみます。

# num = 0
# while num < 2:
#     print("num = " + str(num))

# print("End")
# この時実行される流れは次のようになります。

#  1) 変数 num に 0 を代入
#  2) while 文の条件式を評価。変数 num は 2 より小さいので条件式は真
#  3) 変数 num の値を出力
#  4) ブロックの最後まで達したので再度 while 文の条件式を評価
#  5) 変数 num は 2 より小さいので条件式は真
#  6) 変数 num の値を出力
#  7) (4)から(6)を無限に繰り返し実行
# このように while 文は条件式を評価し、真であればブロック内の処理を実行し再度条件式の評価へ戻ります。今回の例ではブロック内で条件式が変化するような処理がないため、繰り返しが無限に繰り返されてしまいます。

# では先ほどの例を少し変更します。

# num = 0
# while num < 2:
#     print("num = " + str(num))
#     num += 1

# print("End")
# 今度はブロック内で変数 num に代入されている値に 1 を加算しています。今回の処理の流れは次のようになります。

#  1) 変数 num に 0 を代入
#  2) while 文の条件式を評価。変数 num は 2 より小さいので条件式は真
#  3) 変数 num の値を出力
#  4) 変数 num に 1 を加算 (num は 1)
#  5) ブロックの最後まで達したので再度 while 文の条件式を評価
#  6) 変数 num は 2 より小さいので条件式は真
#  7) 変数 num の値を出力
#  8) 変数 num に 1 を加算 (num は 2)
#  9) ブロックの最後まで達したので再度 while 文の条件式を評価
# 10) 変数 num は 2 より小さくないので条件式は偽
# 11) while 文を終了し次の処理へ
# 12) "End" を出力
# while 文の繰り返し処理が 1 回実行されるたびに変数 num の値が変化しています。その結果 while 文の条件式は3回目で偽となり while 文は終了します。

# サンプルプログラム
# それでは簡単なサンプルプログラムを作って試してみます。テキストエディタで次のように記述したあと、 sample1-1.py という名前で保存します。

# num = 1
# print("Start")

# while num < 6:
#     print("num = " + str(num))
#     num += 1

# print("End")
# その後で、次のように実行してください。

# python sample1-1.py

# while文の処理の流れ(1)

# 変数 num の値を変化させて num の値が 5 以上になるまで繰り返しを行いました。

# while文の最後に実行される処理を記述する(while..else文)
# while 文は指定した条件式が真の間、処理を繰り返し実行しますが、条件式が偽になった時に実行される処理を else 節のあとに記述することができます。

# while 条件式:
#     条件式が真の時に実行する文1
#     条件式が真の時に実行する文2
# else:
#     条件式が偽の時に実行する文1
#     条件式が偽の時に実行する文2
# これは単に while 文の次に記述した場合と基本は変わりありません。 while 文が終了すると、 while 文の次に記述されている文が実行されるためです。

# while 条件式:
#     条件式が真の時に実行する文1
#     条件式が真の時に実行する文2

# 実行する文1
# 実行する文2
# ただ while 文の中で break 文が実行された場合だけ異なります。 break 文が実行されると else 節のあとに記載されているブロック内の処理は実行せずに while 文の次へ処理が移るためです。 else 節を使わなかった場合は break 文が実行されたかどうかに関わらず while 文の次に記述された処理が実行されます。(break 文については「break文を使った繰り返し処理の強制終了とcontinue文を使った繰り返し処理のスキップ」を参照されてください)。

# サンプルプログラム
# それでは簡単なサンプルプログラムを作って試してみます。テキストエディタで次のように記述したあと、 sample1-2.py という名前で保存します。

# num = 1
# total = 0
# print("Start")

# while num < 6:
#     print("num = " + str(num))
#     total += num
#     num += 1
# else:
#     print("Total = " + str(total))

# print("End")
# その後で、次のように実行してください。

# python sample1-2.py

# while文の最後に実行される処理を記述する(while..else文)(1)

# else 節を使って while 文の最後に実行される処理を記述しました。

# -- --

# Python で繰り返し処理を行う時に利用できる while 文の使い方について解説しました。



# 【for文を使った繰り返し】
# for文を使った繰り返し

# Python で繰り返し処理を行う時に利用できる for 文の使い方について解説します。 for 文は別途指定したイテラブルなオブジェクトの要素の数だけ要素を 1 つずつ取り出してながら繰り返しを行います。

# 目次

# for文の処理の流れ
# for文の最後に実行される処理を記述する(for..else文)

# for文の処理の流れ
# for 文は決められた回数だけ、処理を繰り返し実行します。基本的な書式は次の通りです。

# for 変数 in イテラブルオブジェクト:
#     実行する文
# イテラブルオブジェクトから要素を順につ取得しつつ、イテラブルオブジェクトの要素の数だけその後に記述されたブロックの中の文を順に実行します。複数の文を実行させたい場合にはブロック内に記述してください。

# なおイテラブルオブジェクトとは要素を順番に取り出すことができるオブジェクトのことで、文字列、リスト、タプル、辞書などがイテラブルオブジェクトです。

# for 変数 in イテラブルオブジェクト:
#     実行する文1
#     実行する文2
#     実行する文3
# ※ Python ではブロックをインデントを使って定義します。詳しくは「Pythonにおけるインデントを使ったブロックの定義」を参照されてください。

# 次のような例で考えてみます。

# mylist = ["Orange", "Peach", "Lemon"]
# for val in mylist:
#     print(val)

# print("End")
# この時実行される流れは次のようになります。

#  1) リストを定義し変数 mylist にを代入
#  2) mylist から要素を 1 つ取得して val に代入 (val は "Orange")
#  3) 変数 val の値を出力
#  4) mylist から要素を 1 つ取得して val に代入 (val は "Peach")
#  5) 変数 val の値を出力
#  6) mylist から要素を 1 つ取得して val に代入 (val は "Lemon")
#  7) 変数 val の値を出力
#  8) イテラブルオブジェクトから要素をすべて取得したので for 文を終了
#  9) "End" を出力
# このように for 文で指定したイテラブルオブジェクトの要素の数だけ繰り返しが行われます。

# サンプルプログラム
# それでは簡単なサンプルプログラムを作って試してみます。テキストエディタで次のように記述したあと、 sample3-1.py という名前で保存します。

# mylist = ["Orange", "Peach", "Lemon", "Apple"]
# print(mylist)
# for val in mylist:
#     print("value:" + val)

# print("¥n")

# mydict = {"L":"Lemon", "O":"Orage", "G":"Grapes"}
# print(mydict)
# for mykey, myvalue in mydict.items():
#     print("key:" + mykey + ", value:" + myvalue)
# その後で、次のように実行してください。

# python sample3-1.py

# for文の処理の流れ(1)

# for 文を使ってリストおよび辞書のオブジェクトから要素を 1 つずつ取得し画面に出力しました。(辞書型で使用できる items メソッドについては「辞書に含まれるすべてのキーと値を取得する」を参照されてください。)

# for文の最後に実行される処理を記述する(for..else文)
# for 文はイテラブルオブジェクトの要素の数だけ繰り返し処理を行いますが、全ての要素を取得したあとに最後に実行される処理を else 節のあとに記述することができます。

# for 変数 in イテラブルオブジェクト:
#     実行する文1
#     実行する文2
# else:
#     実行する文1
#     実行する文2
# これは単に for 文の次に記述した場合と基本は変わりありません。 for 文が終了すると、 for 文の次に記述されている文が実行されるためです。

# for 変数 in イテラブルオブジェクト:
#     実行する文1
#     実行する文2

# 実行する文1
# 実行する文2
# ただ for 文の中で break 文が実行された場合だけ異なります。 break 文が実行されると else 節のあとに記載されているブロック内の処理は実行せずに for 文の次へ処理が移るためです。 else 節を使わなかった場合は break 文が実行されたかどうかに関わらず for 文の次に記述された処理が実行されます。(break 文については「break文を使った繰り返し処理の強制終了とcontinue文を使った繰り返し処理のスキップ」を参照されてください)。

# サンプルプログラム
# それでは簡単なサンプルプログラムを作って試してみます。テキストエディタで次のように記述したあと、 sample3-2.py という名前で保存します。

# count = 0
# mylist = ["Orange", "Peach", "Lemon", "Apple"]
# print(mylist)
# for val in mylist:
#     print("value:" + val)
#     count += 1
# else:
#     print("要素の数 = " + str(count))
# その後で、次のように実行してください。

# python sample3-2.py

# for文の最後に実行される処理を記述する(for..else文)(1)

# else 節を使って for 文の最後に実行される処理を記述しました。

# -- --

# Python で繰り返し処理を行う時に利用できる for 文の使い方について解説しました。



# 【for文の中でrange関数を使って指定した回数だけ繰り返し処理を行う】
# for文の中でrange関数を使って指定した回数だけ繰り返し処理を行う

# for 文ではイテラブルなオブジェクトから要素を 1 つずつ取り出して繰り返しを行いますが、 range 関数を使用することで、簡単に指定した回数だけ繰り返し処理を行うことができます。ここでは for 文で range 関数を使い指定回数繰り返しを行う方法について解説します。

# 目次

# range関数を使って指定した回数だけ繰り返し処理を行う

# range関数を使って指定した回数だけ繰り返し処理を行う
# Python では繰り返し処理を行うために for 文が使用されますが、例えば 10 回繰り返すなど指定して回数だけ繰り返しを行いたい場合には range 関数と組み合わせると便利です。

# 例えば次のように記述します。

# for i in range(10):
#     実行する処理 1
#     実行する処理 2
# range 関数は実際は range 型のコンストラクタで 0 から 引数に指定した数値を超えない値までの連続した数値を要素に持つオブジェクトを作成します。例えば range(10) とした場合には 0 1 2 3 4 5 6 7 8 9 の 10 個の要素を持ちます。 for 文では要素を 1 つずつ取り出しながら繰り返し処理を行うので、結果として先ほどの for 文は 10 回繰り返されることになります。

# ※ range 関数について詳しくはは「range関数の使い方(開始から終了までの連続した数値を要素として持つrange型オブジェクトを作成する)」を参照して下さい。

# 同じようなことをリストオブジェクトを使って行う場合次のように記述することができます。

# for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     実行する処理 1
#     実行する処理 2
# 10 回であればまだこのように記述することも可能ですが、 100 回や 1000 回など繰り返す回数が多い場合には range 関数を使用すると便利です。

# サンプルプログラム
# それでは簡単なサンプルプログラムを作って試してみます。テキストエディタで次のように記述したあと、 sample5-1.py という名前で保存します。

# num = 1
# print("num = 1")

# for i in range(10):
#     num *= 2
#     print("* 2 = " + str(num))
# その後で、次のように実行してください。

# python sample5-1.py

# range関数を使って指定した回数だけ繰り返し処理を行う(1)

# range 関数を使って繰り返し処理を 10 回行いました。

# -- --

# for 文の中で range 関数を使って指定した回数だけ繰り返し処理を行う方法について解説しました。



# 【break文を使った繰り返し処理の強制終了とcontinue文を使った繰り返し処理のスキップ】
# break文を使った繰り返し処理の強制終了とcontinue文を使った繰り返し処理のスキップ

# while 文や for 文の繰り返し処理の中で、 break 文を使用すると繰り替えし処理の強制終了を行うことができ、また continue 文を使用すると残り繰り返し処理をスキップして条件式の判定へ進めることができます。ここでは while 文や for 文の中で break 文と continue 文の使い方について解説します。

# 目次

# break文を使って繰り返し処理の強制終了
# continue文を使った繰り返し処理のスキップ

# break文を使って繰り返し処理の強制終了
# while 文や for 文のブロックの中で break 文が実行されると繰り返し処理が強制的に終了して次の文へ処理が移ります。

# break
# break 文は if 文と組み合わせて次のような使い方をします。

# while 条件式:
#     条件式が真の時に実行する文1
#     条件式が真の時に実行する文2

#     if 条件式:
#         break

#     条件式が真の時に実行する文3
# while 文であれば条件式が真の間繰り返しブロック内の処理を実行しますが、ブロック内で if 文を記述し、 if 文の条件式が真になった時は break を実行するように記述します。 break 文が実行されると while 文が強制的に終了します。

# 具体的に次のような例で考えてみます。 while 文の条件式は True としてあるため必ず真となり無限ループとなります。ただブロック内で if 文を使い条件式が真の場合は break 文を使って繰り返し処理を終了させます。

# num = 0
# while True:
#     print("num = " + str(num))
#     num += 1
#     if num >= 2:
#         breaak

# print("End")
# この時実行される流れは次のようになります。

#  1) 変数 num に 0 を代入
#  2) while 文の条件式を評価。条件式が True のため必ず条件式は真となる
#  3) 変数 num の値を出力
#  4) 変数 num に 1 を加算 (num は 1)
#  5) if 文の条件式を評価。変数 num は 2 より小さいので条件式は偽
#  6) ブロックの最後まで達したので再度 while 文の条件式を評価
#  7) 変数 num の値を出力
#  8) 変数 num に 1 を加算 (num は 2)
#  9) if 文の条件式を評価。変数 num は 2 より小さいくないので条件式は真
# 10) while 文を終了し次の処理へ
# 11) "End" を出力
# このように break 文を使用することで、特定の状態になった時に while 文や for 文を抜けることができます。

# サンプルプログラム
# それでは簡単なサンプルプログラムを作って試してみます。テキストエディタで次のように記述したあと、 sample6-1.py という名前で保存します。

# print("Start")

# while True:
#     print("数値を入力すると 5 倍した値を表示します")
#     print("終了する場合は -1 を入力してください")
#     num = int(input("> "))
#     if num == -1:
#         break
#     print("num = " + str(num) + ", num *  = " + str(num * 5) + "¥n")

# print("End")
# その後で、次のように実行してください。

# python sample6-1.py

# break文を使って繰り返し処理の強制終了(1)

# 数値の入力待ちとなります。数値を入力すると 5 倍にした数値を計算して表示します。

# break文を使って繰り返し処理の強制終了(2)

# break文を使って繰り返し処理の強制終了(3)

# -1 を入力すると break 文が実行されて処理が終了します。

# break文を使って繰り返し処理の強制終了(4)

# continue文を使った繰り返し処理のスキップ
# while 文や for 文のブロックの中で continue 文が実行されると繰り返し処理がスキップして条件式の評価まで処理が移ります。

# continue
# continue 文は if 文と組み合わせて次のような使い方をします。

# for 変数 in イテラブルオブジェクト:
#     実行する文1
#     実行する文2

#     if 条件式:
#         continue

#     実行する文3
# for 文であればリストやタプルなどのイテラブルオブジェクトに含まれる要素の数だけ繰り返しブロック内の処理を実行しますが、ブロック内で if 文を記述し、 if 文の条件式が真になった時は continue を実行するように記述します。 continue 文が実行されるとブロック内の if 文以降にある「実行する文3」は実行されずに for 文でイテラブルオブジェクトから次の要素を取り出すところまで処理がスキップします。

# 具体的に次のような例で考えてみます。 for 文でリストから要素を順に取り出し値を画面に表示します。ただし要素の値が文字列だった場合はスキップして次の要素の取得を行います。

# for val in [3, "ab", 7]:
#     if isinstance(val, str):
#         continue
#     print("val = " + str(val))

# print("End")
# この時実行される流れは次のようになります。

#  1) 変数 val にリストから要素を1つ代入 (val は 3)
#  2) if の条件式で val のデータ型が文字列型か調べる --> 偽
#  3) 変数 val の値を出力
#  4) 変数 val にリストから要素を1つ代入 (val は "ab")
#  5) if の条件式で val のデータ型が文字列型か調べる --> 真
#  6) ブロック内の残りの文はスキップ
#  7) 変数 val にリストから要素を1つ代入 (val は 7)
#  8) if の条件式で val のデータ型が文字列型か調べる --> 偽
#  9) 変数 val の値を出力
# 10) "End" を出力
# このように continue 文を使用することで、特定の状態の時にブロック内のそれ以降の処理をスキップさせることができます。

# サンプルプログラム
# それでは簡単なサンプルプログラムを作って試してみます。テキストエディタで次のように記述したあと、 sample6-1.py という名前で保存します。

# print("Start")
# total = 0

# for num in [35, 25, "OK", 45, "Pass", 28]:
#     if isinstance(num, str):
#         continue
#     print("num = " + str(num))
#     total += num

# print("Total = " + str(total))
# print("End")
# その後で、次のように実行してください。

# python sample6-2.py

# continue文を使った繰り返し処理のスキップ(1)

# リストの中の数値の要素だけを画面に出力し、最後に数値の合計を出力します。リストから要素を取得したときに文字列だった場合は continue 文でスキップしています。

# -- --

# while 文や for 文の中で break 文と continue 文の使い方について解説しました。
