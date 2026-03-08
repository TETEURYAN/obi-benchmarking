#!/bin/bash
set -e

echo "🚀 Starting Piston environment..."

# 1. Start Docker containers
cd piston
docker compose up -d
cd ..

# 2. Wait for Piston to be ready and install languages
echo "⏳ Waiting for Piston API to be ready..."
uv run scripts/setup_piston.py

echo "✅ Environment is ready!"
