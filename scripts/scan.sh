#!/usr/bin/env bash
# Run opengrep over src/, tests/ and tools/ with the project rules. Run before every push.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
OPENGREP="${OPENGREP:-$HOME/.opengrep/cli/latest/opengrep.exe}"
[[ -x "$OPENGREP" ]] || OPENGREP="$HOME/.opengrep/cli/latest/opengrep"
"$OPENGREP" scan --config scripts/opengrep-rules.yml --error --quiet src tests tools
echo "opengrep: no findings"
