from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S24 Ultra", "+79997772131"),
    Smartphone("iPhone", "14 PRO MAX", "+79886667788"),
    Smartphone("Xiaomi", "Note 4X ", "+79775554455"),
    Smartphone("Realme", "9 PRO", "+79664449898"),
    Smartphone("Huawei", "P70X", "+79559993345"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")

