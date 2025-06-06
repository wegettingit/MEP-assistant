# MEP Assistant – Setup Guide

## Prerequisites
- [x] Python 3.10+ installed
- [x] Node.js + npm installed
- [x] Ollama installed (`https://ollama.com/`)
- [x] Ollama model pulled: `ollama run llama3:8b`

## Quick Start
1. Run Ollama (`ollama run llama3:8b`).
2. Run the Flask backend:

python mep_api.py

3. Double-click `MEP Assistant.exe` (in /out folder after install).

---

## 6. **BONUS: Automate All of This**
- Write a `.bat` file or use [electron-builder](https://www.electron.build/) or [pkg](https://github.com/vercel/pkg) to make a single .exe that runs all the parts in one go.
- Or reach out for help and I’ll give you the code for a “double-click-to-launch-everything” experience!

---

**Summary:**
- **For hackers:** Zip your folder, add a README, and share.
- **For normal users:** Use `npm run make` to generate an installer, zip the output, and provide instructions for Python/Ollama.

If you want a step-by-step to make a “one-click-for-everything” experience, just ask!  
Let me know if you want a **clean zip/installer script template** for your exact setup!
