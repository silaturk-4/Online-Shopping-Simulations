# Online-Shopping-Simulations
Project 2 online shopping
class Product:
    def __init__(self, sku, name, category, price, stock, description):
        self.sku = sku
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.description = description
        self.discontinued = False


class Catalog:
    def __init__(self):
        self.products = []

    # SKU benzersiz olsun
    def sku_exists(self, sku):
        return any(p.sku == sku for p in self.products)

    # Ürün ekleme
    def add_product(self, sku, name, category, price, stock, description):
        if self.sku_exists(sku):
            print("HATA: SKU zaten mevcut!")
            return
        
        if stock < 0:
            print("HATA: Stok negatif olamaz!")
            return
        
        product = Product(sku, name, category, price, stock, description)
        self.products.append(product)
        print("Ürün eklendi:", name)

    # Ürün güncelleme
    def update_product(self, sku, **kwargs):
        for p in self.products:
            if p.sku == sku:
                if "stock" in kwargs and kwargs["stock"] < 0:
                    print("HATA: Stok negatif olamaz!")
                    return
                
                for key, value in kwargs.items():
                    setattr(p, key, value)

                print("Ürün güncellendi:", sku)
                return
        
        print("HATA: Ürün bulunamadı")

    # Ürün satıştan kaldırma
    def discontinue_product(self, sku):
        for p in self.products:
            if p.sku == sku:
                p.discontinued = True
                print("Ürün satıştan kaldırıldı:", sku)
                return
        print("HATA: Ürün bulunamadı")

    # Kategoriye göre listeleme
    def list_by_category(self, category):
        return [p for p in self.products if p.category == category and not p.discontinued]

    # Anahtar kelime arama
    def search(self, keyword):
        return [
            p for p in self.products
            if keyword.lower() in p.name.lower() or keyword.lower() in p.description.lower()
        ]

    # Sıralama
    def sort_by(self, field):
        valid_fields = ["price", "stock"]
        if field not in valid_fields:
            print("Sıralama alanı geçersiz!")
            return []

        return sorted(self.products, key=lambda p: getattr(p, field))
