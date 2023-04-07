import os

from github import Github

from src.summarizer.summarizer import summarize_text


def main():
    # 環境変数からAPIキーとリポジトリ情報を取得
    github_token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("GITHUB_REPOSITORY")
    issue_number = os.getenv("GITHUB_ISSUE_NUMBER")

    # GitHubクライアントの作成
    github_client = Github(github_token)
    repo = github_client.get_repo(repo_name)
    issue = repo.get_issue(number=int(issue_number))

    # Issueの全コメントを取得
    comments = issue.get_comments()

    # コメントをまとめたテキストを作成
    comments_text = "\n\n".join(comment.body for comment in comments)

    # コメントの要約を作成
    summarized_text = summarize_text(comments_text)

    # 要約をIssueにコメントとして追加
    issue.create_comment(f"## Summary of Comments\n\n{summarized_text}")

if __name__ == "__main__":
    main()
