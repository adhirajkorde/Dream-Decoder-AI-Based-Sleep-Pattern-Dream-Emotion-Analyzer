@echo off
echo ========================================
echo   Dream Decoder - Starting Server
echo ========================================
echo.

cd /d %~dp0

if not exist venv\Scripts\activate.bat (
    echo ========================================
    echo   ERROR: Virtual Environment Not Found
    echo ========================================
    echo It looks like you haven't installed the prerequisites yet.
    echo Please run 'setup.bat' first to install everything.
    echo.
    pause
    exit /b 1
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Starting Dream Decoder server...
echo.
echo Open your browser to: http://localhost:5000
echo Press Ctrl+C to stop the server.
echo.

python backend\app.py

echo.
echo Server stopped or crashed.
pause
