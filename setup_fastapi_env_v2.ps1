param(
    [string]$ProjectPath = ".",
    [switch]$StartServer
)
$ErrorActionPreference = "Stop"

# Allow script to run in this session only
try { Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force | Out-Null } catch {}

# Resolve project path
$proj = Resolve-Path $ProjectPath

if (!(Test-Path "$proj\requirements.txt")) {
    Write-Error "requirements.txt not found in $proj. Run this from your project folder or pass -ProjectPath 'C:\path\to\project'."
}

# Find Python (prefer py launcher)
$pythonCandidates = @("py -3.12", "py -3.11", "py", "python")
$python = $null
foreach ($cmd in $pythonCandidates) {
    try {
        & $cmd --version *> $null
        if ($LASTEXITCODE -eq 0) { $python = $cmd; break }
    } catch {}
}
if (-not $python) {
    Write-Error "Python not found. Install Python 3.11+ and re-run."
}

Push-Location $proj

# Create venv if missing
if (!(Test-Path ".venv")) {
    Write-Host "Creating virtual environment (.venv)..." -ForegroundColor Cyan
    & $python -m venv .venv
}

# Activate venv
Write-Host "Activating virtual environment..." -ForegroundColor Cyan
. ".\.venv\Scripts\Activate.ps1"

# Upgrade pip
Write-Host "Upgrading pip..." -ForegroundColor Cyan
python -m pip install --upgrade pip

# Install requirements
Write-Host "Installing project dependencies..." -ForegroundColor Cyan
pip install -r requirements.txt

# Quick import check (single line -c to avoid heredocs)
Write-Host "Verifying packages..." -ForegroundColor Cyan
python -c "import fastapi, uvicorn, pytest; print('All packages import successfully.')" | Out-Host

# Run tests
Write-Host "`nRunning tests (pytest -q)..." -ForegroundColor Cyan
pytest -q
if ($LASTEXITCODE -ne 0) {
    Write-Host "`n⚠️  Tests did not pass. Check errors above." -ForegroundColor Yellow
} else {
    Write-Host "`n✅ Environment ready. Tests passed." -ForegroundColor Green
}

Write-Host "`nTo start the API locally:" -ForegroundColor Cyan
Write-Host "  uvicorn app.main:app --reload" -ForegroundColor White
Write-Host "Then visit http://127.0.0.1:8000/healthz" -ForegroundColor White

if ($StartServer) {
    Write-Host "`nStarting uvicorn dev server (Ctrl+C to stop)..." -ForegroundColor Cyan
    uvicorn app.main:app --reload
}

Pop-Location
