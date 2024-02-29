# Задание: калькулятор
# Имя исполнителя: Шедльбергер Екатерина


def calculate(expression):
    try:
        # Разбиваем строку на операнды и оператор
        parts = expression.split()
        if len(parts) != 3:
            raise ValueError("Неверный формат ввода. Попробуйте например: '2 + 3'")
        
        # Получаем операнды и оператор
        a, op, b = parts
        
        # Проверяем, что оба операнда являются числами
        if not (a.isdigit() and b.isdigit()):
            raise ValueError("Операнды должны быть числами")
        
        # Преобразуем операнды в целые числа
        a = int(a)
        b = int(b)
        
        # Проверяем, что операнды являются целыми числами от 1 до 10 включительно
        if not (1 <= a <= 10 and 1 <= b <= 10):
            raise ValueError("Операнды должны быть целыми числами от 1 до 10")
        
        # Проверяем, что оператор допустимый
        if op not in ['+', '-', '*', '/']:
            raise ValueError("Недопустимый оператор: должен быть одним из '+', '-', '*', '/'")
        
        # Выполняем операцию
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            result = a // b  # Целочисленное деление, остаток отбрасывается
            print("Результатом операции деления является целое число, остаток отбрасывается.")
            return result
    except ValueError as ve:
        raise ValueError("Ошибка при обработке ввода: {}".format(ve))

# Пример использования
while True:
    try:
        expression = input("Калькулятор для математической операции - два операнда и один оператор (+, -, /, *)\nВведите выражение (например, 2 + 3): ")
        result = calculate(expression)
        print("Результат:", result)
    except ValueError as e:
        print(e)




 
