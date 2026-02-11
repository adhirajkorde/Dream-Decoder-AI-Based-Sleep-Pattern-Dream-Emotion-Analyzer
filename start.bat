@echo off
echo ========================================
echo   Dream Decoder - Starting Server
echo ========================================
echo.

cd /d %~dp0

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Starting Dream Decoder server...
echo.
echo Open your browser to: http://localhost:5000
echo Press Ctrl+C to stop the server.
echo.

python backend\app.py
