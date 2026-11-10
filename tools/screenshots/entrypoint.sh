#!/bin/sh
# Inside the container: /work is a copy of the repository, /out receives the PNG files.
# Usage: entrypoint.sh name=/path [name=/path ...]
set -eu
pip install --user --no-cache-dir -q /work
PATH="$HOME/.local/bin:$PATH" python /work/tools/screenshots/serve_demo.py &
SERVER=$!
trap 'kill $SERVER' EXIT
for _ in $(seq 1 40); do
  python -c "import urllib.request,sys; urllib.request.urlopen('http://127.0.0.1:5000/', timeout=1)" 2>/dev/null && break
  sleep 0.5
done
python /opt/capture.py http://127.0.0.1:5000 /out "$@"
