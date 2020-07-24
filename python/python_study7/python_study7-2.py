# 【ウィンドウの中に円を描いていこう】
# tkinterでは、「キャンパス(Canvas)」を置いて、そこに必要な図形を描写する

#《円を描いてみよう》

# coding:utf-8
import tkinter as tk

# ウィンドウを描く
root = tk.Tk()
root.geometry("600x400")

# Canvasを置く
canvas =tk.Canvas(root, width =600, height =400, bg="white")
canvas.place(x = 0, y = 0)

# 円を描く
canvas.create_oval(300 - 20, 200 - 20, 300 +20, 200 + 20)

root.mainloop()


# 「キャンパスを作る」
# まずはウィンドウを作る、サイズは600x400ピクセルとし、作ったウィンドウはroot変数に代入する

# root = tk.Tk()
# root.geometry("600x400")
# 次にこのウインドウの上に、キャンパスを重ねる。キャンパスは図形や画像を描画する仕組み
# まずは「Canvasメソッド」を実行してキャンパスを作る。今回は作成したキャンパスを「canbas」と言う名前で変数に代入した
# 最後の引数に指定している「bg」は背景色であり、ここでは「white」として白にした

# canvas =tk.Canvas(root, width =600, height =400, bg="white")
# キャンパスを作成したら、placeメソッドを実行してウィンドウの左上に配置する

# canvas.place(x = 0, y = 0)
# ここまでのプログラミングで、ウィンドウの上に、同じサイズのキャンパスが重なった状態になった

#【円を描画する】
# キャンパスのさまざまなメソッドを使うと、図形や画像を描画できる

# 《Canvasに備わる描画のためのメソッド》
# create_arc(x1, y1, x2, y2, オプション)　　　        弧を描く
# create_bitmap(x, y, オプション)                   ビットマップを描く
# create_image(x, y, オプション)                    画像を描く
# create_line(x1, y1, x2, y2, オプション)           直線を描く
# create_oval(x1, y1, x2, y2, オプション)　         楕円または円を描く
# create_polygon(x1, y1, x2, y2,・・・, オプション)　多角形を描く
# create_rectangle(x1, y1, x2, y2, オプション)      四角形を描く
# create_text(x, y, オプション)                     テキストを描く
# 円を描くには「create_oval」のメソッドを使います。このメソッドには最低、４つの引数を指定する
#《MEMO》４つ以上の引数を指定して、塗りや線の色などを指定する事もできる

# 最初の２つのペアが左上の座標、そして、次の２つのペアが右下の座標
# このメソッドを実行すると、その座標に収まるような楕円、もしくは円が描かれる

# canvas.create_oval(300 - 20, 200 - 20, 300 +20, 200 + 20)
# これによって「中心(300,200)、半径20」の円が描かれる
# キャンパスは「wibth = 600、height = 400」のオプションに設定して、幅600ピクセル、高さ400ピクセルにしてるので、丁度これでキャンパスの中心に円が描かれている事になる

#【円の色を変えてみよう】
# create_ovalメソッドやCanvasに備わる描画のためのメソッドは「黒い線」「塗りなし」で描く
# もし色を付けたいときや線幅を変えたいときは、width,outline、fillの各オプションを指定する
# なお、線を描きたくないときはwidthを0に、塗りたくないときはfillをNoneに指定する

# ・width:線の幅
# ・outline:線の色
# ・fill:塗りの色

# 色は「red」「blue」「green」など、基本的な色を文字列として指定できる
# ここでは「線なし(widthを0)」「赤色(fillを"red")」にして、赤い円にしてみる
# 次のように変更すると、線なしで赤く塗られた円が描かれるようになる

# canvas.create_oval(300 - 20, 200 - 20, 300 +20, 200 + 20, fill = "red", width = 0)
# 上記の「, fill = "red", width = 0)」が修正箇所

#【COLUMN】
# 指定できる色の一覧は下記のサイトに載っている
# https://www.colordic.org
