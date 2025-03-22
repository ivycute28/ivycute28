import random

# 隨機回答列表
responses = [
    "今天過得如何？",
    "你今天學到了什麼新知識呢？",
    "有什麼想法或問題想要問我嗎？",
    "有沒有什麼專案想要和我分享？",
    "你今天忙了什麼呢？",
    "很高興和你聊天！"
]

# 隨機選擇一個回應
def get_random_response():
    return random.choice(responses)

# 更新 README
def update_readme(response):
    with open("README.md", "r", encoding="utf-8") as file:
        readme_content = file.read()

    # 在 README 內更新機器人回應
    new_content = readme_content.replace(
        "🤖：想了解 Ivy 在 GitHub 的哪些專案呢？",
        f"🤖：{response}"
    )

    with open("README.md", "w", encoding="utf-8") as file:
        file.write(new_content)

if __name__ == "__main__":
    random_response = get_random_response()  # 隨機選擇回應
    update_readme(random_response)  # 更新 README
    print(f"🤖：{random_response}")  # 顯示機器人回應
