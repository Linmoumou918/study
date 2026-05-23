import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
import json

# 明确读取当前 Python 文件所在目录下的 .env
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

def ask_ai(question:str, messages:list[dict[str,str]]) -> str:
    messages.append({'role': 'user', 'content': question})
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages
        )
    except Exception as e:
        messages.pop()
        return f'调用 API 失败: {e}'
    
    answer = response.choices[0].message.content
    messages.append({'role': 'assistant', 'content': answer})
    return answer

def save_history(messages, file='chat_history.json'):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)
    return

if __name__ == '__main__':
    print('AI助手已启用，输入quit退出')

    messages = [
        {'role': 'system', 'content': '你是一个耐心、清晰、适合初学者的 Python 老师'}
    ]

    while True:
        question = input('你:')
        if question.strip().lower() in ['exit', 'quit', 'q']:
            save_history(messages)
            print('已退出')
            break

        if not question.strip():
            continue

        answer = ask_ai(question, messages)
        print('AI:', answer)