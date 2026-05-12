'''
写一个 github_user.py
命令行输入用户名
请求 GitHub 用户 API
输出用户名、主页、仓库数、粉丝数
请求失败时给出提示
'''

import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())