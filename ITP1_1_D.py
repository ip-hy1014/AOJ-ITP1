"""
秒単位の時間 S が与えられるので、h:m:s の形式へ変換して出力してください。
ここで、h は時間、m は 60 未満の分、s は 60 未満の秒とします。
"""

s = int(input())
h = s//3600
m = s%3600//60
s = s%60
print(f"{h}:{m}:{s}")