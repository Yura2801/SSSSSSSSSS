import csv
from datetime import datetime
# 1)Функция добавления товара в базу
def add_a_product(file):
    name_product = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    quantity = int(input("Введите количество товара: "))
    print("Товар успешно добавлен!")
    with open(file, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([name_product, price, quantity])
        
# 2)Функция редактирования товаров
def edit_product(file):
    target_product = input("Введите название товара для редактирования: ")

    with open(file, mode='r', newline='', encoding='utf-8') as csvfile:
        rows = list(csv.reader(csvfile))
        found = False

        for row in rows:
            if row[0] == target_product:
                found = True
                row[0] = input("Введите новое название товара: ")
                row[1] = (input("Введите новую цену товара: "))
                row[2] = (input("Введите новое количество товара: "))
                break

        if not found:
            print("Товар не найден.")
        else:
            with open(file, mode='w', newline='', encoding='utf-8') as write_csvfile:
                writer = csv.writer(write_csvfile)
                writer.writerows(rows)
        print("Товар успешно отредактирован")
# 3)функция удаления товаров
def delete_product(file):
    target_product = input("Введите название товара для удаления: ")

    with open(file, mode='r', newline='', encoding='utf-8') as csvfile:
        rows = list(csv.reader(csvfile))
        found = False

        for row in rows:
            if row[0] == target_product:
                found = True
                rows.remove(row)
                break

        if not found:
            print("Товар не найден.")
        else:
            with open(file, mode='w', newline='', encoding='utf-8') as write_csvfile:
                writer = csv.writer(write_csvfile)
                writer.writerows(rows)
            print("Товар успешно удален")
def generate_sales_report(file, start_date, end_date):
    file = 'sales_history.csv' 
    sales_report = []
    with open(file, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Предполагается, что дата продажи хранится в каждой строке (предположим, это первый элемент)
            sale_date = row[0]  # Предположим, что дата находится в первом столбце
            # Проверяем, попадает ли дата в заданный период
            if start_date <= sale_date <= end_date:
                sales_report.append(row)

    if not sales_report:
        print("Нет продаж за указанный период.")
    else:
        print("Отчет о продажах за период:")
        for sale in sales_report:
            print(sale)  # Вывод информации о продажах за указанный период

def main_menu():
    print("Добро пожаловать в систему управления продуктами!")
    print("1. Добавить продукт")
    print("2. Редактировать продукт")
    print("3. Удалить продукт")
    print("4. Сформировать отчет о продажах")
    print("5. Выход")

def run_console():
    name_file = "data_base.csv"  
    while True:
        main_menu()
        выбор = input("Введите ваш выбор (1-5): ")

        if выбор == '1':
            add_a_product(name_file)
        elif выбор == '2':
            edit_product(name_file)
        elif выбор == '3':
            delete_product(name_file)
        elif выбор == '4':
            start_date = input("Введите начальную дату (ГГГГ-ММ-ДД): ")
            end_date = input("Введите конечную дату (ГГГГ-ММ-ДД): ")
            generate_sales_report(name_file, start_date, end_date)
        elif выбор == '5':
            print("Завершение программы. До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 5.")
if __name__ == "__main__":
    run_console()
# 4)Поиск товара 
def search_product(file):
    target_product = input("Введите название товара для поиска: ")
    with open(file, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        found = False

        for row in reader:
            if row[0] == target_product:
                found = True
                print(f"Название товара: {row[0]}")
                print(f"Цена товара: {row[1]}")
                print(f"Количество товара: {row[2]}")
                break

        if not found:
            print("Товар не найден.")
            search_product('data_base.csv')

# 5)читает данные из файла CSV, ожидая, что первый столбец содержит названия продуктов, а второй столбец - цены.
def load_products_from_file(file):
    products = {}
    with open(file, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            product_name, price = row[0], float(row[1])
            products[product_name] = price
    return products
# Функция добавления товара в корзину
def add_to_cart(cart, products):
    product_name = input("Введите название товара: ")
    quantity = int(input("Введите количество товара: "))

    if product_name in products:
        cart.append((product_name, quantity))
        print(f"{product_name} добавлен в Корзину.")
    else:
        print("Товар не найден.")
# Функция для удаления товара из корзины
def remove_from_cart(cart):
    product_name = input("Введите название товара для удаления: ")

    found = False
    for item in cart:
        if item[0] == product_name:
            cart.remove(item)
            found = True
            print(f"{product_name} удален из корзины.")
            break

    if not found:
        print("Такого товара нет в Корзине.")

# Функция печати чека
def print_receipt(cart, products, discount=0):
    print("Чек:")
    total = 0
    for item, quantity in cart:
        if item in products:
            price = products[item]
            item_total = price * quantity
            total += item_total
            print(f"{item}: {quantity} x {price} = {item_total}")

    if discount > 0:
        discount_amount = total * (discount / 100)
        total -= discount_amount
        print(f"Скидка {discount}%: -{discount_amount}")

    print(f"Итого к оплате: {total}")

# Функция расчета итоговой суммы
def calculate_total(cart, products):
    total = 0

    for item, quantity in cart:
        if item in products:
            total += products[item] * quantity

    return total

# Функция применения скидки
def apply_discount(total, discount):
    discounted_total = total - (total * (discount / 100))
    print(f"Применена скидка {discount}%. Итоговая сумма: {discounted_total}")
    return discounted_total

# Функция обработки платежа
def process_payment(total):
    amount_paid = float(input("Введите сумму для оплаты: "))

    if amount_paid >= total:
        change = amount_paid - total
        print(f"Спасибо за покупку! Ваша сдача: {change}")
        return True
    else:
        print("Недостаточно средств для оплаты.")
        return False

# Функция оформления продажи
def make_sale(file, products):
    cart = []
    discount = 0
    discounted_total = 0
    while True:
        action = input("Введите команду (search - Поиск товара / add_to_cart - Добавления товара в корзину / remove_from_cart - Удаление товара из корзины / calculate_total - сумма покупки / apply_discount - применение скидки/ process_payment - Итоговая сумма оплаты / finish_sale -закончить покупку): ")

        if action == "add_to_cart":
            add_to_cart(cart, products)
        elif action == "search":
            search_product('data_base.csv')
        elif action == "remove_from_cart":
            remove_from_cart(cart)
        elif action == "calculate_total":
            total = calculate_total(cart, products)
            print(f"Итоговая сумма: {total}")
        elif action == "apply_discount":
            discount = float(input("Введите размер скидки (%): "))
            total = calculate_total(cart, products)  # Calculate total here
            discounted_total = apply_discount(total, discount) 
        elif action == "process_payment":
            if "total" not in locals():
                print("Сначала рассчитайте общую сумму покупки.")
            elif process_payment(total):
                print_receipt(cart, products,discount)  
                # Получение текущей даты и времени
                sale_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Обновление истории продаж в файле
                with open(file, mode='a', newline='', encoding='utf-8') as sales_history:
                    writer = csv.writer(sales_history, delimiter=',')
                    writer.writerow([sale_date, cart, total - (total * (discount / 100))])  # Добавление даты продажи в историю продаж
                break
        elif action == "finish_sale":
            if "total" not in locals():
                print("Сначала рассчитайте общую сумму покупки.")
            else:
                print_receipt(cart, products,discount)  
                print(f"Итоговая сумма с учетом скидки: {discounted_total}")
                break
        else:
            print("Неверная команда. Попробуйте снова.")
        


