#!/bin/bash

# Direktori tempat script disimpan
SCRIPT_DIR="$HOME/jhtools"

# URL repo GitHub
REPO_URL="https://github.com/johnhornjh/jhtools.git"

# Cek apakah direktori sudah ada
if [ -d "$SCRIPT_DIR" ]; then
    echo "📢 Keluar dari direktori jika sedang di dalamnya..."
    cd ~  # Pindah ke home sebelum update

    echo "📢 Update script dari GitHub..."
    cd "$SCRIPT_DIR"
    git pull
else
    echo "📢 Script belum ada, meng-clone dari GitHub..."
    git clone "$REPO_URL" "$SCRIPT_DIR"
fi

echo "✅ Update selesai!"