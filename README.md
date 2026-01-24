# Gemini Cowork

**Gemini Cowork** is a Python-based GUI application designed to be your **AI Pair Programmer**. It encapsulates powerful Autonomous Agent logic, allowing you to assign complex development tasks through a simple graphical interface.

[中文說明 (Chinese Version)](README-ZH.md)

## 🚀 Features

*   **Intuitive GUI**:
    *   Dark Mode design for eye comfort during long coding sessions.
    *   Work Directory selector.
    *   Multi-line task description input.
    *   Real-time Agent logs display.
*   **Automated Context Injection**:
    *   Automatically scans the target directory structure to let the Agent understand the project context.
    *   Automatically reads global **Skills** (`Gemini-Skill.md`) and **MCP Tools** (`Gemini-MCP.md`) documentation, empowering the Agent with advanced capabilities.
*   **Prompt Generation**:
    *   Automatically generates `PROMPT.md` based on your input as the Agent's instruction manual.
    *   Auto-cleans old state files (`.circuit_breaker_state`, `.ralph_state.json`) to ensure a Fresh Start for every run.
*   **Autonomous Execution**:
    *   Integrated with `ralph_loop.py` backend to support multi-turn autonomous development loops.
*   **Multi-Backend Support**:
    *   **Gemini**: Supports official models like `gemini-2.0-flash-exp` (includes retry mechanisms).
    *   **Ollama (Local)**: Supports local models (e.g., `qwen2.5-coder`) with automatic Port correction, Context Persistence, and No-Rate-Limit mode for high-speed development.

## 📂 File Structure

This project consists of a launcher script and global Python Scripts:

*   **`launch_cowork.bat`**: 
    *   Local launch script. Responsible for calling the Python environment and starting the GUI.
    *   Command: `.\launch_cowork.bat`
*   **Core Logic (Global Scripts)**:
    *   These scripts reside in your global Skills directory (`.antigravity/skills/ralph_loop/scripts/`) and are referenced directly.
    *   `gemini_cowork_gui.py`: Tkinter GUI interface code.
    *   `gemini_cowork.py`: Middleware for environment scanning, Prompt generation, and Process management.
    *   `ralph_loop.py`: The main loop executing AI decisions and tool calls.

## 🛠️ Usage

1.  **Launch Application**:
    Run in PowerShell from the project root:
    ```powershell
    .\launch_cowork.bat
    ```

2.  **Configure Environment**:
    *   **Work Directory**: Select the project folder you want the AI to develop in (defaults to current directory).
    *   **Task Description**: Describe your requirements in natural language (e.g., "Create a Python Snake game using Pygame library").

3.  **Execute & Monitor**:
    *   Click **🚀 Start Cowork** to begin the task.
    *   Monitor progress via the black terminal window at the bottom.
    *   Upon completion, the Agent will generate `PROMPT.md` (Task File) and `walkthrough.md` (Report) in the target directory.

4.  **Control & Logs**:
    *   **🛑 Stop**: Forcefully terminate the current Agent process.
    *   **📋 Copy Logs**: Copy current logs to clipboard for debugging or sharing.
    *   **🗑️ Clear Logs**: Clear the current log window.

## 🔧 Technical Details

*   **Backend**: Python, `subprocess` module for process management.
*   **GUI Framework**: Tkinter.
*   **Encoding**: Enforced UTF-8 for I/O, supporting Chinese display (Microsoft JhengHei UI / NSimSun fonts).
*   **Architecture**: Local Launcher -> Global Logic Script -> Generic Agent Loop.

## 📝 Notes

*   Ensure Python is installed and dependencies are configured in your environment.

## ❤️ Support

If you find this project helpful, consider buying me a coffee!

[![Donate with PayPal](https://img.shields.io/badge/Donate-PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/boboidvtw168)
