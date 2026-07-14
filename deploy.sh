#!/bin/bash

echo "========== DEPLOY START =========="

cd /Users/mohammedadam/Downloads/engineering-ai-assistant-rag

git pull origin main

docker compose down

docker compose up -d --build

echo "========== DEPLOY COMPLETE =========="