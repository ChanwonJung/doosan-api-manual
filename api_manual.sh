#!/usr/bin/env bash
set -euo pipefail

# Determine script location, repository root, and Sphinx paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="${SCRIPT_DIR}"

SRC_DIR="${ROOT_DIR}/source"        # Sphinx source (conf.py, index.rst, ...)
OUT_DIR="${ROOT_DIR}/_site"
PORT="${1:-8000}"                   # web server port (default: 8000)

# Check if sphinx_multiversion exists
if ! python3 -m sphinx_multiversion --help >/dev/null 2>&1; then
  echo "[!] sphinx_multiversion is not installed."
  echo "    Install it with:"
  echo "      pip install sphinx-multiversion"
  exit 1
fi

# Clean previous build
echo "[*] Cleaning previous build..."
rm -rf "${OUT_DIR}"

# Build documentation
echo "[*] Building documentation from ${SRC_DIR} ..."
python3 -m sphinx_multiversion "${SRC_DIR}" "${OUT_DIR}"

# Serve documentation
cd "${OUT_DIR}"
URL="http://localhost:${PORT}/GL013301/index.html"

echo ""
echo "=============================================="
echo " Serving documentation at ${URL}"
echo " Directory: ${OUT_DIR}"
echo " Press Ctrl+C to stop the server."
echo "=============================================="
echo ""

# Automatically open in browser (Linux/WSL/macOS)
if command -v xdg-open >/dev/null 2>&1; then
  (sleep 1 && xdg-open "${URL}" >/dev/null 2>&1) &
elif command -v open >/dev/null 2>&1; then
  # macOS support
  (sleep 1 && open "${URL}") &
fi

# Start the local web server
python3 -m http.server "${PORT}"
