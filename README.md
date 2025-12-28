#  Basit E-Ticaret Uygulaması

Bu proje, **Python başlangıç seviyesi** için geliştirilmiş bir **basit e-ticaret uygulamasıdır**.
Kullanıcı ürünleri görüntüleyebilir, sipariş oluşturabilir; yönetici (admin) ise satışları analiz edebilir ve rapor alabilir.

---

##  Projenin Amacı

Bu proje aşağıdaki konuları uygulamalı olarak göstermek için hazırlanmıştır:

* Temel alışveriş akışları
* Sepet ve fiyat hesaplamaları
* Dosyaya veri kaydetme
* Admin dashboard (analiz & raporlama)
* Modüler Python kod yapısı

---

##  Özellikler

* Ürün ve sipariş yönetimi
* Toplam gelir ve sipariş özeti
* En çok satan ürünler
* Stok azaldığında uyarı 
* Raporları TXT dosyası olarak dışa aktarma
* Başlangıç seviyesine uygun sade kod

---

## Proje Dosya Yapısı

```
project/
│
├─ main.py           # Programın çalıştırıldığı ana dosya
├─ reporting.py     # Analiz ve raporlama fonksiyonları
├─ reports/          # Oluşturulan raporların kaydedildiği klasör
└─ README.md         # Proje açıklama dosyası
```

---

## Programı Çalıştırma

### Gereksinimler

* Python 3.x

### Çalıştırma Adımları

1. Projeyi bilgisayarına indir veya klonla
2. Terminal / Komut İstemi aç
3. Proje klasörüne gir

```bash
python main.py
```

---

##  Admin Dashboard

Program çalıştığında admin için aşağıdaki bilgiler ekrana yazdırılır:

* Toplam sipariş sayısı
* Toplam gelir
* Ortalama sipariş tutarı
* En çok satan ürünler
* Stok uyarıları

---

##  Raporlama

Satış özeti otomatik olarak **reports/** klasörüne kaydedilir.

Örnek çıktı dosyası:

```
total_orders: 2
total_revenue: 16300
average_order: 8150.0
```

---

## Test & Güvenilirlik

* Kod hata vermeden çalışmaktadır
* Boş sipariş durumları kontrol edilmiştir
* Başlangıç seviyesine uygun şekilde test edilmiştir

---

##  Geliştirici

**Sıla Türk**
Python Öğrencisi

---


