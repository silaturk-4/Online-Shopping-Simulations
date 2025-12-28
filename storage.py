#storage.py
import os
import json
from datetime import datetime


def ensure_storage_structure(base_dir: str) -> None:  #storage yapısını oluştur
    """
    Gerekli klasörleri oluşturur.
    Yoksa data/ ve backups/ klasörlerini yaratır.
    """
    data_dir = os.path.join(base_dir, "data")
    backup_dir = os.path.join(base_dir, "backups")

    if not os.path.exists(data_dir):
        os.mkdir(data_dir)

    if not os.path.exists(backup_dir):
        os.mkdir(backup_dir)


def backup_file(source_path: str, backup_dir: str) -> str:   #yedek dosya oluştur
    """
    Dosyanın tarihli yedeğini alır.
    Örnek: products_20250128.json
    """
    if not os.path.exists(source_path):
        return ""

    date_str = datetime.now().strftime("")
    file_name = os.path.basename(source_path)
    backup_name = file_name.replace(".json", f"_{date_str}.json")
    backup_path = os.path.join(backup_dir, backup_name)

    try:        # Dosyayı kopyala
        with open(source_path, "r", encoding="utf-8") as src:
            data = src.read()

        with open(backup_path, "w", encoding="utf-8") as bck:
            bck.write(data)

        return backup_path
    except:
        return ""


def load_json(path: str):   #json dosyasını yükle
    """
    JSON dosyasını okur.
    Hata olursa boş liste döndürür.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        print("JSON read error. Returning empty data.")
        return []


def write_json(path: str, data):  # json dosyasına yaz
    """
    JSON dosyasına güvenli şekilde yazar.
    Önce backup alır.
    """
    base_dir = os.path.dirname(os.path.dirname(path))
    backup_dir = os.path.join(base_dir, "backups")

    # Backup al
    backup_file(path, backup_dir)

    try:
        with open(path, "w", encoding="utf-8") as f:   # json dosyasına yaz
            json.dump(data, f, indent=2, ensure_ascii=False)
    except:
        print("❌ JSON write error. Data not saved.")