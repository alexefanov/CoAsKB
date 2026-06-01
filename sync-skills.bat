@echo off
echo ============================================
echo   OmegaWiki - Sync i18n/ru to .claude
echo ============================================
echo.
cd /d C:\CoAsKB
echo Copying skills...
xcopy /E /Y /Q "i18n\ru\skills\*" ".claude\skills\"
echo.
echo Copying AGENTS.md...
Copy-Item -Path "i18n\ru\AGENTS.md" -Destination "AGENTS.md" -Force
echo.
echo ============================================
echo   Done!
echo ============================================
pause
