param(
    [switch]$Clean = $true,
    [string]$Version = "1.0.0"
)

$ErrorActionPreference = 'Stop'
Set-Location -Path "$PSScriptRoot\.."
$packTmp = ".\.packtmp"
$distOut = Join-Path $packTmp "dist"
$workOut = Join-Path $packTmp "build"

Write-Host "[1/6] Installing build dependencies..."
python -m pip install -r requirements-build.txt

Write-Host "[2/6] Generating app icon..."
python ".\scripts\generate_icon.py"

if ($Clean) {
    Write-Host "[3/6] Cleaning old artifacts..."
    if (Test-Path $packTmp) { Remove-Item $packTmp -Recurse -Force }
    if (Test-Path release) { Remove-Item release -Recurse -Force }
}

Write-Host "[4/6] Building distributable folder..."
python -m PyInstaller --noconfirm --clean --workpath "$workOut" --distpath "$distOut" snake.spec

Write-Host "[5/6] Building installer if Inno Setup exists..."
$innoCmd = Get-Command iscc -ErrorAction SilentlyContinue
$innoPath = $null
if ($innoCmd) {
    $innoPath = $innoCmd.Source
} elseif (Test-Path "C:\Program Files (x86)\Inno Setup 6\ISCC.exe") {
    $innoPath = "C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
} elseif (Test-Path "$env:LOCALAPPDATA\Programs\Inno Setup 6\ISCC.exe") {
    $innoPath = "$env:LOCALAPPDATA\Programs\Inno Setup 6\ISCC.exe"
}
$setupPath = $null
if ($innoPath) {
    & $innoPath ".\installer\snake.iss"
    $candidateSetupPath = ".\installer\output\SnakeGameSetup.exe"
    if (Test-Path $candidateSetupPath) {
        $setupPath = $candidateSetupPath
        Write-Host "Installer created: $setupPath"
    } else {
        Write-Host "Inno Setup ran but Setup.exe was not generated."
    }
} else {
    Write-Host "Inno Setup not found. Runtime package is ready: dist\\SnakeGame"
    Write-Host "Install Inno Setup and run this script again to build Setup.exe"
}

Write-Host "[6/6] Preparing release artifacts..."
$releaseDir = ".\release\v$Version"
New-Item -ItemType Directory -Path $releaseDir -Force | Out-Null

$zipPath = Join-Path $releaseDir "SnakeGame-v$Version-win64.zip"
Compress-Archive -Path ".\.packtmp\dist\SnakeGame\*" -DestinationPath $zipPath -Force

if ($setupPath -and (Test-Path $setupPath)) {
    Copy-Item $setupPath (Join-Path $releaseDir "SnakeGameSetup-v$Version.exe") -Force
}

Write-Host "Done."
