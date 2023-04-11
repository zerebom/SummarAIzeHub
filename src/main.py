import os
import sys

from github import Github

from summarizer.summarizer import summarize_text


def main(repo_name, issue_number, comment_id, token):
    # 環境変数からAPIキーとリポジトリ情報を取得
    PERSONAL_ACCESS_TOKEN = os.getenv("PERSONAL_ACCESS_TOKEN") or token
    repo_name = os.getenv("GITHUB_REPOSITORY") or repo_name
    issue_number = os.getenv("GITHUB_ISSUE_NUMBER") or issue_number

    # GitHubクライアントの作成
    github_client = Github(PERSONAL_ACCESS_TOKEN)
    repo = github_client.get_repo(repo_name)
    issue = repo.get_issue(number=int(issue_number))

    # Issueの全コメントを取得
    comments = issue.get_comments()

    # コメントをまとめたテキストを作成
    comments_section = ""
    for comment in comments:
        comments_section += f"コメント（{comment.user.login}、投稿日：{comment.created_at.strftime('%Y-%m-%d')}）：\n{comment.body}\n\n"

    with open("./templates/prompt_template.txt", "r") as f:
        prompt_template = f.read()

    prompt = prompt_template.format(
        issue_title=issue.title, comments_section=comments_section
    )
    print(prompt)
    summarized_text = summarize_text(prompt)

    # 要約をIssueにコメントとして追加
    issue.create_comment(f"## Summary of Comments\n\n{summarized_text}")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
