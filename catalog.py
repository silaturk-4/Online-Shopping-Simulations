    # catalog.py

def load_products():
    """Example initial catalog"""
    return [
        {"id": "SKU1", "name": "Laptop", "category": "Electronics", "price": 12000, "stock": 5, "description": "Gaming laptop"},
        {"id": "SKU2", "name": "Mouse", "category": "Electronics", "price": 150, "stock": 30, "description": "Wireless mouse"},
        {"id": "SKU3", "name": "T-shirt", "category": "Clothes", "price": 200, "stock": 20, "description": "Cotton shirt"},
    ]


def search_products(products, keyword):                        #anahtar kelime ile ürün arama
    keyword = keyword.lower()
    return [
        p for p in products
        if keyword in p["name"].lower() or keyword in p["description"].lower()
    ]


def filter_by_category(products, category):                  #ürünü kategoriye göre filtreleme
    return [p for p in products if p["category"].lower() == category.lower()]


def sort_products(products, by="price"):                     # fiyat veya stok'a göre ürünleri sırala
    if by not in ("price", "stock"):
        raise ValueError("Sort key must be 'price' or 'stock'")
    return sorted(products, key=lambda p: p[by])


def add_product(products, product): #ürün ekleme 
    if any(p["id"] == product["id"] for p in products):
        raise ValueError("SKU must be unique.")
    if product["stock"] < 0:
        raise ValueError("Stock cannot be negative.")
    
    products.append(product)
    return product


def update_product(products, product_id, updates):               #ürün güncelleme
    for p in products:
        if p["id"] == product_id:
            if "stock" in updates and updates["stock"] < 0:
                raise ValueError("Stock cannot be negative.")
            p.update(updates)
            return p
    return None


def discontinue_product(products, product_id):
    """Remove a product from catalog."""
    for p in products:
        if p["id"] == product_id:
            products.remove(p)
            return True
    return False

if __name__ == "__main__":
    products = load_products()

    print("Search 'mouse':", search_products(products, "mouse"))
    print("Electronics:", filter_by_category(products, "Electronics"))
    print("Sorted by price:", sort_products(products, by="price"))

    add_product(products, {
        "id": "SKU4",
        "name": "Keyboard",
        "category": "Electronics",
        "price": 300,
        "stock": 15,
        "description": "Mechanical keyboard"
    })

    update_product(products, "SKU1", {"price": 11000})
    discontinue_product(products, "SKU3")

    print("Final catalog:", products)
