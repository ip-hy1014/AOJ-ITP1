"""
各データセットごとに、以下の形式で x を出力して下さい
Case i: x
ここで、i は１から始まるデータセットの番号を示します。Caseと番号 iの間に１つの空白を入れて下さい。また、:（コロン）と整数 x の間に１つの空白を入れて下さい。

入力は複数のデータセットから構成されています。各データセットは１つの整数 x を含む１行から構成されています。
x が 0 のとき入力の終わりを示し、このデータセットに対する出力を行ってはいけません。
"""

case = 1
while True:
    x = int(input())
    if x == 0:
        break
    else:
        print("Case %d: %d" % (case,x))
        case+=1