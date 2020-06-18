# https://www.javadrive.jp/python/
# 【辞書】

# 辞書を作成する
# 辞書でキーを指定して値を取得する
# 辞書の要素の値を変更するまたは新しい要素を追加する
# 辞書の長さ(要素数)を取得する
# 辞書から要素を削除する
# 辞書に指定したキーの要素が含まれているか確認する
# 辞書に含まれるすべてのキーと値を取得する


# 【辞書を作成する】
# 辞書を作成する

# 辞書を新しく作成する方法について解説します。辞書にはキーと対応するオブジェクトの組み合わせを 1 つの要素とする複数の要素が含まれます。

# 目次

# 値を指定して辞書を作成する
# 変数に代入された値を要素として指定する

# 値を指定して辞書を作成する
# 辞書型は { から } までの間に複数の要素をカンマ(,)で区切って定義します。要素はキーと対応する値の組み合わせを キー:値 の形式で記述します。書式は次のとおりです。

# {キー1:値1, キー2:値2, ...}

# リストやタプルのようなシーケンス型とは異なり辞書はマッピング型なので要素には順序はありません(ただし Python3.7 からは辞書の順序は要素が挿入された順序であることが保証されるようになりました)。インデックスは存在せず、スライスも使用できません。その代わりにキーを指定して対応するオブジェクトを取得することができます。

# キーにはハッシュ可能なオブジェクトを指定できます。具体的にはイミュータブルなオブジェクトのように値が変更できないもので、数値や文字列、タプルなどが辞書のキーとして使用できます。逆にリストや辞書のようなミュータブルなオブジェクトはキーに使用できません。

# 値には数値や文字列など Python で扱えるオブジェクトであれば何でも指定することができます。

# {1:"Orange", 2:"Lemon", 3:"Peach"} {"red":"赤色", "blue":"青色", "yellow":"黄色"}
# 同じ辞書で要素毎に異なるデータ型のオブジェクトを指定することができます。

# {"old":28, "address":"Tokyo"}

# 要素が空の辞書を作成することができます。

# {}

# 作成した辞書は数値や文字列のように変数に代入して利用することができます。

# mydict = {1:"Orange", 2:"Lemon", 3:"Peach"}

# 変数に代入された値を要素として指定する
# 値を指定して辞書を作成するときに、値を直接入力するかわりに値が代入された変数を指定して辞書を作成することができます。変数はキーと値のどちらでも使用できます。

# >>> x = 1
# >>> y = "Desktop"
# >>> mydict = {x:y}
# >>> print(mydict)
# {1: 'Desktop'}
# >>>
# 要素に変数名を指定した場合、要素には変数の参照が設定されるのではなく辞書の作成時に変数に代入されていた値が直接記述されたのと同じ扱いとなります。その為、先ほどの辞書は次のように作成したものとまったく同じです。

# >>> mydict = {1:"Desktop"}
# >>> print(mydict)
# {1: 'Desktop'}
# >>>
# 辞書を作成したあとに変数に別の値を代入しても、辞書の要素は変更されません。

# >>> x = 1
# >>> y = "Desktop"
# >>> mydict = {x:y}
# >>> print(mydict)
# {1: 'Desktop'}
# >>> y = "Movile"
# >>> print(mydict)
# {1: 'Desktop'}
# >>>
# -- --

# 辞書を作成する方法について解説しました。



# 【辞書でキーを指定して値を取得する】
# 辞書でキーを指定して値を取得する

# 辞書に含まれる要素はキーと値の組み合わせとなっており、キーを指定することで対応する値を取得することができます。ここでは辞書でキーを指定して値を取得する方法について解説します。

# 目次

# キーを指定して値を取得する
# getメソッドを使用して値を取得する

# キーを指定して値を取得する
# 辞書に含まれる要素にはキーと値の組み合わせが含まれます。辞書に対してキーを指定することで、キーに対応する値を取得することができます。

# 辞書[キー]

# 次の例では辞書に対してキーを指定してそれぞれ対応した値を取得しています。

# >>> mydict = {"JP":"Japan", "DE":"Germany", "FR":"France"}
# >>> print(mydict["DE"])
# Germany
# >>> print(mydict["FR"])
# France
# >>> print(mydict["JP"])
# Japan
# >>>
# なお存在しないキーを指定すると KeyError エラーが発生します。

# >>> mydict = {"JP":"Japan", "DE":"Germany", "FR":"France"}
# >>> print(mydict["BR"])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'BR'
# >>>
# サンプルプログラム
# それでは簡単なサンプルプログラムを作って試してみます。テキストエディタで次のように記述したあと、 sample2-1.py という名前で保存します。

# mydict = {"JP":"Japan", "DE":"Germany", "FR":"France"}

# print(mydict)
# key1 = "JP"
# print("キー：" + key1 + "、値：" + mydict[key1])
# key2 = "FR"
# print("キー：" + key2 + "、値：" + mydict[key2])

# その後で、次のように実行してください。

# python sample2-1.py

# キーを指定して値を取得する(1)

# 辞書に対してキーを指定して対応する値を取得することができました。

# getメソッドを使用して値を取得する
# キーを指定して値を取得するのは同じですが、存在しないキーを指定した場合にはデフォルト値を返す方法です。辞書型で利用可能な get メソッドを使用します。

# 辞書.get(key[, default])

# get メソッドは引数に指定したキーの要素を取得します。指定したキーが存在しなかった場合は default が返されます。なお default は省略可能で、省略した場合は None が返ります。

# 具体的には次のように記述します。

# >>> mydict = {"JP":"Japan", "DE":"Germany", "FR":"France"}
# >>> print(mydict.get("DE"))
# Germany
# >>> print(mydict.get("EN"))
# None
# >>>  print(mydict.get("EN", "NotFound"))
# NotFound
# >>>
# キーが存在すれば対応する値を返し、存在しない場合でもエラーとならずに指定した値を返します。

# サンプルプログラム
# それでは簡単なサンプルプログラムを作って試してみます。テキストエディタで次のように記述したあと、 sample2-2.py という名前で保存します。

# mydict = {"JP":"Japan", "DE":"Germany", "FR":"France"}

# print(mydict)
# key1 = "JP"
# print("キー：" + key1 + "、値：" + mydict.get(key1, "NotFound"))
# key2 = "FR"
# print("キー：" + key2 + "、値：" + mydict.get(key2, "NotFound"))
# key3 = "EN"
# print("キー：" + key3 + "、値：" + mydict.get(key3, "NotFound"))

# その後で、次のように実行してください。

# python sample2-2.py

# getメソッドを使用して値を取得する(1)

# 辞書に対してキーを指定して対応する値を取得することができました。

# -- --

# 辞書でキーを指定して値を取得する方法について解説しました。



# 【辞書の要素の値を変更するまたは新しい要素を追加する】
# 辞書の要素の値を変更するまたは新しい要素を追加する

# 作成済みの辞書はあとからキーを指定して要素の値を変更することができます。また辞書に存在しないキーを指定した場合には、新しい要素を辞書に追加することができます。ここでは辞書の要素を変更する方法または要素を追加する方法について解説します。

# 目次

# 辞書の要素の値を変更する
# 辞書に新しい要素を追加する
# 他の辞書のデータを使って辞書の要素の値を更新したり新しい要素を追加する

# 辞書の要素の値を変更する
# 作成済みの辞書の要素の値を変更するには次のようにキーを指定して新しい値を代入します。

# 辞書[キー] = 値

# 指定したキーが辞書に存在する場合には、そのキーに対応する値を新しい値に入れ替えます。

# 具体的には次のように記述します。

# mydict = {1:"Movie", 2:"Foods", 3:"Reading"}
# mydict[2] = "Sports"
# print(mydict)
# --> {1: 'Movie', 2: 'Sports', 3: 'Reading'}
# 指定したキーの対応する値が、新しい値と入れ替わりました。

# 辞書に新しい要素を追加する
# 作成済みの辞書に対してキーを指定して値を代入した場合、辞書の中にキーが存在しなかった場合は新しい要素として辞書に追加されます。

# 辞書[キー] = 値

# キーが存在すれば値を入れ替え、キーが存在していなかった場合は キー:値 を新しい要素として辞書に追加します。

# 具体的には次のように記述します。

# mydict = {1:"Movie", 2:"Foods", 3:"Reading"}
# mydict[4] = "Sports"
# print(mydict)
# --> {1: 'Movie', 2: 'Foods', 3: 'Reading', 4: 'Sports'}
# サンプルプログラム
# それでは簡単なサンプルプログラムを作って試してみます。テキストエディタで次のように記述したあと、 sample3-1.py という名前で保存します。

# mydict = {"w":"Water", "o":"Orange", "t":"Tea"}
# print(mydict)

# mydict["t"] = "GreenTea"
# print(mydict)

# mydict["c"] = "Coffee"
# print(mydict)

# その後で、次のように実行してください。

# python sample3-1.py

# 辞書の要素の値を入れ替えるまたは要素を追加する(1)

# キーを指定して、既存の要素の値を変更したり、新しく辞書に追加することができました。

# 他の辞書のデータを使って辞書の要素の値を更新したり新しい要素を追加する
# 辞書型で利用可能な update メソッドを使用すると、既存の辞書の要素を update メソッドの引数に指定した辞書を使って更新したり新しい要素を追加したりすることができます。

# 対象の辞書.update(別の辞書)

# 別の辞書に含まれる要素の中で、キーが対象の辞書の中に同じものがあった場合、対象の辞書のキーに対する値が別の辞書の方の値で更新されます。また別の辞書に含まれる要素の中で、対象の辞書の中に同じキーが存在しなかった場合、対象の辞書に新しい要素として追加されます。

# 具体的には次のように記述します。

# mydict = {1:"A", 2:"B", 3:"C"}
# otherdict = {2:"b", 4:"d"}

# mydict.update(otherdict)
# print(mydict)
# --> {1:"A", 2:"b", 3:"C", 4:"d"}
# 同じキーの要素については値が更新され、存在していないキーの要素は新しい要素として追加されました。

# サンプルプログラム
# それでは簡単なサンプルプログラムを作って試してみます。テキストエディタで次のように記述したあと、 sample3-2.py という名前で保存します。

# lunchdict = {"a":"curry", "b":"paster", "c":"udon"}
# print(lunchdict)

# todaydict = {"b":"ramen", "d":"omelette"}
# lunchdict.update(todaydict)
# print(lunchdict)

# その後で、次のように実行してください。

# python sample3-2.py

# 他の辞書のデータを使って辞書の要素の値を更新したり新しい要素を追加する(1)

# update メソッドを使って、他の辞書オブジェクトのデータを使った対象の辞書の要素を更新したり新しい要素を追加したりしました。

# -- --

# 辞書の要素を入れ替えるまたは要素を追加する方法について解説します。



# 【辞書の長さ(要素数)を取得する】
# 辞書の長さ(要素数)を取得する

# 組み込み関数の len 関数を使って辞書の長さ(要素数)を取得する方法について解説します。

# 目次

# 辞書の長さを取得する

# 辞書の長さを取得する
# 組み込み関数の len 関数は引数に指定したオブジェクトの長さや要素の数を取得することができます。引数に辞書を指定した場合には、辞書に含まれる要素数を取得することができます。書式は次の通りです。

# len(辞書)

# 引数に指定したリストの要素数を取得します。

# len({1:"Apple", 2:"Orange", 3:"Lemon"}) --> 3

# len 関数について詳しくは「len関数の使い方(オブジェクトの長さや要素数を取得する)」を参照されてください。

# サンプルプログラム
# それでは簡単なサンプルプログラムを作って試してみます。テキストエディタで次のように記述したあと、 sample4-1.py という名前で保存します。

# colorlist = ["Blue", "Red", "Green", "White", "Black"]

# print(colorlist)
# print("要素数は " + str(len(colorlist)) + " です。")

# その後で、次のように実行してください。

# python sample4-1.py

# 辞書の長さを取得する(1)

# len 関数を使って辞書の要素数を取得することができました。

# -- --

# 組み込み関数の len 関数を使って辞書の要素数を取得する方法について解説しました。



# 【辞書から要素を削除する】
# 辞書から要素を削除する

# 作成済みの辞書からキー指定して要素を削除したり、すべての要素を削除する方法について解説します。要素の削除には del 文や pop メソッドや popitem メソッドを使用します。またすべての要素を削除するには clear メソッドを使用します。

# 目次

# del文を使って要素を削除する
# 指定したキーの要素を削除する
# 最後に追加された要素を取得した上で削除する
# 全ての要素を削除する

# del文を使って要素を削除する
# del 文はキーを指定して取り出した辞書の要素を削除します。次のように実行します。

# del 辞書[キー]

# キーを指定した辞書の要素を、 del 文を使って削除しています。

# 具体的には次のように記述します。

# >>> mydict = {"A":"Apple", "L":"Lemon", "O":"Orange"}
# >>> del mydict["L"]
# >>> print(mydict)
# {'A': 'Apple', 'O': 'Orange'}
# >>>
# なお存在しないキーを指定すると KeyError エラーとなります。

# >>> mydict = {"A":"Apple", "L":"Lemon", "O":"Orange"}
# >>> del mydict["P"]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'P'
# >>>
# 指定したキーの要素を削除する
# del 文と同じように指定したキーの要素を辞書から削除する方法です。辞書型で利用可能な pop メソッドを使用します。

# 辞書.pop(key[, default])

# pop メソッドは引数に指定したキーの要素を取得した上で辞書から削除します。指定したキーが存在しなかった場合は default が返されます( default は省略可能です)。

# 具体的には次のように記述します。

# >>> mydict = {"A":"Apple", "L":"Lemon", "O":"Orange"}
# >>> val = mydict.pop("L")
# >>> print(val)
# Lemon
# >>> print(mydict)
# {'A': 'Apple', 'O': 'Orange'}
# >>>
# default を指定せずに存在しないキーを指定すると KeyError エラーとなります。

# >>> mydict = {"A":"Apple", "L":"Lemon", "O":"Orange"}
# >>> val = mydict.pop("P")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'P'
# >>>
# default を指定した場合は、存在しないキーを指定してもエラーとならず default に指定した値が返ります。

# >>> mydict = {"A":"Apple", "L":"Lemon", "O":"Orange"}
# >>> val = mydict.pop("P", "Not Found")
# >>> print(val)
# Not Found
# >>> print(mydict)
# {"A":"Apple", "L":"Lemon", "O":"Orange"}
# >>>
# 最後に追加された要素を取得した上で削除する
# 辞書に最後に追加された要素を (キー, 値) の形式でタプルとして取得したあと要素を辞書から削除する方法です。辞書型で利用可能な popitem メソッドを使用します。

# 辞書.popitem()

# 以前のバージョンでは辞書に含まれるいずれかの一つの要素を取得し削除していましたが、 Python 3.7 以降は最後に追加された要素を取得して削除します。

# 具体的には次のように記述します。

# >>> mydict = {"A":"Apple", "L":"Lemon", "O":"Orange"}
# >>> val = mydict.popitem()
# >>> print(val)
# ('O', 'Orange')
# >>> print(mydict)
# {'A': 'Apple', 'L': 'Lemon'}
# >>>
# >>> val = mydict.popitem()
# >>> print(val)
# ('L', 'Lemon')
# >>> print(mydict)
# {'A': 'Apple'}
# >>>
# >>> val = mydict.popitem()
# >>> print(val)
# ('A', 'Apple')
# >>> print(mydict)
# {}
# >>>
# popitem メソッドを繰り返し呼び出すと、辞書に最後に追加されたものから順に要素を取得していきます。なお要素が空の状態で popitem メソッドを使用すると KeyError エラーが発生します。

# 全ての要素を削除する
# 辞書に含まれるすべての要素を削除する方法です。辞書型で利用可能な clear メソッドを使用します。

# 辞書.clear()

# 辞書の要素がすべて削除されます。辞書オブジェクトは削除されません。

# 具体的には次のように記述します。

# >>> mydict = {"A":"Apple", "L":"Lemon", "O":"Orange"}
# >>> mydict.clear()
# >>> print(mydict)
# {}
# >>>
# clear メソッドを使用したあとは、辞書オブジェクトは空となりました。

# -- --

# 作成済みの辞書からキー指定して要素を削除したり、すべての要素を削除する方法について解説しました。



# 【辞書に指定したキーの要素が含まれているか確認する】
# 辞書に指定したキーの要素が含まれているか確認する

# 作成済みの辞書に指定したキーの要素が含まれているかどうかを確認方法について解説します。要素が含まれているかどうかの確認には in 演算子を使用します。

# 目次

# 指定のキーの要素が含まれているか確認する

# 指定のキーの要素が含まれているか確認する
# 指定のキーの要素が辞書の中に含まれているかどうかを確認するには in 演算子を使用します。

# キー in 辞書

# 辞書の要素の中で指定したキーを持つ要素があった場合には式は True となります。なかった場合には False となります。

# 具体的には次のように記述します。

# >>> mydict = {"L":"Lemon", "O":"Orage", "G":"Grapes"}
# >>> print("O" in mydict)
# True
# >>> print("P" in mydict)
# False
# >>>
# なお in 演算子のかわりに not in 演算子を使うと、指定したキーの要素があった場合に False 、なかった場合に True となります。

# >>> mydict = {"L":"Lemon", "O":"Orage", "G":"Grapes"}
# >>> print("O" not in mydict)
# False
# >>> print("P" not in mydict)
# True
# >>>

# -- --
# 作成済みの辞書に指定したキーの要素が含まれているかどうかを確認方法について解説しました。



# 【辞書に含まれるすべてのキーと値を取得する】
# 辞書に含まれるすべてのキーと値を取得する

# 辞書に含まれるすべてのキー、すべての値、すべてのキーと値の組み合わせをそれぞれ取得する方法について解説します。キーの取得には keys メソッド、値の取得には values メソッド、キーと値の組み合わせの取得には items メソッドを使用します。

# 目次

# 辞書に含まれるすべてのキーを取得する
# 辞書に含まれるすべての値を取得する
# 辞書に含まれるすべてのキーと値の組み合わせを取得する

# 辞書に含まれるすべてのキーを取得する
# 辞書の中のすべてのキーの一覧を取得するには keys メソッドを使用します。

# 辞書.keys()

# 辞書に含まれるキーの一覧を取得します。取得した一覧は dict_keys 型の値として取得します。

# >>> mydict = {"L":"Lemon", "O":"Orage", "G":"Grapes"}
# >>> print(mydict.keys())
# dict_keys(['L', 'O', 'G'])
# >>>
# for 文と組み合わせることですべてのキーを順に取り出すことができます。

# >>> mydict = {"L":"Lemon", "O":"Orage", "G":"Grapes"}
# >>> for mykey in mydict.keys():
# ...     print(mykey)
# ...
# L
# O
# G
# >>>
# dict_keys 型について詳細は分かりませんが、リスト型のコンストラクタの引数に指定することでキーの一覧をリストとして取得することができます。

# >>> mydict = {"L":"Lemon", "O":"Orage", "G":"Grapes"}
# >>> mylist = list(mydict.keys())
# >>> print(mylist)
# ['L', 'O', 'G']
# >>>
# 辞書に含まれるすべての値を取得する
# 辞書の中のすべての値の一覧を取得するには values メソッドを使用します。

# 辞書.values()

# 辞書に含まれる値の一覧を取得します。取得した一覧は dict_values 型の値として取得します。

# >>> mydict = {"L":"Lemon", "O":"Orage", "G":"Grapes"}
# >>> print(mydict.values())
# dict_values(['Lemon', 'Orage', 'Grapes'])
# >>>
# for 文と組み合わせることですべての値を順に取り出すことができます。

# >>> mydict = {"L":"Lemon", "O":"Orage", "G":"Grapes"}
# >>> for myvalue in mydict.values():
# ...     print(myvalue)
# ...
# Lemon
# Orage
# Grapes
# >>>
# dict_values 型について詳細は分かりませんが、リスト型のコンストラクタの引数に指定することでキーの一覧をリストとして取得することができます。

# >>> mydict = {"L":"Lemon", "O":"Orage", "G":"Grapes"}
# >>> mylist = list(mydict.values())
# >>> print(mylist)
# ['Lemon', 'Orage', 'Grapes']
# >>>
# 辞書に含まれるすべてのキーと値の組み合わせを取得する
# 辞書の中のすべてのキーと値の組み合わせの一覧を取得するには items メソッドを使用します。

# 辞書.items()

# 辞書に含まれるキーと値の組み合わせの一覧を取得します。取得した一覧は dict_items 型の値として取得します。

# >>> mydict = {"L":"Lemon", "O":"Orage", "G":"Grapes"}
# >>> print(mydict.items())
# dict_items([('L', 'Lemon'), ('O', 'Orage'), ('G', 'Grapes')])
# >>>
# for 文と組み合わせることですべての値を順に取り出すことができます。

# >>> mydict = {"L":"Lemon", "O":"Orage", "G":"Grapes"}
# >>> for mykey, myvalue in mydict.items():
# ...     print("key:" + mykey + ", values:" + myvalue)
# ...
# key:L, values:Lemon
# key:O, values:Orage
# key:G, values:Grapes
# >>>
# dict_items 型について詳細は分かりませんが、リスト型のコンストラクタの引数に指定することでキーの一覧をリストとして取得することができます。

# >>> mydict = {"L":"Lemon", "O":"Orage", "G":"Grapes"}
# >>> mylist = list(mydict.items())
# >>> print(mylist)
# [('L', 'Lemon'), ('O', 'Orage'), ('G', 'Grapes')]
# >>>
# -- --

# 辞書に含まれるすべてのキー、すべての値、すべてのキーと値の組み合わせをそれぞれ取得する方法について解説しました。
