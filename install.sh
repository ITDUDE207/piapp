#!/bin/bash
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
chmod +x "$DIR"/desktop "$DIR"/myapp.py "$DIR"/install.sh || true

