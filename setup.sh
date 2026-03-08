#!/bin/bash
set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 Starting Whole Project Setup...${NC}"

# 1. Check for required system tools
echo -e "${YELLOW}🔍 Checking system dependencies...${NC}"
command -v docker >/dev/null 2>&1 || { echo -e "${RED}❌ docker is not installed. Please install it first.${NC}" >&2; exit 1; }
command -v docker compose >/dev/null 2>&1 || { echo -e "${RED}❌ docker compose is not installed. Please install it first.${NC}" >&2; exit 1; }
command -v uv >/dev/null 2>&1 || { echo -e "${RED}❌ uv is not installed. Installing it now...${NC}" ; curl -LsSf https://astral.sh/uv/install.sh | sh; }

# 2. Handle Environment Variables
if [ ! -f .env ]; then
    echo -e "${YELLOW}📄 Creating .env from .env.example...${NC}"
    cp .env.example .env
    echo -e "${RED}⚠️  ACTION REQUIRED: Please edit your .env file and add your OPENAI_API_KEY.${NC}"
fi

# 3. Python Dependency Sync
echo -e "${YELLOW}📦 Syncing Python dependencies...${NC}"
uv sync

# 4. Start Piston Engine
echo -e "${YELLOW}🐳 Starting Piston Docker containers...${NC}"
cd piston
docker compose up -d
cd ..

# 5. Language Configuration (Retry logic included)
echo -e "${YELLOW}⏳ Configuring Piston runtimes...${NC}"
# Wait for Piston to be ready and install languages
uv run scripts/setup_piston.py

echo -e "\n${GREEN}✅ Project setup complete!${NC}"
echo -e "${GREEN}-----------------------------------${NC}"
echo -e "To start the tutor, run:"
echo -e "${YELLOW}uv run streamlit run app/main.py${NC}"
echo -e "${GREEN}-----------------------------------${NC}"
