# GitHub Issue Summarizer

This GitHub Action utilizes the GPT-4 model by OpenAI to automatically summarize long GitHub issues when the `/summarize-issue` command is used in a comment. This helps make the issue discussion more accessible and digestible for later readers.

## Setup

1. Add this action to your repository by creating a new file in the `.github/workflows` directory, for example: `.github/workflows/summarize_issue.yml`. In this file, paste the following content:

```yaml
name: Summarize Issue

on:
  issue_comment:
    types: [created]

jobs:
  summarize_issue:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: "3.9"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install poetry
          poetry install

      - name: Run summarizer
        uses: your_username/gh-issue-summarizer@main
        with:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

2. Replace `your_username` with your GitHub username or organization name.

3. In your repository, go to Settings > Secrets and add the following secrets:
    - `GITHUB_TOKEN`: A GitHub personal access token with the `repo` scope.
    - `OPENAI_API_KEY`: Your OpenAI API key.

4. Save your changes.

Now, when a user comments `/summarize-issue` on an issue, the action will trigger and automatically generate a summary, which will be added as a new comment.

## Customization

You can customize the prompt template used by the GPT model by creating a custom prompt template file in your repository. The prompt template is the text sent to the GPT model along with the issue information, allowing the GPT model to generate an appropriate summary.

## Notes

- This action only triggers when a comment includes `/summarize-issue`. It will not run for other comments.
- Summaries are generated automatically and may not be perfect. Edits to the summaries may be required.
- Manage your OpenAI API key appropriately, as there may be costs associated with API requests. Storing the API key in the repository secrets ensures it will not be leaked to other users.

## License

This project is released under the MIT License. For more details, please refer to the [LICENSE](LICENSE) file.
