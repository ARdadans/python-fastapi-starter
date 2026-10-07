#!/usr/bin/env bash
set -e

REPO_URL="https://github.com/ARdadans/python-fastapi-starter.git"
APP_DIR="${APP_DIR:-python-fastapi-starter}"
BRANCH="${BRANCH:-main}"
HOST="${HOST:-0.0.0.0}"
PORT="${PORT:-8000}"

echo "=========================================="
echo " Python FastAPI Starter"
echo "=========================================="
echo "Repository : ${REPO_URL}"
echo "Directory  : ${APP_DIR}"
echo "Branch     : ${BRANCH}"
echo "Host       : ${HOST}"
echo "Port       : ${PORT}"
echo "=========================================="

if ! command -v git >/dev/null 2>&1; then
    echo "ERROR: git is not installed."
    exit 1
fi

if ! command -v python3 >/dev/null 2>&1; then
    echo "ERROR: python3 is not installed."
    exit 1
fi

echo "[1/5] Checking repository..."

if [ ! -d "${APP_DIR}/.git" ]; then
    echo "Cloning repository..."
    git clone --branch "${BRANCH}" "${REPO_URL}" "${APP_DIR}"
else
    echo "Repository already exists. Updating..."
    cd "${APP_DIR}"
    git fetch origin
    git checkout "${BRANCH}"
    git reset --hard "origin/${BRANCH}"
    cd ..
fi

cd "${APP_DIR}"

echo "[2/5] Checking Python..."
python3 --version

echo "[3/5] Creating virtual environment..."

if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

VENV_PYTHON=".venv/bin/python"
VENV_PIP=".venv/bin/pip"

if [ ! -x "${VENV_PYTHON}" ]; then
    echo "ERROR: virtual environment could not be created."
    exit 1
fi

echo "[4/5] Installing dependencies..."
"${VENV_PYTHON}" -m pip install --upgrade pip
"${VENV_PIP}" install -r requirements.txt

echo "[5/5] Starting application..."
echo "Server: http://${HOST}:${PORT}"
echo "Press Ctrl+C to stop."
echo "=========================================="

export HOST
export PORT

"${VENV_PYTHON}" run.py
