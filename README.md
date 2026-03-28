# 🧠 The Maran
### Never let your AI die.

AI agents often stop working when APIs fail.

The Maran prevents that.

It keeps your system running by:
- rotating API keys
- handling rate limits
- switching providers
- falling back to offline mode

---

## ⚡ Quick Start (1 minute)

Clone and run:

```bash
git clone https://github.com/christianarg7-sys/The-Maran
cd The-Maran
bash install.sh
python3 ~/the_maran/api_manager.py

❓ Why this exists

Most AI systems fail when:

API tokens run out
Providers return errors (429, 401)
Free models become unavailable

When that happens, the system stops.

👉 The Maran solves this by making systems resilient instead of fragile.

🚀 Features
🔁 API key rotation
🔑 API validation before use
⚠️ Rate limit handling
🌐 Multi-provider ready (OpenRouter, DeepSeek)
🧠 Offline fallback mode
⚡ Interactive CLI setup

🧪 Use Cases
AI agents (AutoGPT, custom agents)
Trading bots
Research assistants
Low-cost AI systems
Offline-first environments

🧠 How it works
Asks for API configuration
Tests API keys
Saves only valid keys
Uses API when available
If API fails → tries next key
If all fail → activates offline mode

🧯 Fallback Mode

If no APIs are available:

🧠 LOCAL MODE ACTIVATED

The system continues working without crashing.

⚠️ Notes
Free APIs may fail frequently
It is recommended to use multiple providers
This tool prioritizes stability over performance

📦 Project Structure
The-Maran/
├── README.md
├── LICENSE
├── install.sh
├── the_maran/
│   └── api_manager.py
└── examples/
    └── config.example.json

📜 License

MIT License

⭐ Philosophy

A real AI system is not the smartest one —
it's the one that never stops.


---

## 4️⃣ GUARDAR

👉 Abajo:

```text
Commit changes

Mensaje:

Update README (final version)

👉 Click: Commit changes

