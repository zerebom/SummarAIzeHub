# SummarAIzeHub

SummarAIzeHub is a GitHub Action that uses advanced AI language models to automatically summarize GitHub issues when prompted by a comment containing `/summarize-issue`. This action is designed to make it easier for project maintainers and contributors to get the key points from long, complex issues without having to read through the entire thread.

## How to use

1. Add the `SummarAIzeHub` action to your GitHub repository by creating a new workflow file (e.g., `.github/workflows/summarize_issue.yml`) with the following content:

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

      - name: Run SummarAIzeHub
        uses: your-username/summarAIzeHub@v1
        with:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

2. Create the following secrets in your repository:
  - `GITHUB_TOKEN`: A personal access token with repo scope.
  - `OPENAI_API_KEY`: Your OpenAI API key to access the AI language model.

3. Whenever you or someone else comments `/summarize-issue` on an issue, the SummarAIzeHub action will be triggered and summarize the issue using an advanced AI language model.

For more information and customization options, please visit the [SummarAIzeHub GitHub repository](https://github.com/zerebom/SummarAIzeHub).

