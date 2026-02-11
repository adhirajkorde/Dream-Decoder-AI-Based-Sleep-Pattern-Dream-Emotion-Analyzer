@echo off
setlocal enabledelayedexpansion
echo ========================================
echo   Dream Decoder - Setup (Python 3.10)
echo ========================================
echo.

cd /d %~dp0

:: Check for Existing Venv
if exist venv (
    set /p "REINSTALL=Virtual environment already exists. Delete and reinstall? (y/n): "
    if /i "!REINSTALL!"=="y" (
        echo Cleaning up old venv...
        rmdir /s /q venv
    ) else (
        echo Skipping venv creation.
        goto install_deps
    )
)

:create_venv
echo [1/4] Detecting Python 3.10...
:: Try py launcher first
py -3.10 --version >nul 2>&1
if %errorlevel% equ 0 (
    set "PYTHON_CMD=py -3.10"
) else (
    :: Fallback to standard python command
    python --version >version.txt 2>&1
    set /p PY_VER=<version.txt
    del version.txt
    echo !PY_VER! | findstr /c:"3.10." >nul
    if %errorlevel% equ 0 (
        set "PYTHON_CMD=python"
    ) else (
        echo.
        echo ERROR: Python 3.10 was not found.
        echo Found: !PY_VER!
        echo.
        echo Would you like to attempt to install Python 3.10 automatically?
        echo (Requires 'winget' and Administrator privileges may be requested)
        set /p "INSTALL_PY=Install Python 3.10 now? (y/n): "
        if /i "!INSTALL_PY!"=="y" (
            echo Attempting to install Python 3.10 via winget...
            winget install Python.Python.3.10 --silent --accept-package-agreements --accept-source-agreements
            if errorlevel 1 (
                echo.
                echo ERROR: Automatic installation failed. 
                echo Please install Python 3.10.x manually from python.org.
                pause
                exit /b 1
            )
            echo.
            echo Python 3.10 installed successfully! Please RESTART this script.
            pause
            exit /b 0
        )
        echo.
        echo Please install Python 3.10.x manually and try again.
        pause
        exit /b 1
    )
)

echo Using: !PYTHON_CMD!
echo Creating virtual environment...
!PYTHON_CMD! -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment. 
    pause
    exit /b 1
)

:install_deps
echo.
echo [2/4] Activating virtual environment...
if not exist venv\Scripts\activate.bat (
    echo ERROR: Virtual environment directory is missing Scripts\activate.bat.
    pause
    exit /b 1
)
call venv\Scripts\activate.bat

echo.
echo [3/4] Installing/Updating core tools...
python -m pip install --upgrade pip setuptools wheel

echo.
echo [4/4] Installing dependencies...
echo (Large packages like torch and transformers may take time...)
pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo ERROR: Failed to install dependencies.
    echo TIP: If you see "File name too long" errors:
    echo 1. Run PowerShell as Administrator
    echo 2. Execute: .\fix_long_paths.ps1
    echo 3. Restart this setup.
    pause
    exit /b 1
)

echo.
echo Downloading NLP models...
python -c "import spacy; try: spacy.load('en_core_web_sm'); print('Model already exists.'); except: spacy.cli.download('en_core_web_sm')"

echo.
echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo Run 'start.bat' to launch the application.
echo.
pause
