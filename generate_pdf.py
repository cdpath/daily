import json
import pdfkit

with open('question.json', 'r') as file:
    question_data = json.load(file)

title = question_data["question"]['title']
difficulty = question_data["question"]['difficulty']
acRate = question_data["question"]['acRate']
topicTags = ', '.join([tag['name'] for tag in question_data["question"]['topicTags']])

content = question_data['content']

html_content = f"""
<h1>{title}</h1>
<div><strong>Difficulty:</strong> {difficulty}</div>
<div><strong>Acceptance Rate:</strong> {acRate}%</div>
<div><strong>Topic Tags:</strong> {topicTags}</div>
<hr>
{content}
"""

print(html_content)
# 创建PDF
pdf_file = "LeetCode_Question.pdf"
pdfkit.from_string(html_content, pdf_file)
