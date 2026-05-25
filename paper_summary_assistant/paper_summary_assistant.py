import os
from pathlib import Path
import json
from dotenv import load_dotenv
from openai import OpenAI

env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

api_key = os.getenv('ARK_API_KEY')
base_url = os.getenv('ARK_BASE_URL')
model = os.getenv('ARK_MODEL')

if not api_key:
    raise RuntimeError('没有读取到 ARK_API_KEY ，请检查 .env 文件')
if not base_url:
    raise RuntimeError('没有读取到 ARK_BASE_URL , 请检查 .env 文件')
if not model:
    raise RuntimeError('没有读取到 ARK_MODEL ，请检查 .env 文件')

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

def build_prompt(abstract):
    return f'''
请阅读下面的论文摘要，并提取以下信息：

1. 研究问题
2. 方法
3. 数据集
4. 主要贡献
5. 局限性

请严格使用 JSON 格式输出，不要输出多余解释。
JSON 字段名必须使用：

research_problem
method
dataset
contribution
limitation

如果摘要中没有明确提到某一项，请填写 "未明确提及"。

论文摘要：
{abstract}
'''

def ai_work(abstract):
    try:
        response = client.chat.completions.create(
            model = model,
            messages = [
                {'role': 'system', 'content': '你是一个严谨的论文阅读助手，擅长从论文摘要中提取结构化信息。'},
                {'role': 'user', 'content': build_prompt(abstract)}
            ],
        )
    except Exception as e:
        print('调用 API 失败:', e)
        return None
    
    return response.choices[0].message.content

def save_as_json(message, file='result.json'):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(message, f, ensure_ascii=False, indent=4)
    print('已保存')

if __name__ == '__main__':
    print('请输入论文摘要，输入 END 结束：')
    lines = []
    while True:
        line = input()
        if line.strip() == 'END':
            break
        lines.append(line)

    abstract = '\n'.join(lines)
    answer = ai_work(abstract)
    if answer is None:
        print('未提取到相关信息')
    else:
        try:
            result = json.loads(answer)
            save_as_json(result)
        except json.JSONDecodeError:
            print('模型返回的内容不是合法 JSON ，已按文本保存')
            save_as_json({'raw_answer': answer})
        print(answer)