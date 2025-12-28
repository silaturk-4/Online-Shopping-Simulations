import os


def top_selling_products(orders: list, limit: int = 5) -> list:  #en çok satan ürünler
    sales = {}

    for order in orders:
        for item in order["items"]:
            name = item["product"]
            qty = item["qty"]

            if name in sales:
                sales[name] += qty
            else:
                sales[name] = qty

    sorted_sales = sorted(sales.items(), key=lambda x: x[1], reverse=True)
    return sorted_sales[:limit]


def sales_summary(orders: list) -> dict:   #satış özeti
    total_orders = len(orders)
    total_revenue = 0

    for order in orders:
        for item in order["items"]:
            total_revenue += item["qty"] * item["price"]

    if total_orders > 0:
        average_order = total_revenue / total_orders
    else:
        average_order = 0

    return {
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "average_order": round(average_order, 2)
    }


def export_report(data: dict, filename: str) -> str:    #rapor dışa aktarma
    if not os.path.exists("reports"):
        os.mkdir("reports")

    path = "reports/" + filename

    file = open(path, "w", encoding="utf-8")
    for key in data:
        file.write(f"{key}: {data[key]}\n")
    file.close()

    return path


def admin_dashboard(products: list, orders: list) -> None:     #yönetici paneli
    print("\n=== ADMIN DASHBOARD ===")

    summary = sales_summary(orders)
    print("Total Orders:", summary["total_orders"])
    print("Total Revenue:", summary["total_revenue"], "TL")
    print("Average Order:", summary["average_order"], "TL")

    print("\nTop Selling Products:")
    top_products = top_selling_products(orders)

    for item in top_products:
        print("-", item[0], ":", item[1], "sold")

    print("\nStock Alerts:")
    for p in products:
        if p["stock"] < p["threshold"]:
            print("⚠ Reorder needed:", p["name"], "(Stock:", p["stock"], ")")



products = [
    {"name": "Laptop", "price": 15000, "stock": 5, "threshold": 3},
    {"name": "Mouse", "price": 300, "stock": 2, "threshold": 5},
    {"name": "Keyboard", "price": 700, "stock": 10, "threshold": 4}
]

orders = [
    {
        "id": 1,
        "items": [
            {"product": "Laptop", "qty": 1, "price": 15000},
            {"product": "Mouse", "qty": 2, "price": 300}
        ]
    },
    {
        "id": 2,
        "items": [
            {"product": "Mouse", "qty": 1, "price": 300},
            {"product": "Keyboard", "qty": 1, "price": 700}
        ]
    }
]

# Admin dashboard
admin_dashboard(products, orders)

# Report export
summary = sales_summary(orders)
file_path = export_report(summary, "sales_report.txt")

print("\nReport saved to:", file_path)
