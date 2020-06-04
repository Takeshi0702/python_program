#【たくさんの円を動かそう】
# これまでは１つの円を描画してきたが、今度は一度にもっとたくさんの円を描画する
# たくさんの円を制御するには、リストを使ってループ処理する
# 
#【円をディレクショナリとリストで管理する】
# たくさんの円を制御するためには、それぞれの円が持つ値を、すべて管理しないといけない
# １つの円を制御するのには、少なくとも４つの変数が必要
# 「x」・・・ X座標を示す
# 「y」・・・ Y座標を示す
# 「dx」・・・Xの移動量を示す
# 「dy」・・・Yの移動量を示す

# もし、こうした変数のまま、３個の円を制御するならば
# 「1つめの円」・・・x、y、dx、dy
# 「2つめの円」・・・x2、y2、dx2、dy2
# 「3つめの円」・・・x3、y3、dx3、dy3
# 
# という変数が必要になる
# もっと増えれば、その分だけ変数が必要となり、とても管理しにくくなる
# そこで２つの工夫をする

# １つめの工夫
# 【値をひとまとめにするディクショナリ】
# 「１つの円に関するデータは、ひとまとめにする」という考え方
# そのための方法として、Pythonの「ディクショナリ(Dictionary)」という機能を使う
# ディクショナリは「キーと値のペア」を、ひとまとめにして管理する仕組み
# 例えば、次のように使う。ここでは「ball」は任意の変数名です

# ball = {"x" : 400, "y" : 300, "dx" : 1, "dy" : 1}
#このように記述すると 、ballというひとまとまりの中に、「x」「y」「dx」「dy」が保存される
# 
#もしX座標の値を取り出したいなら 
# ball["x"]
# のように記述し、同様にY座標を取り出したいなら
# ball["y"]

# のように記述する。このようにディクショナリは以下の書式で設定する
# 変数名 = { キー名 : 値, キー名 : 値, ・・・}
# こうして記述すると、それぞれのキーに対して
# 変数名["キー名"]
# という書式で参照できる仕組みです
# このようにディクショナリを使うと、関連するデータをひとまとめにしやすくなる。

# P208から
#【リストを使って複数個扱う】
# 


