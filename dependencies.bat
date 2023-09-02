@echo off

REM Install required dependencies for Speedtest script

REM Upgrade pip
python -m pip install --upgrade pip

REM Install colorama
pip install colorama

REM Install requests
pip install requests

REM Install speedtest-cli
pip install speedtest-cli
