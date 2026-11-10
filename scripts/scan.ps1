# Run opengrep over src/, tests/ and tools/ with the project rules. Run before every push.
$ErrorActionPreference = 'Stop'
Set-Location (Join-Path $PSScriptRoot '..')
$opengrep = Join-Path $HOME '.opengrep\cli\latest\opengrep.exe'
& $opengrep scan --config scripts/opengrep-rules.yml --error --quiet src tests tools
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Write-Output 'opengrep: no findings'
