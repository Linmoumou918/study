# Training Log Analyzer

这是一个用于分析 AI 训练日志的 Python 命令行工具。

本项目可以从 `train.log` 中提取训练过程中的 `epoch`、`loss` 和 `acc` 信息，并自动生成 CSV 文件、训练曲线图和实验分析结果。

本项目是 Python 学习中的第二个小项目，主要用于练习：

- 正则表达式
- 文件读取
- pandas 数据分析
- matplotlib 画图
- CSV 文件保存
- 命令行参数 argparse
- AI 实验日志处理

---

## 功能介绍

程序可以完成以下功能：

- 读取训练日志文件
- 提取每一轮训练的 `epoch / loss / acc`
- 保存为 CSV 文件
- 绘制 loss 曲线
- 绘制 acc 曲线
- 输出最小 loss
- 输出最高 acc
- 输出最佳 epoch
- 判断 loss 是否整体下降

---

## 项目文件

```text
log_analyzer.py      # 主程序
train.log            # 示例训练日志
train.csv            # 程序生成的 CSV 文件
loss_curve.png       # 程序生成的 loss 曲线
acc_curve.png        # 程序生成的 acc 曲线
README.md            # 项目说明文档
requirements.txt     # 项目依赖