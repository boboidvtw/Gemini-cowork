@echo off
echo Starting Gemini Cowork GUI...
python "C:\Users\boboi\.antigravity\skills\ralph_loop\scripts\gemini_cowork_gui.py"
if %errorlevel% neq 0 (
    echo Error occurred!
    pause
)
