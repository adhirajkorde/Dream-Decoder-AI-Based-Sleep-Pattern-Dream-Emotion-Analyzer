@echo off
echo ========================================
echo   Dream Decoder - Reset Database
echo ========================================
echo.
echo WARNING: This will delete all dreams and sleep records!
echo.

set /p confirm="Are you sure? (y/n): "
if /i not "%confirm%"=="y" (
    echo Cancelled.
    pause
    exit /b 0
)

cd /d %~dp0

echo.
echo Deleting database...
if exist "data\dream_decoder.db" (
    del "data\dream_decoder.db"
    echo Database deleted.
) else (
    echo No database found.
)

echo.
echo Database will be recreated when you start the app.
echo.
pause
