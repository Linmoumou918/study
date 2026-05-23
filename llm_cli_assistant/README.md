# LLM CLI Assistant

这是一个基于 Python 编写的 LLM API 命令行助手。

用户可以在命令行中输入问题，程序会调用大模型 API，并返回模型回答。本项目使用 `.env` 管理 API Key，支持 system prompt、多轮对话和对话记录保存。

本项目是 Python 学习中的第三个小项目，主要用于练习：

- LLM API 调用
- API Key 管理
- `.env` 配置文件
- `python-dotenv`
- OpenAI 兼容接口调用
- Prompt / System Prompt
- 多轮对话
- JSON 对话记录保存
- 基础错误处理

---

## 功能介绍

程序支持以下功能：

- 从命令行启动 AI 助手
- 用户连续输入问题
- 调用 LLM API 获取回答
- 支持 system prompt 设定助手角色
- 支持多轮对话上下文
- 支持输入 `quit` / `exit` / `q` 退出
- 支持保存对话记录为 JSON 文件
- 使用 `.env` 管理 API Key，避免密钥写死在代码中

---

## 项目文件

```text
llm_cli.py           # 主程序
.env                 # 本地 API 配置文件，不上传 GitHub
.gitignore           # Git 忽略规则
requirements.txt     # 项目依赖
README.md            # 项目说明文档
chat_history.json    # 程序运行后生成的对话记录，可选