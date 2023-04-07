#!/bin/bash

# ディレクトリ構造の作成
mkdir -p actions src/summarizer tests

# ファイルの作成
touch actions/main_workflow.yml \
      src/__init__.py \
      src/main.py \
      src/summarizer/__init__.py \
      src/summarizer/summarizer.py \
      tests/__init__.py \
      tests/test_summarizer.py
