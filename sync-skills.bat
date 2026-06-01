@echo off
echo ============================================
echo   OmegaWiki - Sync i18n/ru to .claude
echo ============================================
echo.
cd /d C:\CoAsKB
powershell -ExecutionPolicy Bypass -File "setup.ps1" -Lang ru
echo.
echo ============================================
echo   Done!
echo ============================================
pause
