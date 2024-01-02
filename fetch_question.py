import requests
import json

url = 'https://leetcode.com/graphql/'
headers = {
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
data = {
    "query": """
        query questionOfToday {
            activeDailyCodingChallengeQuestion {
                date
                userStatus
                link
                question {
                    acRate
                    difficulty
                    freqBar
                    frontendQuestionId: questionFrontendId
                    isFavor
                    paidOnly: isPaidOnly
                    status
                    title
                    titleSlug
                    hasVideoSolution
                    hasSolution
                    topicTags {
                        name
                        id
                        slug
                    }
                }
            }
        }
    """,
    "variables": {},
    "operationName": "questionOfToday"
}

response = requests.post(url, headers=headers, json=data)
question_data = response.json()['data']['activeDailyCodingChallengeQuestion']
"""
{'data': {'activeDailyCodingChallengeQuestion': {'date': '2024-01-02', 'userStatus': 'NotStart', 'link': '/problems/convert-an-array-into-a-2d-array-with-conditions/', 'question': {'acRate': 87.37286733432606, 'difficulty': 'Medium', 'freqBar': None, 'frontendQuestionId': '2610', 'isFavor': False, 'paidOnly': False, 'status': None, 'title': 'Convert an Array Into a 2D Array With Conditions', 'titleSlug': 'convert-an-array-into-a-2d-array-with-conditions', 'hasVideoSolution': False, 'hasSolution': True, 'topicTags': [{'name': 'Array', 'id': 'VG9waWNUYWdOb2RlOjU=', 'slug': 'array'}, {'name': 'Hash Table', 'id': 'VG9waWNUYWdOb2RlOjY=', 'slug': 'hash-table'}]}}}}
"""
print(question_data)

with open('question.json', 'w') as file:
    json.dump(question_data, file)
