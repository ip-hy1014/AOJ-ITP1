"""
以下のような、たてH cm よこ W cm のチェック柄の長方形を描くプログラムを作成して下さい。

#.#.#.#.#.
.#.#.#.#.#
#.#.#.#.#.
.#.#.#.#.#
#.#.#.#.#.
.#.#.#.#.#
上図は、たて 6 cm よこ 10 cm の長方形を表しています。

長方形の左上が "#" となるように描いて下さい。
"""

while True:
  h, w = map(int, input().split())
  if h == 0 and w == 0:
    break
  for i in range(h):
    for j in range(w):
      if (i+j)%2 == 0:
        print("#", end="")
      else:
        print(".", end="")
    print()
  print()