@echo off
setlocal

set /p choice="Did you install the requirements? (y/n): "

if /i "%choice%"=="n" (
    echo Installing requirements...
    pip install pyinstaller
    pip install browser-cookie3
    echo Requirements installed, open this again.
) else if /i "%choice%"=="y" (
    echo Creating .exe with PyInstaller...
    pyinstaller --noconsole --icon="icon.ico" SillyCookies.py
    made by s-illy
    echo .exe created successfully.
) else (
    echo Invalid choice. Please enter 'y' or 'n'.
)

endlocal
pause
