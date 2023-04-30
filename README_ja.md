# SummarAIzeHub
- [English README](README_en.md)


SummarAIzeHub は、GitHub の issue コメントに `/summarize-issue` と記述されたときに、その issue を自動的に要約します。このアクションは、OpenAI の GPT モデルを使用して要約を生成します。
## 必要な準備

1. OpenAI API へのアクセスが必要です。まず、[OpenAI にサインアップ](https://platform.openai.com/account/api-keys)して API キーを取得してください。
2. GitHub のリポジトリのシークレットに `OPENAI_API_KEY` と `PERSONAL_ACCESS_TOKEN` を追加します。`OPENAI_API_KEY` は前の手順で取得したものです。`PERSONAL_ACCESS_TOKEN` には、`${{ secrets.PERSONAL_ACCESS_TOKEN }}` を使用してください。

## インストール方法

1. リポジトリに `.github/workflows` ディレクトリを作成し、その中に `summarize_issue.yml` という名前のファイルを作成します。
2. 以下のコードを `summarize_issue.yml` に追加します。

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

これで、SummarAIzeHub がリポジトリにインストールされました。コメントに `/summarize-issue` が含まれると、要約が自動的に生成されます。

## カスタムプロンプトテンプレートの使用

デフォルトでは、プロンプトテンプレートは `path/to/default/prompt_template.txt` に格納されています。カスタムプロンプトテンプレートを使用する場合は、以下のように `with` セクションに `prompt_template_path` を追加してください。

```yaml
with:
  PERSONAL_ACCESS_TOKEN: ${{ secrets.PERSONAL_ACCESS_TOKEN }}
  openai_api_key: ${{ secrets.OPENAI_API_KEY }}
  prompt_template_path: 'path/to/your/custom_template.txt'
```

カスタムテンプレートを使用すると、要約の形式や質問などを自由にカスタマイズできます。プロンプトテンプレートは、issue の情報とともに GPT モデルに送信されるテキストです。これにより、GPT が適切な要約を生成できます。

## 注意事項

- このアクションは、コメントが `/summarize-issue` を含む場合にのみトリガーされます。その他のコメントでは実行されません。
- 要約は自動生成されるため、完璧ではない場合があります。要約に対して修正が必要な場合があります。
- OpenAI API キーは、API へのリクエストに関連するコストが発生するため、適切に管理してください。リポジトリのシークレットに API キーを格納することで、キーが他のユーザーに漏れることはありません。

## ライセンス

このプロジェクトは Apache ライセンスの下で公開されています。詳細については、[LICENSE](LICENSE) ファイルを参照してください。
