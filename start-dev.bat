@echo off
cd /d D:\temp\pet-five

echo Installing dependencies...
call npm install

echo.
echo Starting development server...
call npm run dev
pause
