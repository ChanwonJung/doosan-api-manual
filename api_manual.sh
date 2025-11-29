#!/usr/bin/env bash
set -euo pipefail

# Determine script location, repository root, and Sphinx paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="${SCRIPT_DIR}"

SRC_DIR="${ROOT_DIR}/source"        # Sphinx source (conf.py, index.rst, ...)
OUT_DIR="${ROOT_DIR}/build/html"    # Build output directory
PORT="${1:-8000}"                   # web server port (default: 8000)

# Check if sphinx-build is available
if ! command -v sphinx-build >/dev/null 2>&1; then
  echo "[!] sphinx-build not found."
  echo "    Install one of:"
  echo "      sudo apt install python3-sphinx"
  echo "      pip install sphinx sphinx_rtd_theme"
  exit 1
fi

# Clean previous build
echo "[*] Cleaning previous build..."
rm -rf "${OUT_DIR}"

# Build documentation
echo "[*] Building documentation from ${SRC_DIR} ..."
sphinx-build -b html "${SRC_DIR}" "${OUT_DIR}"

# Serve documentation
cd "${OUT_DIR}"
URL="http://localhost:${PORT}/index.html"

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
