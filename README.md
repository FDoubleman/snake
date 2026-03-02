# Snake Game

A modular Snake game built with Python + Pygame.

## Project Layout

- `main.py`: app entry point
- `config.py`: window/grid/theme/difficulty config
- `assets.py`: shared assets (fonts)
- `entities.py`: gameplay entities (`Snake`, `Food`)
- `game.py`: game loop and state machine
- `screens/`: UI screens
- `snake.spec`: PyInstaller spec file
- `scripts/build_windows.ps1`: one-click Windows build script
- `installer/snake.iss`: Inno Setup installer script

## Run Locally

```bash
pip install -r requirements.txt
python main.py
```

## Build Windows App

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\build_windows.ps1
```

Build output:

- `dist\SnakeGame\SnakeGame.exe`
- `dist\SnakeGame\_internal\...`

Copy the whole `dist\SnakeGame` folder to another Windows PC and run `SnakeGame.exe`.

## Build Installer (Setup.exe)

1. Install Inno Setup and ensure `iscc` is available in PATH.
2. Run the same build script again.
3. Installer output: `installer\output\SnakeGameSetup.exe`

The installer supports install/uninstall and shortcuts.