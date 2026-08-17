#!/usr/bin/env python3
import os
import sys

print("[+] update.py çalıştırılıyor...")

# Hedef dizin ve dosya yolları
target_dir = "/Windex/Test/sys"
target_file = os.path.join(target_dir, "test.txt")

try:
    # Dizini oluştur (yoksa)
    print(f"[+] Dizin kontrol ediliyor/oluşturuluyor: {target_dir}")
    os.makedirs(target_dir, exist_ok=True)

    # Dosyayı oluştur ve içeriği yaz
    print(f"[+] Dosya yazılıyor: {target_file}")
    with open(target_file, "w", encoding="utf-8") as f:
        f.write("testt\n")

    print("[+] Dosya başarıyla oluşturuldu!")
    print("Tmm!")
    sys.exit(0)

except Exception as e:
    print(f"[-] Güncelleme sırasında hata oluştu: {e}")
    sys.exit(1)
