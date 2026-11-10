#!/usr/bin/env bash
# Build the image and capture screenshots into docs/screenshots/.
# Usage: tools/screenshots/run.sh r1-home=/ [name=/path ...]
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/../.."
export MSYS_NO_PATHCONV=1
docker build -q -t top-movies-screenshots tools/screenshots >/dev/null
rm -rf .screenshot-work && mkdir .screenshot-work
tar --exclude=.git --exclude=.venv --exclude=.screenshot-work --exclude=instance --exclude=docs/screenshots -cf - . | tar -xf - -C .screenshot-work
mkdir -p docs/screenshots
docker run --rm -v "$PWD/.screenshot-work:/work" -v "$PWD/docs/screenshots:/out" top-movies-screenshots "$@"
rm -rf .screenshot-work
