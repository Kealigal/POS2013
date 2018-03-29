@echo off
title Pirates Client

cd ../

set /P PYTHON_PATH=<PYTHON_PATH

:main
%PYTHON_PATH% -m pirates.piratesbase.PiratesStart
pause
goto :main