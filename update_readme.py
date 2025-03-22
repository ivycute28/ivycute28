import random

# 可能的機器人回應
responses = [
    "🤖：你好！有什麼想問的嗎？",
    "🤖：今天天氣不錯，適合來寫點程式喔！",
    "🤖：你最喜歡的程式語言是什麼呢？",
    "🤖：我會慢慢學習變得更聰明！",
    "🤖：想了解 Ivy 在 GitHub 的哪些專案呢？"
]

# 讀取當前 README
with open("README.md", "r", encoding="utf-8") as file:
    lines = file.readlines()

# 檢查是否已經有機器人留言，若有則替換
new_lines = []
found_bot = False
for line in lines:
    if "🤖：" in line:
        new_lines.append(random.choice(responses) + "\n")
        found_bot = True
    else:
        new_lines.append(line)

# 如果 README 還沒機器人回應，就加一行
if not found_bot:
    new_lines.append("\n" + random.choice(responses) + "\n")

# 寫回 README
with open("README.md", "w", encoding="utf-8") as file:
    file.writelines(new_lines)
