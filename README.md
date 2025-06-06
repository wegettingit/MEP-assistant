# MEP — Mise en Place (AI Kitchen Brain)

**MEP** is a prep-centered AI assistant that remembers what humans forget.  
It helps cooks move smoother, stay ahead, and protect their mental energy.

- 🧠 GPT-powered kitchen assistant (runs local on your computer)
- 🧾 Tracks prep lists, 86s, family meals, and more
- ⚖️ Real ethics, not just code — worker-first logic

---

## 🚦 Status
> 🟢 **Beta:** Local version now live for real chefs  
> 🔗 [Try MEP in GPT (cloud)](https://chatgpt.com/g/g-683117aaa21c81919718d7ccf3802b96-mep)  
> 🧪 Testing in progress (Ollama + Electron desktop app)

---

## 🛠️ Install & Quick Start

**No Java needed! Just Python, Node.js, and Ollama.**

### 1. Prerequisites
- **Python 3.10+**
- **Node.js + npm**
- **Ollama** ([Download here](https://ollama.com/))
- **Electron Forge** (auto-installed via `npm install`)

### 2. Download & Setup

**Clone or unzip this repo, then:**

```bash
# (Once, to get dependencies)
npm install

# (Once, to get the AI model)
ollama pull llama3:8b
