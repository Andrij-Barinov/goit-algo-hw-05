class HashTable:
    def __init__(self, size):
        # Ініціалізація хеш-таблиці з заданим розміром
        self.size = size
        # Створення списку (масиву) з пустими списками (ланцюжками) для кожного слоту таблиці
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        # Обчислення хешу ключа та приведення його в межі розміру таблиці
        return hash(key) % self.size

    def insert(self, key, value):
        # Обчислення індексу в таблиці для даного ключа
        key_hash = self.hash_function(key)
        key_value = [key, value]

        # Перевірка, чи ключ уже існує в ланцюжку
        for pair in self.table[key_hash]:
            if pair[0] == key:
                # Якщо ключ знайдений, оновити значення
                pair[1] = value
                return
        # Якщо ключ не знайдений, додати нову пару ключ-значення до ланцюжка
        self.table[key_hash].append(key_value)

    def get(self, key):
        # Обчислення індексу в таблиці для даного ключа
        key_hash = self.hash_function(key)
        
        # Перевірка, чи існує ключ у відповідному ланцюжку
        for pair in self.table[key_hash]:
            if pair[0] == key:
                # Якщо ключ знайдений, повернути його значення
                return pair[1]
        # Якщо ключ не знайдений, повернути None
        return None

    def delete(self, key):
        # Обчислення індексу в таблиці для даного ключа
        key_hash = self.hash_function(key)
        
        # Перевірка, чи існує ключ у відповідному ланцюжку
        for index, pair in enumerate(self.table[key_hash]):
            if pair[0] == key:
                # Якщо ключ знайдений, видалити його з ланцюжка
                del self.table[key_hash][index]
                return True
        # Якщо ключ не знайдений, повернути False
        return False

# Тестування
H = HashTable(5)  # Створення хеш-таблиці з 5 слотами
H.insert("apple", 10)   # Вставка пари "apple": 10
H.insert("orange", 20)  # Вставка пари "orange": 20
H.insert("banana", 30)  # Вставка пари "banana": 30

print(H.get("apple"))   # Виведе: 10 (отримує значення за ключем "apple")
H.delete("apple")       # Видаляє пару з ключем "apple"
print(H.get("apple"))   # Виведе: None (оскільки ключ "apple" був видалений)

print(H.get("orange"))  # Виведе: 20 (отримує значення за ключем "orange")
H.delete("orange")      # Видаляє пару з ключем "orange"
print(H.get("orange"))  # Виведе: None (оскільки ключ "orange" був видалений)

print(H.get("banana"))  # Виведе: 30 (отримує значення за ключем "banana")
H.delete("banana")      # Видаляє пару з ключем "banana"
print(H.get("banana"))  # Виведе: None (оскільки ключ "banana" був видалений)
