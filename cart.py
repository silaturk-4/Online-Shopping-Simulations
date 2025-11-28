def add_to_cart(pid, qty):
    if pid not in products:
        return "Ürün bulunamadı."

    if qty > products[pid]["stock"]:
        return "Yeterli stok yok."

    cart[pid] = cart.get(pid, 0) + qty
    return "Eklendi."


def remove_from_cart(pid):
    cart.pop(pid, None)


def update_quantity(pid, qty):
    if qty == 0:
        remove_from_cart(pid)
        return

    if qty > products[pid]["stock"]:
        return "Stok yetersiz."

    cart[pid] = qty


def clear_cart():
    cart.clear()


# ---------- PROMOSYON KODLARI ----------

promo_codes = {
    "SAVE10": {"type": "percent", "value": 10},
    "DISCOUNT50": {"type": "fixed", "value": 50},
    "FREESHIP": {"type": "free_shipping", "value": 0},
}

def apply_promo(code):
    global promo
    if code not in promo_codes:
        return "Kod geçersiz."
    promo = promo_codes[code]
    return "Kod uygulandı."


# ---------- HESAPLAMA ----------

def cart_summary():
    subtotal = sum(products[pid]["price"] * qty for pid, qty in cart.items())
    tax = subtotal * 0.18
    discount = 0
    shipping = 50

    if promo:
        if promo["type"] == "percent":
            discount = subtotal * (promo["value"] / 100)
        elif promo["type"] == "fixed":
            discount = min(subtotal, promo["value"])
        elif promo["type"] == "free_shipping":
            shipping = 0

    total = subtotal - discount + tax + shipping

    return {
        "subtotal": subtotal,
        "tax": tax,
        "discount": discount,
        "shipping": shipping,
        "total": total
    }
# ---------- CHECKOUT ----------

def checkout():
    for pid, qty in cart.items():
        if qty > products[pid]["stock"]:
            return "Stok yetersiz! Satın alma engellendi."

    # stok düşme
    for pid, qty in cart.items():
        products[pid]["stock"] -= qty

    total = cart_summary()["total"]
    clear_cart()

    return f"Ödeme başarılı. Toplam: {total:.2f}"