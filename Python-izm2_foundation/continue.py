# 【continue】
# Pythonで現在のループを中断し、次の繰り替し処理を行う場合はcontinueを使用します。ここでいう中断は、ループそのものを中断するのではなく、continue以降の処理をスキップする事を指します。
# 
# 《continueの基礎》
# 言葉での説明が少し難しいので実際に見た方が良いでしょう。次の例は100回繰り返し処理を行うfor文です。値が10で割り切れないものは、printを実行させずに次の繰り返し処理を行っています。
# 
# for num in range(100):
# 
#     if num % 10:
#         continue
# 
#     print(num)
# 
# 
# 《実行結果》
# 0
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90
# 
# 実行結果から10で割り切れる数値のみ出力されていることがわかります。
# 
# 