#!/usr/bin/env bash

echo "🚀 Instalando The Maran..."

INSTALL_DIR="$HOME/the_maran"

mkdir -p "$INSTALL_DIR"

cp "$(dirname "$0")/the_maran/api_manager.py" "$INSTALL_DIR/"

chmod +x "$INSTALL_DIR/api_manager.py"

echo ""
echo "✅ Instalado correctamente"
echo "👉 Ejecutar:"
echo "python3 ~/the_maran/api_manager.py"
