# Import処理
import random

# ランダム処理

# リスト化
me = [
    "パー",
    "グー",
    "チョキ",
]

# 初期段階
print("************************")
print("じゃんけんを行います。")
print("1:パー\n2:グー\n3:チョキ")
print("と入力してください")
print("************************")
a = int(input("数字の入力："))

# 処理
def syori():

    # ランダムでリストmeから文字を返しnumに代入
    num = random.choice(me)

    # printに代入
    print("相手は{}をだしました。".format(num))

    # パーの処理
    if a == 1:
        if num == "パー":
            print("引き分けです。")
        if num == "チョキ":
            print("あなたの負けです。")
        if num == "グー":
            print("あなたの勝ちです")
    
    # グーの処理
    if a == 2:
        if num == "グー":
            print("引き分けです。")
        if num == "パー":
            print("あなたの負けです。")
        if num == "チョキ":
            print("あなたの勝ちです")
    
    # チョキの処理
    if a == 3:
        if num == "チョキ":
            print("引き分けです。")
        if num == "グー":
            print("あなたの負けです。")
        if num == "パー":
            print("あなたの勝ちです")
syori()