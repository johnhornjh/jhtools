from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import os
import datetime,time
import psutil
import os
import subprocess
import requests

# KONFIGURASI BOT TELEGRAM
TOKEN = "7376792028:AAEMFJ0-3d2DvvPcZTX4VvXyXsnU0PZk0-A"  # Ganti dengan token bot kamu
CHAT_ID = "7233342888"  # Ganti dengan chat ID grup atau akun kamu
SEND_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# Variabel penyimpan jumlah pengguna
total_users = 0

def send_notification(data):
    global total_users

    if data == "jhdv=true":
        total_users += 1  # Tambah pengguna baru
        message = f"✅ Pengguna baru = +1\nTotal pengguna sekarang: {total_users}"
    elif data == "tes":
        message = "✅ Tes berhasil!"
    else:
        message = "⚠ Data tidak valid"

    data_send = {"chat_id": CHAT_ID, "text": message}
    requests.post(SEND_URL, json=data_send)

# --- Contoh Penggunaan ---
# Simulasi input dari user (bisa diubah sesuai kebutuhan)
data_input = "jhdv=true"  # Bisa diganti dengan "tes"
send_notification(data_input)

os.system("clear")
password = input("Enter Password : ")
if password != "JH-TOOLS123X0XAZGC7492HTNGRNFHJHTHDGBQTHTJRRYJEYJEGKTJRHYEJETJFGRGEHURK5YSGTJTKYK6GG362TBTJTHBEYN3YNTNHRH4KY3I63I4T1R3O7O6ILURKEGJAHFBXGFBY3KRHKQTUTQHQGJ2YJ3YJ63I3YP67ETQHRUKRHRHKRYKEGKYEKWTJSFJTEJTWJWTH52J25HEG9RW9H9WQR911TTQOHOROEGTWJRHRHRH3TJ14URHYK3TRGTN2YJRQHTHTRYKEYK2YJ2TJ2TJ1T1J25J26DIKAJOHNHORNIISOSIS9W92UWJWISKSHDHSISJIISISSISVJDKXJXIXXIDI8JGEJEGJTJTJRHTJJLONG":
    print("Wrong Password!")
    exit()

print("Login berhasil! Menjalankan tool...")
os.environ["AUTHORIZED"] = "TRUE"  # Set status login

def run_tool(tool_name):
    subprocess.run(["python", tool_name], env=os.environ)
    
console = Console()

tools = rf"""
    _____  ____  ____            _________               __          
   |_   _||_   ||   _|          |  _   _  |             [  |         
     | |    | |__| |    ______  |_/ | | \_|.--.    .--.  | |  .--.   
 _   | |    |  __  |   |______|     | |  / .'`\ \/ .'`\ \| | ( (`\]  
| |__' |   _| |  | |_              _| |_ | \__. || \__. || |  `'.'.  
`.____.'  |____||____|            |_____| '.__.'  '.__.'[___][\__)  
            {datetime.datetime.now()} | JOHNHORN | Tools                                                                    """

def show_menu():
    os.system("clear")  # Gunakan "cls" jika di Windows

    # Judul dengan border
    console.print(Panel.fit(f"[bold cyan]{tools}[/]\n", style="bold blue"))

    # Tabel menu
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Num", justify="center", style="cyan", no_wrap=True)
    table.add_column("Choice", style="yellow")

    menu_items = [
        ("1", "Update Tools"),
        ("2", "Check memory usage"),
        ("3", "View the list of tools in this folder"),
        ("4", "Admin Finder"),
        ("5", "Subdomain Finder"),
        ("6", "Nmap"),
        ("7", "Screenshot Website"),
        ("8", "G-Dork"),
        ("9", "YT-Mp3"),
        ("10", "YT-Mp4"),
        ("11", "NIK - GENERATOR"),
        ("12", "UA-Generator"),
        ("13", "Check version"),
        ("14", "Encrypt Python"),
        ("15", "Encrypt Bash"),
        ("16", "File Monitor"),
        ("0", "Exit")
    ]

    for item in menu_items:
        table.add_row(*item)

    console.print(table)

def main():
    while True:
        show_menu()
        
        pilihan = console.input("[bold yellow]Select options : [/]")
        
        if pilihan == "1":
            os.system("bash update.sh")
        elif pilihan == "2":
            mem = psutil.virtual_memory()
            console.print(f"\n[green]Total Memory:[/] {mem.total / 1e+9:.2f} GB")
            console.print(f"[green]Memory Used:[/] {mem.used / 1e+9:.2f} GB")
            console.print(f"[green]Memori Available:[/] {mem.available / 1e+9:.2f} GB\n")
        elif pilihan == "3":
            files = os.listdir(".")
            console.print(f"\n[green]List :[/]")
            for file in files:
                console.print(f"- {file}")
            console.print("")
        elif pilihan == "4":
            print("using admin finder...")
            time.sleep(2)
            run_tool("finder.py")
        elif pilihan == "5":
            print("using admin Subdomain Finder...")
            time.sleep(2)
            run_tool("subfinder.py")
        elif pilihan == "6":
            print("using Nmap...")
            time.sleep(2)
            run_tool("nmap.py")
        elif pilihan == "7":
            print("using Screenshot Website...")
            time.sleep(2)
            run_tool("ssweb.py")
        elif pilihan == "8":
            print("using G-Dork...")
            time.sleep(2)
            run_tool("dork.py")
        elif pilihan == "9":
            print("using YT-Mp3...")
            time.sleep(2)
            run_tool("mp3.py")
        elif pilihan == "10":
            print("using YT-Mp4...")
            time.sleep(2)
            run_tool("mp4.py")
        elif pilihan == "11":
            print("using NIK-GENERATOR...")
            time.sleep(2)
            run_tool("nikgen.py")
        elif pilihan == "12":
            print("using UA-Generator...")
            time.sleep(2)
            run_tool("uagen.py")
        elif pilihan == "13":
            print("Cheking...")
            time.sleep(2)
            os.system("cat versi")
        elif pilihan == "14":
            print("using Enc Python")
            time.sleep(2)
            run_tool("enc.py")
        elif pilihan == "15":
            print("using Enc Bash")
            time.sleep(2)
            run_tool("enc-sh.py")
        elif pilihan == "16":
            print("using FMonitor")
            time.sleep(2)
            run_tool("Fmonitor.py")
        elif pilihan == "0":
            console.print("\n[bold red]Goodbye.[/]")
            break
        else:
            console.print("\n[bold red]Invalid selection![/]\n")

        console.input("[bold yellow]Press Enter to return to the menu...[/]")

if __name__ == "__main__":
    main()