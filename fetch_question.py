import os
import json
from typing import Dict

import requests

headers = {
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

LANGUAGE = os.environ.get("LANGUAGE", "zh")


def get_question_of_today(region: str = "us") -> Dict:
    if region == "us":
        url = "https://leetcode.com/graphql/"
        key = "activeDailyCodingChallengeQuestion"
    else:
        url = "https://leetcode.cn/graphql/"
        key = "todayRecord"

    data = {
        "query": """
            query questionOfToday {
                %s {
                    question {
                        acRate
                        difficulty
                        freqBar
                        frontendQuestionId: questionFrontendId
                        paidOnly: isPaidOnly
                        status
                        title
                        titleSlug
                        topicTags {
                            name
                            id
                            slug
                        }
                    }
                }
            }
        """
        % key,
    }

    resp = requests.post(url, headers=headers, json=data)
    resp.raise_for_status()
    question_data = resp.json()["data"][key]
    if isinstance(question_data, list):
        question_data = question_data[0]
    return question_data["question"]


def get_question_content(title_slug: str, region: str = "us"):
    if LANGUAGE == "en":
        url = "https://leetcode.com/graphql/"
        query_question_content = """
        query questionContent($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            content
          }
        }
        """
        key = "content"
    else:
        url = "https://leetcode.cn/graphql/"
        query_question_content = """
        query questionTranslations($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            translatedTitle
            translatedContent
          }
        }
        """
        key = "translatedContent"

    variables = {"titleSlug": title_slug}
    resp = requests.post(
        url,
        headers=headers,
        json={"query": query_question_content, "variables": variables},
    )
    content = resp.json()["data"]["question"][key]
    return content


def save(question_data, output_filename="question.json"):
    with open(output_filename, "w") as f:
        json.dump(question_data, f)


def main():
    questions = []
    print("Questions of today are")
    for region in ["us", "zh"]:
        question_data = get_question_of_today(region)
        title_slug = question_data["titleSlug"]
        print("\t%s (%s)" % (title_slug, region))
        question_data["content"] = get_question_content(title_slug, region)
        if question_data["acRate"] > 1:
            question_data["acRate"] = float(question_data["acRate"]) / 100
        questions.append(question_data)
    save(questions)


if __name__ == "__main__":
    main()
