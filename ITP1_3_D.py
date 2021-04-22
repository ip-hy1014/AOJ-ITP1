"""
３つの整数 a、b、c を読み込み、a から b までの整数の中に、c の約数がいくつあるかを求めるプログラムを作成してください。
"""

a,b,c = map(int, input().split())
count = 0
for i in range(a, b+1):
    if c % i == 0:
        count += 1
print(count)