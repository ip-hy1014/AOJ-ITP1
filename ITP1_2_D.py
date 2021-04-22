"""
長方形の中に円が含まれるかを判定するプログラムを作成してください。次のように、長方形は左下の頂点を原点とし、右上の頂点の座標 (W,H) が与えられます。
また、円はその中心の座標 (x,y) と半径 r で与えられます。
"""

W, H, x, y, r = map(int,input().split())
print("Yes" if x>=r and x+r<=W and y>=r and y+r<=H else "No")