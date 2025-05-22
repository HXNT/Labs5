import re
from collections import Counter
import time


# Загрузка и предобработка текста
def preprocess_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    # Извлекаем слова (включая дефисы и апострофы)
    words = re.findall(r'\b[а-яёa-z\-]+\b', text)
    freq = Counter(words)
    return freq


# Поиск слов по запросу
def search_words(query, freq_dict, max_results=20):
    if len(query) < 3:
        print("Введите минимум 3 символа.")
        return []
    query = query.lower()
    matched = [(word, freq) for word, freq in freq_dict.items() if query in word]
    # Сортировка по убыванию частоты
    matched.sort(key=lambda x: -x[1])
    return matched[:max_results]


# Основная программа
def main():
    start_time = time.time()
    freq_dict = preprocess_text('voina-i-mir.txt')  # Укажите путь к файлу
    print(f"Текст обработан за {time.time() - start_time:.2f} секунд.")

    while True:
        query = input("\nВведите строку для поиска (не менее 3 символов, 'выход' — завершить): ").strip()
        if query.lower() == 'выход':
            break
        start_query = time.time()
        results = search_words(query, freq_dict)
        print(f"Результаты поиска ({len(results)} слов):")
        for word, freq in results:
            print(f"{word} — {freq} раз")
        print(f"Поиск занял {time.time() - start_query:.2f} секунд.")


if __name__ == "__main__":
    main()
