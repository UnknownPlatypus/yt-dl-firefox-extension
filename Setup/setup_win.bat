@echo off
set mypath=%~dp0
set script=%mypath%\setup.py 

call python %script%
pause