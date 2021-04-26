"""
以下のような、たてH cm よこ W cm の枠を描くプログラムを作成して下さい。

##########
#........#
#........#
#........#
#........#
##########
上図は、たて 6 cm よこ 10 cm の枠を表しています。
"""

while True:
  h, w = map(int, input().split())
  if h == 0 and w == 0:
    break
  for i in range(h):
    for j in range(w):
      if i == 0 or i == h-1 or j == 0 or j == w-1:
        print("#", end = "")
      else:
        print(".", end = "")
    print()
  print()
