# Gemini Cowork

**Gemini Cowork** 是一個基於 Python 的 GUI 應用程式，旨在作為您的 AI 結對程式設計夥伴 (AI Pair Programmer)。它封裝了強大的自主代理 (Autonomous Agent) 邏輯，讓您能夠透過簡單的圖形介面指派複雜的開發任務。

## 🚀 功能特點 (Features)

*   **直覺的圖形介面 (GUI)**:
    *   使用 Dark Mode 設計，長時間使用不刺眼。
    *   提供工作目錄 (Work Directory) 選擇器。
    *   支援多行任務描述輸入。
    *   即時顯示 Agent 執行日誌 (Real-time Logs)。
*   **自動化上下文注入 (Context Injection)**:
    *   自動掃描目標目錄結構，讓 Agent 理解專案現況。
    *   自動讀取全域 **Skills** (`Gemini-Skill.md`) 與 **MCP Tools** (`Gemini-MCP.md`) 說明，賦予 Agent 使用高階工具的能力。
*   **任務生成 (Prompt Generation)**:
    *   根據您的輸入自動生成 `PROMPT.md`，作為 Agent 的任務指導書。
    *   自動清理舊的狀態檔案 (`.circuit_breaker_state`, `.ralph_state.json`)，確保每次執行都是乾淨的開始 (Fresh Start)。
*   **自主執行 (Autonomous Execution)**:
    *   後端整合 `ralph_loop.py`，支援多迭代 (Multi-turn) 的自主開發循環。

## 📂 檔案結構 (File Structure)

本專案主要由一個啟動腳本與全域 Python Scripts 組成：

*   **`launch_cowork.bat`**: 
    *   本地啟動腳本。負責呼叫 Python 環境並啟動 GUI。
    *   執行指令: `.\launch_cowork.bat`
*   **核心邏輯 (Global Scripts)**:
    *   這些腳本位於您的全域 Skills 目錄中 (`.antigravity/skills/ralph_loop/scripts/`)，本專案直接引用之。
    *   `gemini_cowork_gui.py`: Tkinter GUI 介面程式碼。
    *   `gemini_cowork.py`: 負責環境掃描、Prompt 生成與 Process 管理的中介層。
    *   `ralph_loop.py`: 實際執行 AI 決策與工具呼叫的主迴圈。

## 🛠️ 使用指南 (Usage)

1.  **啟動程式**:
    在專案根目錄下的 PowerShell 執行：
    ```powershell
    .\launch_cowork.bat
    ```

2.  **設定工作環境**:
    *   **Work Directory**: 選擇您要讓 AI 進行開發的專案資料夾 (預設為當前目錄)。
    *   **Task Description**: 用自然語言詳細描述您的需求 (例如："建立一個 Python 貪食蛇遊戲，並使用 Pygame 函式庫")。

3.  **執行與監控**:
    *   點擊 **🚀 Start Cowork** 開始任務。
    *   透過下方黑色終端機視窗監控執行進度。
    *   完成後，Agent 會在目標目錄產生 `PROMPT.md` (任務檔) 與 `walkthrough.md` (執行報告，如果有的話)。

4.  **停止與複製**:
    *   **🛑 Stop**: 強制終止目前的 Agent 程序。
    *   **📋 Copy Logs**: 將目前的執行日誌複製到剪貼簿，方便除錯或分享。

## 🔧 技術細節 (Technical Details)

*   **Backend**: Python, `subprocess` module for process management.
*   **GUI Framework**: Tkinter.
*   **Encoding**: 強制使用 UTF-8 處理 I/O，並支援中文顯示 (Microsoft JhengHei UI / NSimSun 字型)。
*   **Architecture**: Local Launcher -> Global Logic Script -> Generic Agent Loop.

## 📝 注意事項 (Notes)

*   確保您的環境已安裝 Python 並配置好相關依賴。
*   Agent 的能力取決於 `Gemini-Skill.md` 中定義的 Skills 與模型本身的能力。
