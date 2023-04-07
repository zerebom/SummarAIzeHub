from github import Github

# GitHub APIトークンを設定
g = Github("YOUR_GITHUB_API_TOKEN")

# リポジトリの情報
owner = "OWNER_NAME"
repo = "REPOSITORY_NAME"
issue_number = "ISSUE_NUMBER"

# Issue情報を取得
repository = g.get_repo(f"{owner}/{repo}")
issue = repository.get_issue(number=issue_number)

print(issue)
