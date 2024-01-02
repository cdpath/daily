from jinja2 import Template
import os
import subprocess
import json

with open("question.json", "r") as file:
    question_data = json.load(file)

# 从响应中提取问题数据
question_data = response["data"]["activeDailyCodingChallengeQuestion"]["question"]
date = response["data"]["activeDailyCodingChallengeQuestion"]["date"]
link = question_data["link"]
title = question_data["title"]
difficulty = question_data["difficulty"]
acRate = question_data["acRate"]
topicTags = question_data["topicTags"]

# 读取 LaTeX 模板
with open("template.tex", "r") as file:
    template = Template(file.read())

# 使用问题数据渲染 LaTeX 模板
rendered_tex = template.render(
    date=date,
    link=link,
    title=title,
    difficulty=difficulty,
    acRate=acRate,
    topicTags=topicTags,
)

# 将渲染的 LaTeX 写入新文件
with open("question.tex", "w") as file:
    file.write(rendered_tex)

# 调用 LaTeX 引擎生成 PDF
subprocess.run(["pdflatex", "question.tex"])

# 清理生成的辅助文件
for ext in (".aux", ".log"):
    os.remove(f"question{ext}")
