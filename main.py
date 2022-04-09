import pytchat
import time
import json
import codecs
import pandas as pd

chat = pytchat.create(video_id="jLtmBwCwF5Q")

with open("employee.csv", 'r+') as f:
    f.truncate(0)

df = pd.read_json(chat.get().json())
df.to_csv("employee.csv", encoding="cp932", errors="ignore", mode="a")

# while chat.is_alive():

#     df = pd.concat([df, pd.read_json(chat.get().json())], axis=0)
#     # CSV ファイル (employee.csv) として出力
#     print(df)
#     # df.to_csv("employee.csv", encoding="cp932",
#     #           errors="ignore", mode="a")


# # データフレームを作成
# df = pd.DataFrame([
#     ["0001", "John", "Engineer"],
#     ["0002", "Lily", "Sales"]],
#     columns=['id', 'name', 'job'])

# # CSV ファイル (employee.csv) として出力
# df.to_csv("employee.csv", encoding="shift_jis")
