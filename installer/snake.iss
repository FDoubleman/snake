[Setup]
AppId={{D7D8A327-7ECA-4B26-9CD0-7E9A4AA4A3F3}
AppName=SnakeGame
AppVersion=1.0.0
AppPublisher=FDoubleman
DefaultDirName={autopf}\SnakeGame
DefaultGroupName=SnakeGame
SetupIconFile=..\assets\icon.ico
UninstallDisplayIcon={app}\SnakeGame.exe
OutputDir=output
OutputBaseFilename=SnakeGameSetup
Compression=lzma
SolidCompression=yes
WizardStyle=modern
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create desktop shortcut"; GroupDescription: "Additional tasks:"; Flags: unchecked

[Files]
Source: "..\.packtmp\dist\SnakeGame\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\SnakeGame"; Filename: "{app}\SnakeGame.exe"
Name: "{autodesktop}\SnakeGame"; Filename: "{app}\SnakeGame.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\SnakeGame.exe"; Description: "Launch SnakeGame"; Flags: nowait postinstall skipifsilent
