# 🖥️ Proc Monitor

### *Real-time CLI system monitor for Windows — because `Ctrl+Alt+Del` is so last century.*

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-blue)](https://microsoft.com/windows)
[![Made with](https://img.shields.io/badge/Made%20with-psutil-orange)](https://github.com/giampaolo/psutil)

---

## 🎯 What it does

**Proc Monitor** turns your terminal into a live dashboard that shows:

- 📊 **CPU usage** – percentage + live graph bar  
- 💾 **RAM usage** – total memory consumption  
- 🔥 **Top processes** – who's eating your CPU right now  

No GUI. No bloat. Just a lightweight, real‑time process watcher built with **Python** and **psutil**.

---

## ✨ Features

- ⚡ **Live updates** every 2 seconds  
- 🧠 **Minimal CPU footprint** – uses only `psutil`  
- 🎮 **Instant stop** – press `q` to quit (no `Ctrl+C` dancing)  
- 🖥️ **Windows native** – works in CMD, PowerShell, Windows Terminal  
- 🎨 **Clean ASCII output** – easy to read, easy to log  

---
##  📸 Demo
-- -- -- -- -- -- -- -- -- -- -- -- -- -- --

--- Proc Monitor - Press 'q' to stop ---
-- -- -- -- -- -- -- -- -- -- -- -- -- -- --

CPU: 23.4%   RAM: 54.2%
-- -- -- -- -- -- -- -- -- -- -- -- 
--- Top Processes ---

  Code.exe: 12.1%
  chrome.exe: 8.5%
  python.exe: 4.2%
  explorer.exe: 0.8%
  dwm.exe: 0.5%

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
Press 'q' to stop...

## 🛠️ Built with
 - Python 3 – the language

 - psutil – cross‑platform system library

 - msvcrt – Windows key press detection

## 🤔 Why I built this
 - I wanted a lightweight alternative to Task Manager – something I could run directly in the terminal without opening a new window. No Electron, no web UI. Just Python and a few lines of code. It’s also a great example of using psutil for real‑time system monitoring.


## 📌 Future ideas
 - Color‑coded bars (green/orange/red)

 - Save snapshot to CSV (--save)

 - Monitor a specific process by PID (--pid 1234)

 - Linux / macOS support

## ⭐ Show your support

 - If this repository helped you or you just think it's neat, give it a star ⭐ – it means a lot!

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Vansh140507/proc-monitor.git
cd proc-monitor


