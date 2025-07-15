import re

def normalize_phone(phone_number):
    patern = r"[^\d+]"
    cleaned = re.sub(patern, "",  phone_number.strip()) # тут буде видалено все окрім цифр та символа "+"

    if cleaned.startswith("+380"):
        return cleaned # якщо є +380 то повертаємо без змін

    elif cleaned.startswith("380"):
        return "+" + cleaned # якщо починається без "+" то додаємо його

    elif not cleaned.startswith("+"):
        return "+38" + cleaned # якщо номер без 38 але з "+" додаєм все разом

    return cleaned

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print(sanitized_numbers)
