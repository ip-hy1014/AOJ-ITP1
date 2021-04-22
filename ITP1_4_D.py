"""
n 個の整数 ai(i=1,2,...n)を入力し、それらの最小値、最大値、合計値を求めるプログラムを作成してください。
"""

n = int(input())
a = list(map(int, input().split()))
print("%d %d %d"%(min(a),max(a),sum(a)))