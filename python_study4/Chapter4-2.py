# 【変数を使ってみよう】
# 変数は、値を保存するための場所
# 計算結果など、様々なデータを一時的に保存するときに使う
# 
# 
# 【変数とは】
# 「変数は、プログラムを書く人が好きな名前を付けた「器」です」
# その器には、好きな値を格納する事ができ、あとで参照して利用できる
# 
# >>> a = 1
# 
# これは「変数aに、値1を格納する」という意味の文
# このように変数に値を格納する操作を「代入(だいにゅう)する」と表現し、「=」の記号を使う
# 上記の命令を実行すると「aという名前の箱」ができて、その中に「値1」が格納される
# 変数はいくつでも作れる。例えば以下のように、
# 
# >>> b = 2
# 
# と入力すれば、変数bに「値2」が格納される
# 変数は、最初に値を代入したときに作られる
# 最初に「変数名 = 値」と記述して変数を作る操作を「変数を定義して初期化する」と言う
# 
# 
# 《文字列を格納する》
# 
# >>> c = "abc"
# とすれば、変数cに「値"abc"」が格納される
# 
# 《変数名は長くても構わない》
# 実際には、値の意味を分かりやすくするために、「name」(氏名などを格納)、「total」(統計などを格納)、
# 「tel」や「telephone」(電話番号などを格納)といった変数名がよく使われる
# 
# >>> username = "山田太郎"
# 
# 上のように記述すれば、username と言う名前の変数ができ、そこに"山田太郎"と言う値が格納される
# 
# このように「何か好きな名前を付けた入れ物に、値を格納しておく」のが変数です
# 
# 
# 【変数の参照】
# 変数に保存した値は、その「変数名」を指定すると値を取り出せる
# 
# >>> a = 1 としてたら
# >>> a と打つと
# １が表示される
# 
# このように変数の値を取り出す行為を『参照』と言う
# 
# 変数での計算も可能
# 
# >>> a = 1
# >>> b = 2
# >>> a + b
# ３　と表示される
# 
# 【値を格納していないと参照できない】
# まだ値を設定していない変数を参照してしまうと「Error」になる
# 
# 
# 【Pythonのプログラムファイルから操作する】
# 
# これまでインタラクティブモードで操作してきたが、Pythonのプログラムファイルでも同じ操作になる
# 
# # coding:utf-8
# 
# a = 1
# b = 2
# print(a + b)
# 
# ３と表示される
# 
# 