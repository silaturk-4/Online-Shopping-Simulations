#___orders.py___

#MÜŞTERİDEN BİLGİ ALIMI
name = input("Adınız: ")
email = input("E-posta adresiniz: ")
address = input("Adresiniz: ")

# SİPARİŞ ÖZETİ GÖSTERME
print("\n--- SİPARİŞ ÖZETİ ---")
print("Müşteri Bilgileri:")
print("Ad:", name)
print("E-posta:", email)
print("Adres:", address)

print("\nÜrünler:")
total = 0

for product, info in cart.items():
    subtotal = info["price"] * info["quantity"]
    total += subtotal
    print(f"- {product} x{info['quantity']} = {subtotal} TL")

print("\nToplam Tutar:", total, "TL")
print("---------------------")

#ÖDEME YÖNTEMİ SEÇİMİ
print("Ödeme Yöntemi Seçiniz:")
print("1 - Nakit")
print("2 - Kart")
print("3 - Dijital Cüzdan")

choice = input("Seçiminiz (1/2/3): ")

if choice == "1":
    payment_method = "Nakit"
elif choice == "2":
    payment_method = "Kart"
elif choice == "3":
    payment_method = "Dijital Cüzdan"
else:
    print("Geçersiz seçim! Ödeme iptal edildi.")
    exit()

print("\nÖdeme alınıyor...")
print("Ödeme yöntemi:", payment_method)
print("Ödeme başarıyla tamamlandı ")

import uuid
from datetime import datetime

payment_method = "Kart"  # Örnek ödeme yöntemi

# Sipariş oluşturma
order = {
    "order_id": str(uuid.uuid4()),          # Benzersiz ID
    "timestamp": datetime.now().isoformat(), # Tarih & saat
    "items": [],
    "total": 0,
    "payment_method": payment_method
}

# Ürünleri ve toplamı hesapla
for product, info in cart.items():
    subtotal = info["price"] * info["quantity"]
    order["items"].append({
        "name": product,
        "price": info["price"],
        "quantity": info["quantity"],
        "subtotal": subtotal
    })
    order["total"] += subtotal

# Sipariş özeti
print("\n--- SİPARİŞ KAYDI ---")
print("Sipariş ID:", order["order_id"])
print("Tarih:", order["timestamp"])
print("Ödeme Yöntemi:", order["payment_method"])

print("\nÜrünler:")
for item in order["items"]:
    print(f"- {item['name']} x{item['quantity']} = {item['subtotal']} TL")

print("\nToplam:", order["total"], "TL")


import json
from pathlib import Path

# Örnek sipariş (order record)
order = {
    "order_id": "12345",
    "timestamp": "2025-12-18T20:30:00",
    "items": [
        {"name": "Elma", "price": 10, "quantity": 2, "subtotal": 20},
        {"name": "Muz", "price": 7, "quantity": 3, "subtotal": 21}
    ],
    "total": 41,
    "payment_method": "Kart"
}

# Siparişi dosyaya kaydetme
def save_order_to_file(order, filename="orders.json"):
    orders = []

    file_path = Path(filename)
    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as f:
            orders = json.load(f)

    orders.append(order)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(orders, f, indent=2, ensure_ascii=False)


# Makbuz (fiş) oluşturma
def generate_receipt(order, folder="receipts"):
    Path(folder).mkdir(exist_ok=True)

    receipt_file = Path(folder) / f"{order['order_id']}.txt"

    with open(receipt_file, "w", encoding="utf-8") as f:
        f.write("===== SATIŞ FİŞİ =====\n")
        f.write(f"Sipariş ID: {order['order_id']}\n")
        f.write(f"Tarih: {order['timestamp']}\n\n")

        f.write("Ürünler:\n")
        for item in order["items"]:
            f.write(
                f"- {item['name']} x{item['quantity']} = {item['subtotal']} TL\n"
            )

        f.write("\n")
        f.write(f"Toplam: {order['total']} TL\n")
        f.write(f"Ödeme Yöntemi: {order['payment_method']}\n")
        f.write("=====================\n")


# Fonksiyonları çağırma
save_order_to_file(order)
generate_receipt(order)

print("Sipariş kaydedildi ve makbuz oluşturuldu ")
