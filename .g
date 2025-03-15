import os
import subprocess

# Konfigurasi
GITHUB_REPO = "https://github.com/johnhornjh/jhtools.git"  # Ganti dengan URL repo
BRANCH = "main"  # Ganti jika branch-nya berbeda

def run_command(command):
    """Jalankan perintah shell dan tampilkan outputnya."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("⚠️ Error:", result.stderr)

def git_init():
    """Inisialisasi Git jika belum ada."""
    if not os.path.exists(".git"):
        print("🔧 Inisialisasi Git...")
        run_command("git init")
        run_command(f"git remote add origin {GITHUB_REPO}")
        run_command(f"git checkout -b {BRANCH}")

def git_add_commit_push():
    """Menambahkan semua file, commit, dan push ke GitHub."""
    run_command("git add .")
    commit_message = input("📝 Masukkan pesan commit: ")
    run_command(f'git commit -m "{commit_message}"')
    run_command(f"git push origin {BRANCH}")

def git_remove_file():
    """Menghapus file dari repository GitHub."""
    file_name = input("🗑️ Masukkan nama file yang ingin dihapus: ")
    if os.path.exists(file_name):
        run_command(f"git rm {file_name}")
        commit_message = f"Remove {file_name}"
        run_command(f'git commit -m "{commit_message}"')
        run_command(f"git push origin {BRANCH}")
        print(f"✅ {file_name} berhasil dihapus dari repository!")
    else:
        print(f"⚠️ File {file_name} tidak ditemukan!")

if __name__ == "__main__":
    git_init()
    
    while True:
        print("\n📌 Pilihan:")
        print("1️⃣ Tambahkan file dan push ke GitHub")
        print("2️⃣ Hapus file dari repository")
        print("3️⃣ Keluar")
        pilihan = input("👉 Pilih menu (1/2/3): ")

        if pilihan == "1":
            git_add_commit_push()
        elif pilihan == "2":
            git_remove_file()
        elif pilihan == "3":
            print("👋 Keluar dari script...")
            break
        else:
            print("⚠️ Pilihan tidak valid, coba lagi!")