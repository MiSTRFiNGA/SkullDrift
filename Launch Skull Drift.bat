@echo off
title SKULL DRIFT
cd /d "%~dp0"
echo.
echo   ============================
echo     SKULL DRIFT  -  launching
echo   ============================
echo.
start "" /min cmd /c "python cors_server.py"
timeout /t 2 /nobreak >nul
start "" "http://127.0.0.1:8378/index.html"
echo   Game opened in your browser at http://127.0.0.1:8378/index.html
echo   (Keep this window open while playing; close it to stop the server.)
echo.
pause >nul
