FROM maven:3.9.12-eclipse-temurin-25

RUN apt update && \
  apt install -y --no-install-recommends bash git curl wget ca-certificates && \
  rm -rf /var/lib/apt/lists/*

WORKDIR /tdd/java

# 依存関係のインストール
# COPY ./java/pom.xml .
# RUN mvn dependency:go-offline
