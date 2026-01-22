FROM python:3.14-slim-trixie

RUN apt update && \
  apt install -y --no-install-recommends bash git curl wget ca-certificates && \
  pip install uv && \
  rm -rf /var/lib/apt/lists/*

WORKDIR /tdd/python

# 依存関係のインストール
COPY ./python/pyproject.toml ./python/uv.lock ./
RUN uv sync --frozen
