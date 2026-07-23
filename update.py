#!/usr/bin/env python3
import os

def create_test_folder():
    # Kullanıcının masaüstü yolunu sistemden dinamik olarak çeker
    desktop_path = os.path.expanduser("~/Desktop")
    
    # Masaüstü Türkçe sistemlerde "Masaüstü" olabileceği için kontrol
    if not os.path.exists(desktop_path):
        tr_desktop = os.path.expanduser("~/Masaüstü")
        if os.path.exists(tr_desktop):
            desktop_path = tr_desktop

    test_folder = os.path.join(desktop_path, "test")

    try:
        os.makedirs(test_folder, exist_ok=True)
        print(f"[WindexOS] Test klasörü başarıyla oluşturuldu: {test_folder}")
    except Exception as e:
        print(f"[WindexOS] Klasör oluşturulurken hata: {e}")

if __name__ == "__main__":
    create_test_folder()
