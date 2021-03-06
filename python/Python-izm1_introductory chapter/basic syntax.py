# 【基本構文】
# 前項まででインストールおよびプログラムの実行方法を学びました。ここでPythonの基本構文について触れておきます。なおPythonでは関数やクラス、その他命令が書かれたファイルをモジュールと呼びます。今後は作成したファイルをモジュールと書きますのでご注意ください。
# ※関数やクラスは応用編で紹介します。
# 
# 1 プログラム構造
# 2 エンコード宣言
# 2.1 Python 3系では
# 2.2 Python 2系では
# 3 インデントとコメントアウト
# 4 「__name__」とは？「__main__」とは？
# 5 処理の順番
# 6 インタープリタ記述
# 
# 
# １ プログラム構造
# もう一度新規でファイルを作成しましょう。下記コードを書き込んでください。
# 
# Python 3系
# 
# print('モジュールのロード')
# 
# def test():
#     print('関数：testを呼び出しました')
# 
# if __name__ == '__main__':
# 
#     print('python-izm')
# #   print('パイソンイズム')
#     test()
# 
# 
# 《実行結果》
# モジュールのロード
# python-izm
# 関数：testを呼び出しました
# 
# 
# 上記の通り出力されるので、簡単に解説します。
# 
# 
# ２ エンコード宣言
# Python 3系では
# 
# 後述するPython 2系では、ほとんどのケースにおいて# -*- coding: utf-8 -*- のようにUTF-8でエンコード宣言を行う事が望ましいです（特に日本語環境でプログラミングを行う場合）。3系においては、先に示したtest02.pyのようにエンコード宣言を省略した場合、デフォルトでUTF-8が適用されるため、モジュールを作成するたびに毎回記述する必要がなくなりました。
# 
# 
# ３ インデントとコメントアウト
# 3行目に関数、6行目にif文が登場しています（2系では5行目、8行目）。
# ※関数は応用編で、if文は基礎編で紹介します。
# 
# この関数は、呼び出された際に関数：testを呼び出しましたと出力するだけの簡単なものです。
# 
# Python 3系
# 
# print('モジュールのロード')
# 
# def test():
#     print('関数：testを呼び出しました')
# 
# if __name__ == '__main__':
# 
#     print('python-izm')
# #   print('パイソンイズム')
#     test()
# 
# 
# Pythonはブロック構造に「 { 」（中カッコ）を用いない、インデントでのブロック構造となっています。そのため関数testの範囲は4行目、if文の範囲は7行目から10行目となります（2系では6行目、9行目から12行目）。なお見た目上はインデントがきちんとしていても、タブと半角スペースが混じったようなインデントではエラーとなります(4タブと半角スペース4つなど）。

# 先程の実行結果には9行目のパイソンイズムは出力されませんでした（2系では11行目）。その理由は9行目、行頭の「 # 」（ハッシュマーク）がPythonではコメントアウト記号となっているからです。ハッシュマーク以降の記述は実行の対象とはならず、Pythonの文法に即していなくても構いません。
# 
# 
# 
# ４ 「__name__」とは？「__main__」とは？
# 6行目のif文は（2系では8行目）、スクリプトとして直接呼び出した時のみ実行し、別のモジュールから呼び出された時（インポート）には実行しない、という記述です（※インポートは基礎編で紹介します）。 変数__name__には、スクリプトとして起動した際に__main__という値が入ります。 別のモジュールから呼び出された時には、自身のモジュール名が入るので実行されない、という仕組みです。
# 
# Python 3系
# 
# print('モジュールのロード')
# 
# def test():
#     print('関数：testを呼び出しました')
# 
# if __name__ == '__main__':
# 
#     print('python-izm')
# #   print('パイソンイズム')
#     test()
# 
# 
# ５ 処理の順番
# 先程の出力結果は下記の通りでした。
# 
# 《実行結果》
# モジュールのロード
# python-izm
# 関数：testを呼び出しました
# 
# 
# まず最初にモジュールのロードが出力されています。
# Pythonのプログラムは、実行されると上から順に処理していきます。
# そのため一番最初にモジュールのロードが出力されます。
# 
# Python 3系
# 
# 
# print('モジュールのロード')
# 
# def test():
#     print('関数：testを呼び出しました')
# 
# if __name__ == '__main__':
# 
#     print('python-izm')
# #   print('パイソンイズム')
#     test()
# 
# 
# 次にpython-izmが出力されています。上から順に処理していますが、4行目のprint文は（2系では6行目）関数の配下にいるため、test関数が呼ばれない限り実行される事はありません。さらに下へ行くと、先程も触れたif文があります。スクリプトとして実行しているので、__name__には__main__が入っています。そのため、この評価式はTrueとなりif文内の最初の命令であるpython-izmが出力されます。
# 
# 
# Python 3系
# 
# print('モジュールのロード')
# 
# def test():
#     print('関数：testを呼び出しました')
# 
# if __name__ == '__main__':
# 
#     print('python-izm')
# #   print('パイソンイズム')
#     test()
# 
# 
# 次のパイソンイズムはコメントアウトされているので実行されません。
# そして最後にtest関数が呼び出されて関数:testを呼び出しましたが出力される、という順番です。
# 
# Python 3系
# 
# print('モジュールのロード')
# 
# def test():
#     print('関数：testを呼び出しました')
# 
# if __name__ == '__main__':
# 
#     print('python-izm')
# #   print('パイソンイズム')
#     test()
# 
# 
