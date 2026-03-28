#!/usr/bin/env python3

import json
import requests
import time
from pathlib import Path

CONFIG_FILE = Path.home() / ".the_maran/config.json"

# ───────── CONFIG ─────────

def save_config(cfg):
    CONFIG_FILE.parent.mkdir(exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(cfg, f, indent=4)

def load_config():
    if not CONFIG_FILE.exists():
        return None
    with open(CONFIG_FILE) as f:
        return json.load(f)

# ───────── TEST API ─────────

def test_api(base_url, api_key, model):
    try:
        url = base_url.rstrip("/") + "/chat/completions"

        r = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": model,
                "messages": [{"role": "user", "content": "ping"}],
                "max_tokens": 5
            },
            timeout=10
        )

        if r.status_code == 200:
            return "ok"
        elif r.status_code == 401:
            return "bad_key"
        elif r.status_code == 400:
            return "bad_model"
        elif r.status_code == 429:
            return "rate"
        else:
            return f"error_{r.status_code}"

    except requests.exceptions.RequestException:
        return "connection_error"

# ───────── FALLBACK ─────────

def local_fallback():
    print("\n🧠 MODO LOCAL ACTIVADO (sin APIs)\n")
    while True:
        try:
            user = input("🧑 > ")
            if user.lower() in ["exit", "salir"]:
                print("👋 Saliendo")
                break
            print("🤖 (offline):", user)
        except KeyboardInterrupt:
            print("\n👋 Saliendo modo offline")
            break

# ───────── WIZARD ROBUSTO ─────────

def wizard():
    print("\n🚀 THE MARAN — CONFIGURACIÓN GUIADA\n")

    # BASE URL
    while True:
        base = input("Base URL (ej: https://openrouter.ai/api/v1): ").strip()

        if not base.startswith("http"):
            print("❌ URL inválida (debe comenzar con http)")
            continue

        if " " in base:
            print("❌ URL contiene espacios")
            continue

        break

    # MODELO
    while True:
        model = input("Modelo (ej: mistralai/mistral-7b-instruct:free): ").strip()

        if "/" not in model:
            print("❌ Modelo inválido")
            continue

        break

    # API KEYS
    keys = []

    while True:
        key = input("API KEY (enter para terminar): ").strip()

        if not key:
            break

        if len(key) < 20:
            print("❌ API KEY demasiado corta")
            continue

        print("🔍 Probando...")

        result = test_api(base, key, model)

        if result in ["ok", "rate"]:
            print(f"✅ Guardada ({result})")
            keys.append({"key": key})
        else:
            print(f"❌ inválida ({result})")

    if not keys:
        print("\n🚨 No se guardó ninguna API válida\n")
        return wizard()

    cfg = {
        "providers": [{
            "base_url": base,
            "models": [model],
            "api_keys": keys
        }]
    }

    save_config(cfg)
    print("\n✅ Configuración guardada correctamente\n")

# ───────── CORE ─────────

class Maran:

    def __init__(self):
        cfg = load_config()

        if not cfg:
            wizard()
            cfg = load_config()

        self.providers = cfg.get("providers", [])

    def run(self):
        if not self.providers:
            print("🚨 Sin APIs configuradas → fallback")
            local_fallback()
            return

        provider = self.providers[0]

        if not provider.get("api_keys"):
            print("🚨 Sin API keys → fallback")
            local_fallback()
            return

        base = provider["base_url"]
        model = provider["models"][0]

        # Probar todas las keys hasta que una funcione
        for key_obj in provider["api_keys"]:
            key = key_obj["key"]

            print(f"\n🔍 Probando modelo: {model}")

            result = test_api(base, key, model)

            if result == "ok":
                print("✅ API funcionando correctamente")
                return

            elif result == "rate":
                print("⚠️ Rate limit — intentando siguiente key")
                continue

            else:
                print(f"❌ Error ({result}) — probando siguiente")

        print("\n🚨 Todas las APIs fallaron")
        local_fallback()

# ───────── MAIN ─────────

if __name__ == "__main__":
    m = Maran()
    m.run()
