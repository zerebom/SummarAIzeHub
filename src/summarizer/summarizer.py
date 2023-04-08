import os

import openai


def summarize_text(text, api_key=None):
    # APIキーの設定
    openai.api_key = api_key or os.getenv("OPENAI_API_KEY")

    # 要約のリクエスト
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Summarize the following text:\n\n{text}",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # 要約されたテキストを取得
    summarized_text = response.choices[0].text.strip()
    return summarized_text

def dummy_summarize_text(text, api_key=None):
    print(text)
    return "dummy"

