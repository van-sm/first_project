from dotenv import load_dotenv
import os

# Загружаем переменные из .env файла
load_dotenv()

def print_author():
    # Читаем значение из переменной окружения AUTHOR
    author = os.getenv('AUTHOR')
    
    if author is None:
        author = "Неизвестный автор"
        print(f"Внимание: переменная AUTHOR не установлена!")
    else:
        print(f"Автор проекта: {author}")

# Вызовем функцию для проверки
print_author()
