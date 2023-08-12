@echo off
echo Starting BoxSys...
timeout 2 >nul
echo Loading App.py...
timeout 1 >nul
echo App.py Starting up...
timeout 0.2 >nul
echo Gathering data...
timeout 0.5 >nul
chdir DATA
cd
echo Data Gathered
chdir System
cd
timeout 0.1 >nul
App.py
echo App.py started

