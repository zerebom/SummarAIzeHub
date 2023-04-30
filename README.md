# SummarAIzeHub
- [Japanese README](README_ja.md)

SummarAIzeHub automatically summarizes an issue on GitHub when `/summarize-issue` is written in an issue comment. This action generates summaries using OpenAI's GPT model.
## Prerequisites

1. You need access to the OpenAI API. First, [sign up for OpenAI](https://platform.openai.com/account/api-keys) and obtain an API key.
2. Add `OPENAI_API_KEY` and `PERSONAL_ACCESS_TOKEN` to your GitHub repository secrets. The `OPENAI_API_KEY` is obtained in the previous step. Use `${{ secrets.PERSONAL_ACCESS_TOKEN }}` for the `PERSONAL_ACCESS_TOKEN`.

## Installation

1. Create a `.github/workflows` directory in your repository and create a file named `summarize_issue.yml` within it.
2. Add the following code to `summarize_issue.yml`:

```yaml
name: Summarize Issue

on:
  issue_comment:
    types: [created]

jobs:
  summarize_issue:
    if: startsWith(github.event.comment.body, '/summarize-issue')
    runs-on: ubuntu-latest
    name: Checkout code & SummarAIze
    steps:
      - uses: actions/checkout@v3
      - uses: zerebom/SummarAIzeHub@main
        with:
          PERSONAL_ACCESS_TOKEN: ${{ secrets.PERSONAL_ACCESS_TOKEN }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}

```

Replace `your-username` with the GitHub username hosting the action.

Now, SummarAIzeHub is installed in your repository. When a comment contains `/summarize-issue`, a summary will be automatically generated.

## Using Custom Prompt Templates

By default, the prompt template is stored in `path/to/default/prompt_template.txt`. If you want to use a custom prompt template, add `prompt_template_path` to the `with` section as follows:

```yaml
with:
  PERSONAL_ACCESS_TOKEN: ${{ secrets.PERSONAL_ACCESS_TOKEN }}
  openai_api_key: ${{ secrets.OPENAI_API_KEY }}
  prompt_template_path: 'path/to/your/custom_template.txt'
```

Using a custom template allows you to freely customize the format and questions of the summary. The prompt template is text sent to the GPT model along with the issue information, allowing GPT to generate an appropriate summary.

## Notes

- This action is triggered only when the comment contains `/summarize-issue`. It will not be executed for other comments.
- Summaries are automatically generated and may not be perfect. Corrections may be necessary for the summaries.
- Manage your OpenAI API key properly, as it is associated with costs for API requests. Storing the API key in the repository's secrets ensures that the key will not be leaked to other users.

## License

This project is released under the Apache License. For more information, see the [LICENSE](LICENSE) file.
