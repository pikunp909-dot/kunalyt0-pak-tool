#!/data/data/com.termux/files/usr/bin/bash
set -e

GH_USER="pikunp909-dot"
REPO="kunalyt0-pak-tool"
BIN_URL="https://github.com/$GH_USER/$REPO/releases/latest/download/kunal_enc"
SRC_URL="https://raw.githubusercontent.com/$GH_USER/$REPO/main/kunal.py"
INSTALL_DIR="$HOME/.kunalyt0"

echo "╔══════════════════════════════════════════╗"
echo "║   KUNALYT0 PAK TOOL - Installer          ║"
echo "╚══════════════════════════════════════════╝"

if [ ! -d "$PREFIX" ]; then echo "❌ Termux required"; exit 1; fi
[ ! -d "$HOME/storage" ] && (termux-setup-storage; sleep 2)
command -v python3 >/dev/null || pkg install python -y

echo "📦 Installing dependencies (2-3 min)..."
pip install --quiet --upgrade pip
for pkg in rich requests pycryptodome zstandard gmalg colorama termcolor pytz; do
    pip install --quiet "$pkg" 2>/dev/null || echo "  ⚠️ $pkg retry needed"
done

mkdir -p "$INSTALL_DIR"
BINARY_OK=0

if [ "$(uname -m)" = "aarch64" ]; then
    echo "⬇️  Trying pre-built binary..."
    if curl -fsSL "$BIN_URL" -o "$INSTALL_DIR/kunal_enc" 2>/dev/null; then
        chmod +x "$INSTALL_DIR/kunal_enc"
        if ! ldd "$INSTALL_DIR/kunal_enc" 2>&1 | grep -q "not found"; then
            BINARY_OK=1
            echo "✅ Binary installed"
        else
            rm -f "$INSTALL_DIR/kunal_enc"
            echo "⚠️  Binary incompatible, using source"
        fi
    fi
fi

if [ "$BINARY_OK" -eq "0" ]; then
    echo "⬇️  Downloading source (portable)..."
    curl -fsSL "$SRC_URL" -o "$INSTALL_DIR/kunal.py"
fi

cat > "$PREFIX/bin/kunalyt0" << 'WRAP'
#!/data/data/com.termux/files/usr/bin/bash
cd "$HOME" || exit 1
if [ -x "$HOME/.kunalyt0/kunal_enc" ]; then
    exec "$HOME/.kunalyt0/kunal_enc" "$@"
elif [ -f "$HOME/.kunalyt0/kunal.py" ]; then
    exec python3 "$HOME/.kunalyt0/kunal.py" "$@"
else
    echo "❌ Install corrupted"; exit 1
fi
WRAP
chmod +x "$PREFIX/bin/kunalyt0"

mkdir -p "/storage/emulated/0/Documents/KUNALYT0"/{PAK,UNPACK,REPACK,RESULT}

echo ""
echo "✅ Installed!"
echo "   Run: kunalyt0"
echo "   Mode: $([ "$BINARY_OK" -eq "1" ] && echo 'Binary' || echo 'Source')"
