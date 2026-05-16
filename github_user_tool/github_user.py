'''
写一个 github_user.py
命令行输入用户名
请求 GitHub 用户 API
输出用户名、主页、仓库数、粉丝数
请求失败时给出提示
'''

import argparse
import requests
import json

def analyze_url(username):
    try:
        url = f'https://api.github.com/users/{username}'
        response = requests.get(url, timeout=10)
    except requests.RequestException as e:
        print('网络请求失败', e)
        return None

    if response.status_code != 200:
        print('访问用户信息失败')
        print(response.status_code)
        return
    else:
        js = response.json()
        username = js['login']
        followers = js['followers']
        html = js['html_url']
        repos = js['public_repos']
    
    return{
        'username':username,
        'followers':followers,
        'html':html,
        'repos':repos
    }

def latest_repos(username):
    url = f'https://api.github.com/users/{username}/repos'

    params = {
        'sort': 'created',
        'direction': 'desc',
        'per_page': 5,
    }

    try:
        response = requests.get(url, params=params, timeout=10)
    except requests.RequestException as e:
        print('网络请求失败', e)
        return None
    
    if response.status_code == 404:
        print('用户不存在:', username)
        print(response.status_code)
        return None
    elif response.status_code != 200:
        print('访问用户信息失败')
        print(response.status_code)
        return None
    else:
        repos = response.json()
        repo_name = []
        for repo in repos:
            repo_name.append(repo['name'])
    
    return repo_name

def save_json(result, file='user.json'):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
    print('已保存为json')
    return

    
def main(username, save):
    user = analyze_url(username)
    repos = latest_repos(username)
    if user is None or repos is None:
        return

    result = {
        'user': user,
        'repos': repos,
    }
    
    print('用户名为:', user['username'])
    print('主页:', user['html'])
    print('粉丝数为:', user['followers'])
    print('仓库数:', user['repos'])
    print('最近的5个仓库名称:', repos)

    if save:
        save_json(result, save)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='访问用户空间'
    )
    parser.add_argument('-u', '--username', default='octocat', help='请输入访问用户名')
    parser.add_argument('-s', '--save', help='要保存的JSON文件名称')
    args = parser.parse_args()
    main(args.username, args.save)    