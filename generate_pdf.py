import json
import pdfkit

with open('question.json', 'r') as file:
    questions = json.load(file)

html_content = ''
for question in questions:
    title = question['frontendQuestionId'] + ". " + question["title"]
    content = question['content']
    difficulty = question['difficulty']
    acRate = question['acRate']
    topicTags = ', '.join([tag['name'] for tag in question['topicTags']])

    # 创建HTML文档
    html_content += f"""
    <html>
    <head>
    <meta charset="UTF-8">
    <style>
        h1 {{font-size: 24px;}}
        div {{margin-bottom: 10px;}}
        body {{ font-family: "Source Han Serif CN", "Source Han Serif", serif; }}
    </style>
    </head>
    <body>
    <h1>{title}</h1>
    <div><strong>Difficulty:</strong> {difficulty}</div>
    <div><strong>Acceptance Rate:</strong> {acRate}%</div>
    <div><strong>Tags:</strong> {topicTags}</div>
    <hr>
    {content}
    <div style='page-break-after: always;'></div>
    </body>
    </html>
    """

pdf_file = "LeetCode_Question.pdf"
pdfkit.from_string(html_content, pdf_file)
