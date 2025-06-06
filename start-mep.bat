@echo off
REM Starts Ollama, backend, and Electron app – all at once!

REM Start Ollama in the background
start "" /min cmd /k ollama run llama3:8b

REM Wait a few seconds for Ollama to load
timeout /t 5

REM Start backend
start "" cmd /k python mep_api.py

REM Wait for backend to start
timeout /t 3

REM Start Electron app (or .exe if built)
IF EXIST "out\MEP Assistant.exe" (
    start "" "out\MEP Assistant.exe"
) ELSE (
    npm start
)
